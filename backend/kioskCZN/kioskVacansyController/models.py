from django.db import models


class Districts(models.Model):
    """Район"""
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(verbose_name='Наименование района', max_length=256)
    min_code = models.BigIntegerField(verbose_name='Наименьший порог кода района')
    max_code = models.BigIntegerField(verbose_name='Наибольший порог кода района')
    work_places = models.BigIntegerField(verbose_name='Кол-во рабочих мест', default=0)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'
        db_table = 'vacansy_district'


class Vacansy(models.Model):
    """Вакансия"""
    id = models.TextField(verbose_name='id', primary_key=True, db_column='id')
    stateRegionCode = models.TextField(verbose_name='stateRegionCode', default='Отсутствует', db_column='stateRegionCode')
    vacancyName = models.TextField(verbose_name='vacancyName', default='Отсутствует', db_column='vacancyName')
    codeProfessionalSphere = models.TextField(verbose_name='codeProfessionalSphere', default='Отсутствует', db_column='codeProfessionalSphere')
    professionalSphereName = models.TextField(verbose_name='professionalSphereName', default='Отсутствует', db_column='professionalSphereName')
    vacancyAddress = models.TextField(verbose_name='vacancyAddress', default='Отсутствует', db_column='vacancyAddress')
    vacancyAddressAdditionalInfo  = models.TextField(verbose_name='vacancyAddressAdditionalInfo', default='Отсутствует', db_column='vacancyAddressAdditionalInfo')
    salary = models.TextField(verbose_name='salary', default='Отсутствует', db_column='salary')
    salaryMin = models.IntegerField(verbose_name='salaryMin', default=0, db_column='salaryMin')
    salaryMax = models.IntegerField(verbose_name='salaryMax', default=999999, db_column='salaryMax')
    socialProtecteds = models.TextField(verbose_name='socialProtecteds', default='Отсутствует', db_column='socialProtecteds')
    languageKnowledge = models.TextField(verbose_name='languageKnowledge', default='Отсутствует', db_column='languageKnowledge') #по данным с вакансиям, тут приходит list, но нам нужно сюда отпралвять строку просто с языками через ,
    busyType = models.TextField(verbose_name='busyType', default='Отсутствует', db_column='busyType')
    skills = models.TextField(verbose_name='skills', default='Отсутствует', db_column='skills') #аналогично, как с languageKnowledge, также строка с навыками через ,
    #ключи с workPlace
    workPlaceForeign = models.BooleanField(verbose_name='workPlaceForeign', blank=True, null=True, db_column='workPlaceForeign')
    workPlaceOrdinary = models.BooleanField(verbose_name='workPlaceOrdinary', blank=True, null=True, db_column='workPlaceOrdinary')
    workPlaceQuota = models.BooleanField(verbose_name='workPlaceQuota', blank=True, null=True, db_column='workPlaceQuota')
    workPlaceSpecial = models.BooleanField(verbose_name='workPlaceSpecial', blank=True, null=True, db_column='workPlaceSpecial')
    #конец workPlace

    trainingDays = models.IntegerField(verbose_name='trainingDays', default=0, db_column='trainingDays')
    shift = models.TextField(verbose_name='shift', default='Отсутствует', db_column='shift')  #аналогично, как с languageKnowledge, также строка с смежность или че через , хз я не понял
    hardSkills = models.TextField(verbose_name='hardSkills', default='Отсутствует', db_column='hardSkills') #аналогично, как с languageKnowledge, также строка через ,
    softSkills = models.TextField(verbose_name='softSkills', default='Отсутствует', db_column='softSkills') #аналогично, как с languageKnowledge, также строка через ,
    experienceRequirements = models.IntegerField(verbose_name='experienceRequirements', default=0, db_column='experienceRequirements')
    scheduleType = models.TextField(verbose_name='scheduleType', default='Отсутствует', db_column='scheduleType')
    careerPerspective = models.BooleanField(verbose_name='careerPerspective', default=False, db_column='careerPerspective')
    codeExternalSystem = models.TextField(verbose_name='codeExternalSystem', default='Отсутствует', db_column='codeExternalSystem')
    needMedcard = models.TextField(verbose_name='needMedcard', default='Отсутствует', db_column='needMedcard')
    sourceType = models.TextField(verbose_name='sourceType', default='Отсутствует', db_column='sourceType')
    requiredDriveLicense = models.TextField(verbose_name='requiredDriveLicense', default='Отсутствует', db_column='requiredDriveLicense')  #аналогично, как с languageKnowledge, также строка через ,
    changeTime = models.TextField(verbose_name='changeTime', default='Отсутствует', db_column='changeTime')
    contactPerson = models.TextField(verbose_name='contactPerson', default='Отсутствует', db_column='contactPerson')
    fullCompanyName = models.TextField(verbose_name='fullCompanyName', default='Отсутствует', db_column='fullCompanyName')
    companyBusinessSize = models.TextField(verbose_name='companyBusinessSize', default='Отсутствует', db_column='companyBusinessSize')
    dateModify = models.TextField(verbose_name='dateModify', default='Отсутствует', db_column='dateModify')
    workPlaces = models.IntegerField(verbose_name='workPlaces', default=1, db_column='workPlaces')
    isUzbekistanRecruitment = models.BooleanField(verbose_name='isUzbekistanRecruitment', default=False, db_column='isUzbekistanRecruitment')
    federalDistrictCode = models.IntegerField(verbose_name='federalDistrictCode', default=0, db_column='federalDistrictCode')
    datePublished = models.TextField(verbose_name='datePublished', default='Отсутствует', db_column='datePublished')
    accommodationCapability = models.BooleanField(verbose_name='accommodationCapability', default=False, db_column='accommodationCapability')
    foreignWorkersCapability = models.BooleanField(verbose_name='foreignWorkersCapability', default=False, db_column='foreignWorkersCapability')
    isQuoted = models.BooleanField(verbose_name='isQuoted', default=False, db_column='isQuoted')
    creationDate = models.TextField(verbose_name='creationDate', default='Отсутствует', db_column='creationDate')
    responsibilities = models.TextField(verbose_name='responsibilities',default='Отсутствует', db_column='responsibilities')
    addressCode = models.BigIntegerField(verbose_name='addressCode', default=0, db_column='addressCode')
    regionName = models.TextField(verbose_name='regionName', default='Отсутствует', db_column='regionName')
    status = models.TextField(verbose_name='status', default='Отсутствует', db_column='status')
    vacancyUrl = models.TextField(verbose_name='vacancyUrl', default='Отсутствует', db_column='vacancyUrl')
    #ключи с geo
    latitude = models.FloatField(verbose_name='latitude', default=0.0, blank=True, null=True, db_column='latitude')
    longitude = models.FloatField(verbose_name='longitude', default=0.0, blank=True, null=True, db_column='longitude')
    #конец ключей с geo

    #ключи с educationRequirements
    educationType = models.TextField(verbose_name='educationType', default='Отсутствует', blank=True, null=True, db_column='educationType')
    #конец ключей с educationRequirements (но не факт)

    # есть такой ключи premium там идет {} хз зачем там

    #ключи с company
    companyCode = models.TextField(verbose_name='companyCode', default='Отсутствует', db_column='companyCode')
    url = models.TextField(verbose_name='url', default='Отсутствует', db_column='url')
    inn = models.TextField(verbose_name='inn', default='Отсутствует', db_column='inn')
    kpp = models.TextField(verbose_name='kpp', default='Отсутствует', db_column='kpp')
    ogrn = models.TextField(verbose_name='ogrn', default='Отсутствует', db_column='ogrn')
    #конец ключей с company

    isModerated = models.BooleanField(verbose_name='isModerated', blank=True, null=True, db_column='isModerated')
    deleted = models.BooleanField(verbose_name='deleted', blank=True, null=True, db_column='deleted')
    visibility = models.TextField(verbose_name='visibility', default='Отсутствует', blank=True, null=True, db_column='visibility')

    #ключи с contactList
    contactType = models.TextField(verbose_name='contactType', default='Отсутствует', db_column='contactType')
    contactValue = models.TextField(verbose_name='contactValue', default='Отсутствует', db_column='contactValue')
    isModerated = models.BooleanField(verbose_name='isModerated', null=True, blank=True, db_column='isModerated')
    isPreferred = models.BooleanField(verbose_name='isPreferred', null=True, blank=True, db_column='isPreferred')


    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        db_table = 'vacansy'