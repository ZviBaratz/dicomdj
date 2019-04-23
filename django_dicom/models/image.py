import numpy as np
import pydicom

from django.db import models
from django.urls import reverse
from django_dicom.models.dicom_entity import DicomEntity
from django_dicom.models.validators import digits_and_dots_only, validate_file_extension
from django_dicom.reader import HeaderInformation


class Image(DicomEntity):
    """
    A model to represent a single DICOM_ image. This model is meant to be
    instantiated with the `file` field set to some *.dcm* file, and then it is
    updated automatically by inspection of the file's header information.

    .. _DICOM: https://www.dicomstandard.org/
    
    """

    # Stores a reference to the image file.
    dcm = models.FileField(
        max_length=250, upload_to="dicom", validators=[validate_file_extension]
    )

    uid = models.CharField(
        max_length=64,
        unique=True,
        validators=[digits_and_dots_only],
        verbose_name="Image UID",
    )
    number = models.IntegerField(verbose_name="Image Number")
    date = models.DateField()
    time = models.TimeField()

    series = models.ForeignKey("django_dicom.Series", on_delete=models.PROTECT)

    _header = None
    FIELD_TO_HEADER = {
        "uid": "SOPInstanceUID",
        "number": "InstanceNumber",
        "date": "InstanceCreationDate",
        "time": "InstanceCreationTime",
    }

    def __str__(self) -> str:
        return self.uid

    def get_absolute_url(self) -> str:
        return reverse("dicom:image_detail", args=[str(self.id)])

    def read_file(self, header_only: bool = False) -> pydicom.FileDataset:
        return pydicom.read_file(self.dcm.path, stop_before_pixels=header_only)

    def get_data(self) -> np.ndarray:
        return self.read_file(header_only=False).pixel_array

    def read_header(self) -> HeaderInformation:
        raw_header = self.read_file(header_only=True)
        return HeaderInformation(raw_header)

    def get_b_value(self) -> int:
        return self.header.get_value(("0019", "100c"))

    @property
    def header(self) -> HeaderInformation:
        if not isinstance(self._header, HeaderInformation):
            self._header = self.read_header()
        return self._header

    @property
    def slice_timing(self):
        return self.header.get_value(("0019", "1029"))

    @property
    def gradient_direction(self):
        return self.header.get_value(("0019", "100e"))

    class Meta:
        indexes = [models.Index(fields=["uid"]), models.Index(fields=["date", "time"])]

