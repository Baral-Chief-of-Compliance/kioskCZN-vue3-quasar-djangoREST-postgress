from django.db import models


class Districts(models.Model):
    """Район"""
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(verbose_name='Наименование района', max_length=256)
    min_code = models.BigIntegerField(verbose_name='Наименьший порог кода района')
    max_code = models.BigIntegerField(verbose_name='Наибольший порог кода района')
    work_place = models.BigIntegerField(verobose_name='Кол-во рабочих мест')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Района'
        db_table = 'vacansy_district'


class Vacansy(models.Model):
    """Вакансия"""
    id = models.CharField(verbose_name='id', max_length=256, primary_key=True)
    stateRegionCode = models.CharField(verbose_name='stateRegionCode', default='Отсутствует')
    vacancyName = models.CharField(verbose_name='vacancyName', default='Отсутствует', max_length=512)
    codeProfessionalSphere = models.CharField(verbose_name='codeProfessionalSphere', default='Отсутствует', max_length=512)
    professionalSphereName = models.CharField(verbose_name='professionalSphereName', default='Отсутствует', max_length=512)
    vacancyAddress = models.CharField(verbose_name='vacancyAddress', default='Отсутствует', max_length=512)
    vacancyAddressAdditionalInfo  = models.CharField(verbose_name='vacancyAddressAdditionalInfo', default='Отсутствует', max_length=512)
    salary = models.CharField(verbose_name='salary', default='Отсутствует', max_length=512)
    salaryMin = models.IntegerField(verbose_name='salaryMin', default=0)
    salaryMax = models.IntegerField(verbose_name='salaryMax', default=999999)
    socialProtecteds = models.CharField(verbose_name='socialProtecteds', default='Отсутствует')
    languageKnowledge = models.CharField(verbose_name='languageKnowledge', default='Отсутствует') #по данным с вакансиям, тут приходит list, но нам нужно сюда отпралвять строку просто с языками через ,
    busyType = models.CharField(verbose_name='busyType', default='Отсутствует')
    skills : str = Field(default='Отсутствует') #аналогично, как с languageKnowledge, также строка с навыками через ,
    #ключи с workPlace
    workPlaceForeign : Optional[bool] = Field(default=None)
    workPlaceOrdinary : Optional[bool] = Field(default=None)
    workPlaceQuota : Optional[bool] = Field(default=None)
    workPlaceSpecial : Optional[bool] = Field(default=None)
    #конец workPlace

    trainingDays : int = Field(default=0)
    shift : str = Field(default='Отсутствует')  #аналогично, как с languageKnowledge, также строка с смежность или че через , хз я не понял
    hardSkills : str = Field(default='Отсутствует') #аналогично, как с languageKnowledge, также строка через ,
    softSkills : str = Field(default='Отсутствует') #аналогично, как с languageKnowledge, также строка через ,
    experienceRequirements : int = Field(default=0)
    scheduleType : str = Field(default='Отсутствует')
    careerPerspective : bool = Field(default=False)
    codeExternalSystem : str = Field(default='Отсутствует')
    needMedcard : str = Field(default='Отсутствует')
    sourceType : str = Field(default='Отсутствует')
    requiredDriveLicense : str = Field(default='Отсутствует')  #аналогично, как с languageKnowledge, также строка через ,
    changeTime : str = Field(default='Отсутствует')
    contactPerson : str = Field(default='Отсутствует')
    fullCompanyName : str = Field(default='Отсутствует')
    companyBusinessSize : str = Field(default='Отсутствует')
    dateModify : str = Field(default='Отсутствует')
    workPlaces : int = Field(default=1)
    isUzbekistanRecruitment : bool = Field(default=False)
    federalDistrictCode : int 
    datePublished : str = Field(default='Отсутствует')
    accommodationCapability : bool = Field(default=False)
    foreignWorkersCapability : bool = Field(default=False)
    isQuoted : bool = Field(default=False)
    creationDate : str = Field(default='Отсутствует')
    responsibilities : str = Field(default='Отсутствует')
    addressCode : int = Field(
        default=0,
        sa_column=sa.Column(sa.BigInteger)
    )
    regionName : str = Field(default='Отсутствует')
    status : str = Field(default='Отсутствует')
    vacancyUrl : str = Field(default='Отсутствует')
    #ключи с geo
    latitude : Optional[float] = Field(default=0.0)
    longitude : Optional[float] = Field(default=0.0)
    #конец ключей с geo

    #ключи с educationRequirements
    educationType : str = Field(default='Отсутствует')
    #конец ключей с educationRequirements (но не факт)

    # есть такой ключи premium там идет {} хз зачем там

    #ключи с company
    companyCode : str = Field(default='Отсутствует')
    url : str = Field(default='Отсутствует')
    inn : str = Field(default='Отсутствует')
    kpp : str = Field(default='Отсутствует')
    ogrn : str = Field(default='Отсутствует')
    #конец ключей с company

    isModerated : Optional[bool] = Field(default=None)
    deleted : Optional[bool] = Field(default=None)
    visibility : str = Field(default='Отсутствует')

    #ключи с contactList
    contactType : str = Field(default='Отсутствует')
    contactValue : str = Field(default='Отсутствует')
    isModerated : Optional[bool] = Field(default=None)
    isPreferred : Optional[bool] = Field(default=None)