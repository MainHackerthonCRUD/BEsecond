from django.urls import path
from .views import *
from . import views

app_name = 'board'

'''
{
"title":"test",
"body":"test",
"star":3
}
{
"username":"honggyu",
"password1":"asdf1234qwer",
"password2":"asdf1234qwer",
"nickname":"hongddd"
}





{
    "id": 23,
    "nickname": "hongddd",
    "title": "test",
    "body": "test",
    "created_at": "2024-08-01",
    "star": "3"
}










--- 카카오 로그인 ---

카카오 로그인 요청을 보낸다.
카카오 서버에서 인가 코드를 돌려받는다.
코드를 카카오 서버에 보낸다.
카카오 서버에서 카카오 액세스 토큰을 돌려받는다.
액세스 토큰을 보내고 사용자 정보를 가져온다.
카카오 서버에서 돌려받은 사용자 정보로 우리 서버에 가입시킨다.


---- 정보 ---------
카카오 설정값
    사이트 도메인
    http://127.0.0.1:8000

    Redirect URI
    http://127.0.0.1:8000/kakao/

    rest api키
    6bf5f3d7db0da82bb551b5e113dcc846

----------------

(예시)
https://kauth.kakao.com/oauth/authorize?client_id=REST_API 키&redirect_uri=http://127.0.0.1:8000/&response_type=code

위 예시를 활용해서 링크를 만들어 접속해야 함


https://kauth.kakao.com/oauth/authorize?client_id=6bf5f3d7db0da82bb551b5e113dcc846&redirect_uri=http://127.0.0.1:8000/kakao&response_type=code

-> 리턴
http://127.0.0.1:8000/?code=A3K1DBDwXy8lOlpaogl3lzH2l6l8MX4jqVMc7GhTiSVQ0qS_K3Q3bQAAAAQKPCRZAAABkRa03MjE017PSiBv1Q
-> cdoe= 추출
code=rYMUccy9C6_qbdvCmnGU4_vpG7b-tfVT2lLpC_ausBtq16C3vRHL0wAAAAQKKiWQAAABkRPzZZ_mTYKY7N6ACw



grant_type=authorization_code (고정 값, 변경 필요 X)

client_id ( 내 애플리케이션의 4개의 앱 키 값 중 REST_API 키 )
	6bf5f3d7db0da82bb551b5e113dcc846

redirect_uri : http://127.0.0.1:8000/kakao/
            

code ( 위 로직에서 받은 인가 코드) / 요청할 때마다 변경됨

를 사용해서 url 만들어서 post 요청 보내기
(예시)
https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id=ee7b5032bbe401cf9fdbfc532c5b2f42&redirect_uri=http://127.0.0.1:8000/&code=W9TSSzc7R34TF3DYT3CBfBxQHuga7WkMMwEsCON0zR2r3vyZ0zR64zw01Y152d7C4u1UQAopcJ4AAAGCpkIs7Q'

(내가 수정)
https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id=ee7b5032bbe401cf9fdbfc532c5b2f42&redirect_uri=http://127.0.0.1:8000/&code=A3K1DBDwXy8lOlpaogl3lzH2l6l8MX4jqVMc7GhTiSVQ0qS_K3Q3bQAAAAQKPCRZAAABkRa03MjE017PSiBv1Q



-> 카카오에서 반환
{
    "access_token": "pNdtElYXpMCo3UWirIBsHU9WyJEhveBqAAAAAQo9cxgAAAGRFryFlgGXonZVdqHq",
    "token_type": "bearer",
    "refresh_token": "ZHx_jq_0wn7Kn2fmvNvAj2xrGlU9oxmIAAAAAgo9cxgAAAGRFryFkgGXonZVdqHq",
    "expires_in": 21599,
    "refresh_token_expires_in": 5183999
}


'''

urlpatterns = [
    # # 추가
    # path('rest-auth/kakao/', views.KakaoLogin.as_view(), name='kakao'),
    # path('rest-auth/naver/', views.NaverLogin.as_view(), name='naver'),
    # path('rest-auth/google/', views.GoogleLogin.as_view(), name='google'),
    # path('rest-auth/github/', views.GithubLogin.as_view(), name='github'),

    
    
    
    
    
    
    # json 파일 저장
    # path('savejson/',board_post),
    # 오류 생겨서 주석처리 해놨습니다.

    
    

# 병원
    # 전체 병원 리스트 조회 - OK
    path('home/', board_list),

    
    
    # 병원 이름 검색 - OK
    path('search/<str:name>/', hospital_name),

    # 병원 구 검색 - OK
    path('searchgu/<str:gu>/',hospital_gu),

    

# 리뷰
    # 병원 객체에 대해 리뷰 작성 - OK
    path('<int:pk>/comment/',comment_post),

    # 병원 id 값에 달린 댓글 가져오기 - OK
    path('<int:pk>/commentget/', comment_list),

    
    # 리뷰 객체 get, put,delete
    path('review/<int:board_pk>/<int:comment_pk>/',review_put_delete),



# 마이페이지
    # mypage - OK
    path('mypage/<str:pk>/',mypage),

    
    



# etc
    # 병원 객체 조회
    # 프론트 필요 없음
    path('hospital/<int:pk>/',board_detail),

    # 임시로 만든 병원 전체 POST
    # path('homehonggyu/',board_post),

    # 병원 데이터 저장 - 한번만 실행/접속
    path('post/', data_post),


    # 필요 없어짐
    # 개별 리뷰 페이지 - OK
    path('review/<int:pk>/',review_get),
    # id : 14 -> 삭제됨
]