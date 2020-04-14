from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models
from data import models as data_models

# Create your models here.


class PersonnelType(core_models.TimeStampedModel):

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    the_type = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PersonnelInfo(core_models.TimeStampedModel):

    personnel_type = models.ForeignKey(
        "PersonnelType", related_name="info", on_delete=models.PROTECT
    )
    number = models.IntegerField()
    report = models.ForeignKey(
        "PersonnelReport", related_name="info", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.personnel_type.name


class PersonnelReport(core_models.TimeStampedModel):

    department = models.ForeignKey(
        data_models.Department,
        related_name="personnel",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    country = CountryField()
    report_date = models.DateField(verbose_name="보고기준일")

    author = models.ForeignKey(
        user_models.User,
        related_name="personnel",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    koica = models.IntegerField(null=True, blank=True, verbose_name="KOICA 직원")
    koica_admin = models.IntegerField(null=True, blank=True, verbose_name="일반 행정원")
    v_codi = models.IntegerField(null=True, blank=True, verbose_name="봉사단 코디네이터")
    p_codi = models.IntegerField(null=True, blank=True, verbose_name="개발협력 코디네이터")
    yp = models.IntegerField(null=True, blank=True, verbose_name="YP")
    local_v = models.IntegerField(null=True, blank=True, verbose_name="사무소 파트 현지고용원")
    local_p = models.IntegerField(null=True, blank=True, verbose_name="봉사단 파트 현지고용원")

    koica_v = models.IntegerField(null=True, blank=True, verbose_name="KOICA 봉사단")
    advisor = models.IntegerField(null=True, blank=True, verbose_name="중장기 자문단")
    kmco = models.IntegerField(null=True, blank=True, verbose_name="다자협력전문가")
    global_doctor = models.IntegerField(null=True, blank=True, verbose_name="글로벌 협력의사")
    etc_v = models.IntegerField(null=True, blank=True, verbose_name="타 WFK봉사단(NIPA 등)")
    project_koica = models.IntegerField(
        null=True, blank=True, verbose_name="사무소 고용 프로젝트 인원"
    )
    project_etc = models.IntegerField(
        null=True, blank=True, verbose_name="외부소속 프로젝트 인원"
    )

    description = models.TextField(null=True, blank=True, verbose_name="참고사항")

    # 분류
    TOTAL_LIST = [
        "koica",
        "koica_admin",
        "v_codi",
        "p_codi",
        "yp",
        "local_v",
        "local_p",
        "koica_v",
        "advisor",
        "kmco",
        "global_doctor",
        "etc_v",
        "project_koica",
        "project_etc",
    ]

    # 사무소 근무인원
    OFFICE_LIST = [
        "koica",
        "koica_admin",
        "v_codi",
        "p_codi",
        "yp",
        "local_v",
        "local_p",
    ]

    # 현장 근무인원
    FIELD_LIST = [
        "koica_v",
        "advisor",
        "kmco",
        "global_doctor",
        "etc_v",
        "project_koica",
        "project_etc",
    ]

    def get_office_subtotal(self):
        return get_field_sum(PersonnelReport.OFFICE_LIST, self,)

    def get_field_subtotal(self):
        return get_field_sum(PersonnelReport.FIELD_LIST, self,)

    def get_total(self):
        return get_field_sum(PersonnelReport.TOTAL_LIST, self,)

    def get_office_value(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in PersonnelReport._meta.fields
            if field.name in PersonnelReport.OFFICE_LIST
        ]

    def get_field_value(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in PersonnelReport._meta.fields
            if field.name in PersonnelReport.FIELD_LIST
        ]


def get_field_sum(x: list, self):
    return sum(
        filter(
            lambda x: x != None,
            [
                field.value_from_object(self)
                for field in PersonnelReport._meta.fields
                if field.name in x
            ],
        )
    )
