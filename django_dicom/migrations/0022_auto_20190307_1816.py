# Generated by Django 2.1.4 on 2019-03-07 18:16

from django.db import migrations, models
import django_dicom.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_dicom', '0021_auto_20190219_1351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='nifti',
            new_name='_nifti',
        ),
        migrations.AlterField(
            model_name='series',
            name='modality',
            field=models.CharField(choices=[('AR', 'Autorefraction'), ('ASMT', 'Content Assessment Results'), ('AU', 'Audio'), ('BDUS', 'Bone Densitometry (ultrasound)'), ('BMD', 'Bone Densitometry (X-Ray)'), ('BI', 'Biomagnetic imaging'), ('CR', 'Computed Radiography'), ('CT', 'Computed Tomography'), ('CTPROTOCOL', 'CT Protocol (Performed)'), ('DG', 'Diaphanography'), ('DOC', 'Document'), ('DX', 'Digital Radiography'), ('ECG', 'Electrocardiography'), ('EPS', 'Cardiac Electrophysiology'), ('EDS', 'Endoscopy'), ('FID', 'Fiducials'), ('GM', 'General Microscopy'), ('HC', 'Hard Copy'), ('HD', 'Hemodynamic Waveform'), ('IO', 'Intra-Oral Radiography'), ('IOL', 'Intraocular Lens Data'), ('IVOCT', 'Intravascular Optical Coherence Tomography'), ('IVUS', 'Intravascular Ultrasound'), ('KER', 'Keratometry'), ('KO', 'Key Object Selection'), ('LEN', 'Lensometry'), ('LS', 'Laser surface scan'), ('MG', 'Mammography'), ('MR', 'Magnetic Resonance'), ('M3D', 'Model for 3D Manufacturing'), ('NM', 'Nuclear Medicine'), ('OAM', 'Ophthalmic Axial Measurements'), ('OCT', 'Optical Coherence Tomography (non-Ophthalmic)'), ('OP', 'Ophthalmic Photography'), ('OPM', 'Ophthalmic Mapping'), ('OPT', 'Ophthalmic Tomography'), ('OPTBSV', 'Ophthalmic Tomography B-scan Volume Analysis'), ('OPTENF', 'Ophthalmic Tomography En Face'), ('OPV', 'Ophthalmic Visual Field'), ('OSS', 'Optical Surface Scan'), ('OT', 'Other'), ('PLAN', 'Plan'), ('PR', 'Presentation State'), ('PT', 'Positron emission tomography (PET)'), ('PX', 'Panoramic X-Ray'), ('REG', 'Registration'), ('RESP', 'Respiratory Waveform'), ('RF', 'Radio Fluoroscopy'), ('RG', 'Radiographic imaging (conventional film/screen)'), ('RTDOSE', 'Radiotherapy Dose'), ('RTIMAGE', 'Radiotherapy Image'), ('RTPLAN', 'Radiotherapy Plan'), ('RTRECORD', 'RT Treatment Record'), ('RTSTRUCT', 'Radiotherapy Structure Set'), ('RWV', 'Real World Value Map'), ('SEG', 'Segmentation'), ('SM', 'Slide Microscopy'), ('SMR', 'Stereometric Relationship'), ('SR', 'SR Document'), ('SRF', 'Subjective Refraction'), ('STAIN', 'Automated Slide Stainer'), ('TG', 'Thermography'), ('US', 'Ultrasound'), ('VA', 'Visual Acuity'), ('XA', 'X-Ray Angiography'), ('XC', 'External-camera Photography')], default='MR', max_length=10),
        ),
        migrations.AlterField(
            model_name='series',
            name='scanning_sequence',
            field=django_dicom.models.fields.ChoiceArrayField(base_field=models.CharField(choices=[('SE', 'Spin Echo'), ('IR', 'Inversion Recovery'), ('GR', 'Gradient Recalled'), ('EP', 'Echo Planar'), ('RM', 'Research Mode')], max_length=2), blank=True, null=True, size=5),
        ),
        migrations.AlterField(
            model_name='series',
            name='sequence_variant',
            field=django_dicom.models.fields.ChoiceArrayField(base_field=models.CharField(choices=[('SK', 'Segmented k-Space'), ('MTC', 'Magnetization Transfer Contrast'), ('SS', 'Steady State'), ('TRSS', 'Time Reversed Steady State'), ('SP', 'Spoiled'), ('MP', 'MAG Prepared'), ('OSP', 'Oversampling Phase'), ('NONE', 'None')], max_length=4), blank=True, help_text='Variant of the Scanning Sequence.', null=True, size=None),
        ),
    ]