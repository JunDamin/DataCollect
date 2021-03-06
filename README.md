# 안전센터 데이터 관리를 고려해서 한번 생각해 보자.

# View 부터 생각해보자.

설계를 하려고 하면 무엇을 위해서 하는가에 대한 목적을 기억해야 한다. 보고 싶은 것이 무엇이 있기 때문에 이렇게 만드는 것이기 때문이다. 그래서 무엇을 보고자 하는지 정의를 하면 어떤 기능과 어떤 것들이 들어가야 하는지 설계하기가 쉬워지는 것같다.

## 사무소를 위해서 필요한 것
 - 사무소 자료를 모아서 보는 기능
 - 각 자료별로 이력을 볼 수 있으면서 수정할 수 있는 기능
 - 모아보는 곳에서 자료를 입력하는 곳으로 넘어가는 그닝

 ## 총괄부서를 위해서 필요한 기능
  - 어떤 사무소가 업로드 했는지, 안했는지 확인하는 기능
    - 사무소별 근무인원/종류/인원
    - 현장 근무인원/종류/인원
    - 기타 인원/종류/인원
  - 안전위험예지를 최신 기록을 중심으로 종합해서 보는 기능
  - 주요사건을 달력과 함께 볼 수 있는 기능
  - 파견인력 현황을 달력과 함께 볼 수 있는 기능
  - 소계 및 합계 보는 것
  - 국가별 항목별로 상세를 볼 수 있는 페이지로 이동하는 것

## 기타 아이디어

  - 입력방식
    - 개별 사건별 입력?
    - 입력자료는? 사건/세부내역
    - Formset?
    - 시즌의 경우 어떻게 표기할 것인가?
  - 총괄표기
    - 국가별 색 설정?
    - 국가별 선택기능
    - 전체 기능
    - 타임라인 형식
    - 달력 표기는 날짜 + 카드 형식
      - 카드 제목을 누르면 하이퍼링크로 이동하게
      - 사건을 추가도 간단하게 할려면 어떻게 해야 할까?
      - 보이는 곳에서 위치를 잡아서 추가할 수 있게 해야 한다.
    - 국가명을 누르면 국가 종합 페이지로 이동해서 일정을 볼 수 있도록 하기
    - 국가종합 페이지는 안전위험예지/해외파견인력현황/주요사건 목록을 모두 볼 수 있도록 한다.


# Model을 생각하자

결국 모델의 시작은 엑셀이나 기존 관리하는 자료의 형태를 잘 이해하는 것에서 시작한다. 

## 월간 주간 예지 Model
- 국가
  - 국가 모델 사용((추가 가능성 낮음)
- 작성일자
- 위험수준(변경 가능성 매우 낮음/별도로 추가될 경우 새로운 필드 생성하는 것이 나을 것)
- 위험분류(변경 가능성 낮음/기타에서 추가될 가능성이 있음)
- - 위험분류 모델 사용
- 내용
- 조치사항
  
## 해외파견인력
- 구분
  - 파견구분 Class 만들기(추가 가능성은 높음)
  - 사무소
    - 파견직원
      - 코이카직원
      - 일반행정원
      - 봉사단코디네이터
      - 개발협력코디네이터
      - YP
    - 현지고용원
      - 사무소파트
  - 현장
    - 봉사단
      - KOICA봉사단
      - 중장기자문단
      - 다자협력전문가
      - 글로벌협력의사
      - 타 WFK봉사단
    - 프로젝트
- 인원
- 담당 사무소
  - 사무소 모델 
- 파견국가
- 갱신일자
  
파견인력의 경우에는 종류별로 만들어야 할 것처럼 처음에는 생각했지만 그렇게 하면 나중에 봉사단 종류등이 변경될 때 곤란할 수 있기 때문에 형태를 조금 다르게 접근해야 할 것으로 보인다. 즉 가장 작은 단위로 하고 그 위에 구분을 요소로 하는 것으로 해서 처리해야 할 것으로 보인다.

그리고 뷰에서는 각 종류별로 한꺼번에 입력할 수 있는 Formset을 활용해야 할 것으로 보이며
모든 종류가 Tree구조로 해서 Template에서 한꺼번에 잘 입력할 수 있게 하는 것이 좋을 것으로 보인다.

# 사무소 Model
- 국가
- 주소
- 지역구분
  - 추가 가능성은 적음
- 겸임국

# 주요사건 Model
- 국가
- 사건구분(추가가능성 높음)
- 사건명
- 세부사항


## 앱 구조

- 유저
- 기준자료
  - 사무소
  - 지역구분
  - 파견구분
- 코어
- 월간주간예지
- 파견인력현황
- 주요사건


#1 Model

#1.1 Core model

#1.2. users model

#1.3. data model

#1.3.1 data model change
 - 한 클래스가 여러 변수를 다른 한 클래스에서 참조할 경우 어떻게 되는가?

#1.4 event model

#1.5 personnel model
#1.5.1 create Personnel Report class

#1.6. prediction model

#1.7 Error manage
 - class should inherit models.Model
 - make urls

#1.7.2. Custom User setting
#2 Admin

#2.1 create admin

#2.1.1 
#3 sample data command

#4 View

#4.1 Copy Users Views

#4.2.1 Prediction Create View
- form에서 초기 값은 inital로 처리 가능
- orm에서 filter와 order_by로 가장 최신 선택가능

#4.3 Finish Event View

#4.3.1 Change employment to department

#4.3.2 Apply single method in template with JS

#4.4 Personnel View

#4.4.1 personnel report crud

#4.4.2 personnel report inline

#4.5 Create List View

#4.5.2 Create Personnel Report List View 

Q.
 - 어떻게 해야 ordering이 된 가장 최신 값만 표기할 수 있을까? 신규 등록할 때 최신자료로 일대일 맵핑
 - 어떻게 해야지 view에서 employment 유무를 확인해서 다른 곳으로 보낼 수 있을까? try-catch를 사용
 - 검색기능을 구현하자.
 - 부서페이지를 구현하자.




python anywhere 

import os
import sys

path = '/home/kakaodamin/kakaodamin.pythonanywhere.com'

if path not in sys.path:
    sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()