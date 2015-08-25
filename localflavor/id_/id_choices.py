from django.utils.translation import ugettext_lazy as _

#: Indonesia does not have an official Province code standard.
#: I decided to use unambiguous and consistent (some are common) 3-letter codes.
#: http://id.wikipedia.org/wiki/Daftar_provinsi_Indonesia
PROVINCE_CHOICES = (
    ('ACE', _('Aceh')),
    ('BLI', _('Bali')),
    ('BTN', _('Banten')),
    ('BKL', _('Bengkulu')),
    ('DIY', _('Yogyakarta')),
    ('JKT', _('Jakarta')),
    ('GOR', _('Gorontalo')),
    ('JMB', _('Jambi')),
    ('JBR', _('Jawa Barat')),
    ('JTG', _('Jawa Tengah')),
    ('JTM', _('Jawa Timur')),
    ('KBR', _('Kalimantan Barat')),
    ('KSL', _('Kalimantan Selatan')),
    ('KTG', _('Kalimantan Tengah')),
    ('KTM', _('Kalimantan Timur')),
    ('BBL', _('Kepulauan Bangka-Belitung')),
    ('KRI', _('Kepulauan Riau')),
    ('LPG', _('Lampung')),
    ('MLK', _('Maluku')),
    ('MUT', _('Maluku Utara')),
    ('NTB', _('Nusa Tenggara Barat')),
    ('NTT', _('Nusa Tenggara Timur')),
    ('PPA', _('Papua')),
    ('PPB', _('Papua Barat')),
    ('RIU', _('Riau')),
    ('SLB', _('Sulawesi Barat')),
    ('SLS', _('Sulawesi Selatan')),
    ('SLT', _('Sulawesi Tengah')),
    ('SLR', _('Sulawesi Tenggara')),
    ('SLU', _('Sulawesi Utara')),
    ('SMB', _('Sumatera Barat')),
    ('SMS', _('Sumatera Selatan')),
    ('SMU', _('Sumatera Utara')),
)

#: License plate prefixes
LICENSE_PLATE_PREFIX_CHOICES = (
    ('A', _('Banten')),
    ('AA', _('Magelang')),
    ('AB', _('Yogyakarta')),
    ('AD', _('Surakarta - Solo')),
    ('AE', _('Madiun')),
    ('AG', _('Kediri')),
    ('B', _('Jakarta')),
    ('BA', _('Sumatera Barat')),
    ('BB', _('Tapanuli')),
    ('BD', _('Bengkulu')),
    ('BE', _('Lampung')),
    ('BG', _('Sumatera Selatan')),
    ('BH', _('Jambi')),
    ('BK', _('Sumatera Utara')),
    ('BL', _('Nanggroe Aceh Darussalam')),
    ('BM', _('Riau')),
    ('BN', _('Kepulauan Bangka Belitung')),
    ('BP', _('Kepulauan Riau')),
    ('CC', _('Corps Consulate')),
    ('CD', _('Corps Diplomatic')),
    ('D', _('Bandung')),
    ('DA', _('Kalimantan Selatan')),
    ('DB', _('Sulawesi Utara Daratan')),
    ('DC', _('Sulawesi Barat')),
    ('DD', _('Sulawesi Selatan')),
    ('DE', _('Maluku')),
    ('DG', _('Maluku Utara')),
    ('DH', _('NTT - Timor')),
    ('DK', _('Bali')),
    ('DL', _('Sulawesi Utara Kepulauan')),
    ('DM', _('Gorontalo')),
    ('DN', _('Sulawesi Tengah')),
    ('DR', _('NTB - Lombok')),
    ('DS', _('Papua dan Papua Barat')),
    ('DT', _('Sulawesi Tenggara')),
    ('E', _('Cirebon')),
    ('EA', _('NTB - Sumbawa')),
    ('EB', _('NTT - Flores')),
    ('ED', _('NTT - Sumba')),
    ('F', _('Bogor')),
    ('G', _('Pekalongan')),
    ('H', _('Semarang')),
    ('K', _('Pati')),
    ('KB', _('Kalimantan Barat')),
    ('KH', _('Kalimantan Tengah')),
    ('KT', _('Kalimantan Timur')),
    ('L', _('Surabaya')),
    ('M', _('Madura')),
    ('N', _('Malang')),
    ('P', _('Jember')),
    ('R', _('Banyumas')),
    ('RI', _('Federal Government')),
    ('S', _('Bojonegoro')),
    ('T', _('Purwakarta')),
    ('W', _('Sidoarjo')),
    ('Z', _('Garut')),
)