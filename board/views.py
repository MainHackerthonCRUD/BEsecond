from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Board
from rest_framework.response import Response
from .serializers import BoardListSerializer, BoardDetailSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly
import requests
from .serializers import *
import json

'''

---- 정보 ---------
카카오 설정값
    사이트 도메인
    http://127.0.0.1:8000

    Redirect URI
    http://127.0.0.1:8000/kakao/

    rest api키
    6bf5f3d7db0da82bb551b5e113dcc846
'''
'''
(예시)
https://kauth.kakao.com/oauth/authorize?client_id=REST_API 키&redirect_uri=http://127.0.0.1:8000/&response_type=code
(변형)
https://kauth.kakao.com/oauth/authorize?
client_id=6bf5f3d7db0da82bb551b5e113dcc846&
redirect_uri=http://127.0.0.1:8000/&
response_type=code

(한 줄로 - 복붙용)
https://kauth.kakao.com/oauth/authorize?client_id=6bf5f3d7db0da82bb551b5e113dcc846&redirect_uri=http://127.0.0.1:8000/kakao/callback/&response_type=code
위 예시를 활용해서 링크를 만들어 접속해야 함
나중에 순서 바꿔서 해보기. 상관 없을 것 같음
'''


#------------mine-----------
from django.shortcuts import redirect


def kakao(request):

    kakao_api="https://kauth.kakao.com/oauth/authorize?"
    redirect_uri="https://yellowtaxi.store/kakao/callback/"
    client_id="6bf5f3d7db0da82bb551b5e113dcc846"
    response_type="code"

    return redirect(f"{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}&response_type={response_type}")


import requests
from member.models import CustomUser







def check_id(req_id):
    for user in CustomUser.objects.all():
        if user.username==req_id:
            return True
    return False






'''
https://kauth.kakao.com/oauth/authorize?client_id=6bf5f3d7db0da82bb551b5e113dcc846&redirect_uri=https://yellowtaxi.store/kakao/callback/&response_type=code
'''
@api_view(['GET'])
def kakako_callback(request):

    data={
        "grant_type"    :"authorization_code",
        "client_id":"6bf5f3d7db0da82bb551b5e113dcc846",
        "redirect_uri":"https://yellowtaxi.store/kakao/callback/",
        "code":request.GET["code"]
    }

    kakao_token_api="https://kauth.kakao.com/oauth/token"
    access_token=requests.post(kakao_token_api,data=data).json()['access_token']
    

    print()
    print()
    print()
    print()
    print(access_token)









    # ----------사용자 정보 가져오기-------------


    kakao_user_api="https://kapi.kakao.com/v2/user/me"
    header={
        f"Authorization : Bearer ${access_token}"
        }
    # data={
    #     "property_keys:['kakao_account.email']"
    # }
    
    # user_information=requests.get(kakao_user_api,headers=header,data=data).json()
    # user_information=requests.get(kakao_user_api,headers=header).json()
    user_info=requests.get("https://kapi.kakao.com/v2/user/me",headers={"Authorization":f"Bearer {access_token}"}).json()


    for i in user_info:
        if i=='id':
            user_id=user_info[i]

        elif i=='properties':
            user_nickname=user_info[i]['nickname']

    print()
    print()
    print(f"user_id : {user_id}")
    print(f"user_nickname : {user_nickname}")
    print()
    print()






    # -------------------로그인 및 회원가입----------------
    
    regist_url="https://yellowtaxi.store/dj/registration/"
    login_url="https://yellowtaxi.store/dj/login/"
    regist_data={
        "username":str(user_id),
        "password1":"asdf1234qwer",
        "password2":"asdf1234qwer",
        "nickname":user_nickname
    }

    login_data={
        "username":str(user_id),
        "password":"asdf1234qwer",
        "email":None
    }
    
    #-----------


    flag=check_id(str(user_id))
    print()
    print()
    print(flag)

    if flag:
        # true : 존재함
        print(access_token)





        # 로그인 후 access token 반환 받은 것으로 수정해서 보내주기
        # al_user=CustomUser.objects.get(nickname=user_nickname)
        try:
            ans_login_data=requests.post(login_url,data=login_data,time=1000)
            print()
            print("ans_login_data")
            print(ans_login_data)
            ans_login_data_json=ans_login_data.json()
            print()
            


            return Response(ans_login_data_json,status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    else:
        # false : 존재하지 않음 -> 회원가입 진행
        regist_response=requests.post(regist_url,data=regist_data).json()
        # .json()을 해버리면 본문만 남음.
        if regist_response.status_code==201:
            al_user=CustomUser.objects.get(nickname=user_nickname).json()
            # return_data={
            #     "nickname":al_user.nickname,
            #     "id":al_user.id,
            #     "access_token":access_token
            # }
            return Response(regist_response,status=status.HTTP_201_CREATED)
        elif regist_response.status_code==499:
            return "499error"
        else:
            print('실패')
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        # return Response({f"access_token":{access_token}},status=status.HTTP_200_OK)


#--------------first---------------
# from django.shortcuts import redirect

# # api_view or View
# class kakaoView(api_view):
#     def get(self,request):
#         kakao_api="https://kauth.kakao."










# --------------second---------------
# from allauth.socialaccount.views import SocialLogin
# from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from your_app.serializers import SocialLoginSerializer

# # 추가

# # 소셜 로그인
# BASE_URL = 'http://localhost:8000/api/v1/accounts/rest-auth/'
# KAKAO_CALLBACK_URI = BASE_URL + 'kakao/callback/'
# NAVER_CALLBACK_URI = BASE_URL + 'naver/callback/'
# GOOGLE_CALLBACK_URI = BASE_URL + 'google/callback/'
# GITHUB_CALLBACK_URI = BASE_URL + 'github/callback/'


# class KakaoLogin(SocialLogin):
#     adapter_class = KakaoOAuth2Adapter
#     callback_url = KAKAO_CALLBACK_URI
#     client_class = OAuth2Client
#     serializer_class = SocialLoginSerializer


# class NaverLogin(SocialLogin):
#     adapter_class = NaverOAuth2Adapter
#     callback_url = NAVER_CALLBACK_URI
#     client_class = OAuth2Client
#     serializer_class = SocialLoginSerializer


# class GithubLogin(SocialLogin):
#     adapter_class = GitHubOAuth2Adapter
#     callback_url = GITHUB_CALLBACK_URI
#     client_class = OAuth2Client
#     serializer_class = SocialLoginSerializer


# class GoogleLogin(SocialLogin):
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = GOOGLE_CALLBACK_URI
#     client_class = OAuth2Client
#     serializer_class = SocialLoginSerializer



#-----------third--------------
# from django.views import View
# from django.shortcuts import redirect

# class KakaoView(View):
#     def get(self,request):
#         kakao_api="https://kauth.kakao.com/oauth/authorize?response_type=code"
#         redirect_uri="http://127.0.0.1:8000/kakao/"
#         client_id="6bf5f3d7db0da82bb551b5e113dcc846"
        
#         return redirect(f"{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}")

# class KakaoCallBackView(View):
#     def get(self,request):
#         data={
#             "grant_type"    :"authorization_code",
#             "client_id"     :"6bf5f3d7db0da82bb551b5e113dcc846",
#             "redirection_uri":"http://127.0.0.1:8000/kakao/",
#             "code"          :request.GET["code"]
#         }
#         kakao_token_api="https://kauth.kakao.com/oauth/token"
#         access_token=requests.post(kakao_token_api,data=data).json()['access_token']





















# DB에 JSON 붙여넣기    
@api_view(['POST'])
def data_post(request):
    if request.method=='POST':
        serializer = BoardPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 병원 객체 리스트 보기
@api_view(['GET']) 
def board_list(request):
        if request.method =='GET':
            try:
                boards = Board.objects.all()
                serializer = BoardListSerializer(boards, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Board.DoesNotExist: 
                return Response(status=status.HTTP_404_NOT_FOUND)



# 병원 객체 상세보기
@api_view(['GET'])
def board_detail(request, pk):
    if request.method =='GET':
        try:
            board = Board.objects.get(pk=pk)
            serializer = BoardDetailSerializer(board)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Board.DoesNotExist: 
            return Response(status=status.HTTP_404_NOT_FOUND)  


'''
{

"title":"sdf",
"body":"sdf",
"star":3
}


'''
# 리뷰 작성
@api_view(['POST'])
def comment_post(request,pk):
    if request.method =='POST':
        board = Board.objects.get(pk=pk)
        serializer = CommentRequestSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save(board=board, user=request.user)
            response = CommentResponseSerializer(comment)
            return Response(response.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def comment_list(request, pk):
    if request.method == 'GET':
        board = get_object_or_404(Board, pk=pk)
        comments = Comment.objects.filter(board=board)
        response = CommentResponseSerializer(comments, many=True)
        return Response(response.data, status=status.HTTP_200_OK)







# 마이페이지
# board/mypage/
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def mypage(request,pk):
    if request.method=='GET':
        user=CustomUser.objects.get(nickname=pk)
        # pk값 뭐로 할 지 생각하고 수정하기
        serializer=MypageSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)








# 이름 검색 api
@api_view(['GET'])
def hospital_name(request, name):
     boards = Board.objects.filter(hospital_name__contains = name)
     serializer = BoardDetailSerializer(boards, many=True)
     return Response(serializer.data, status=status.HTTP_200_OK)

# 구 검색 api
@api_view(['GET'])
def hospital_gu(request, gu):
     boards = Board.objects.filter(gu__contains = gu)
     serializer = BoardDetailSerializer(boards, many=True)
     return Response(serializer.data, status=status.HTTP_200_OK)



# 리뷰 개별 페이지
# CommentRequestSerializer
@api_view(['GET'])
def review_get(request,pk):
    if request.method=='GET':
        reviews=Comment.objects.get(pk=pk)
        serializer=CommentResponseSerializer(reviews)
        return Response(serializer.data,status=status.HTTP_200_OK)


    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def review_put_delete(request,board_pk,comment_pk):
    try:
        board=Board.objects.get(pk=board_pk)
        if request.method=='GET':
            comment=Comment.objects.get(pk=comment_pk)
            serializer=CommentResponseSerializer(comment)
            return Response(serializer.data,status=status.HTTP_200_OK)

        if request.method=='PUT':
            try:
                comment=Comment.objects.get(pk=comment_pk)
                serializer=CommentRequestSerializer(comment,data=request.data)
                if serializer.is_valid():
                    commentsave=serializer.save(board=board)
                    response=CommentResponseSerializer(commentsave)
                    return Response(response.data,status=status.HTTP_200_OK)
                
            except Comment.DoesNotExist:
                return Response(request.data,status=status.HTTP_404_NOT_FOUND)

        elif request.method=='DELETE':
            try:
                comment=Comment.objects.get(pk=comment_pk)
                comment.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Comment.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)    
            
    except Board.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)














'''
{"병원명":"김은주산부인과의원",
"주소":"서울 구로구 신도림동",
"구":"구로구",
"예약가능여부":null,
"진료시작시각":"10:00에 진료 시작",
"방문자리뷰":"방문자 리뷰 428",
"블로그리뷰":"블로그 리뷰 116",
"산부인과전문의수":"산부인과전문의 1명",
"기타전문의여부":null}
'''






# # file_path = "C:\Users\eunji\OneDrive\바탕 화면\hack\merged_df_UTF.json"

# file_path='C:/Users/user/Desktop/hackerthon05/hospital_list_withGU.json'
# 이 아래로 다 주석 처리

# file_path='C:/Users/user/Desktop/hackerthontest/hospital_list_withGU.json'

# with open(file_path, 'r', encoding='utf-8') as file:
#     datas = json.load(file)



# # board/post/
# @api_view(['POST'])
# def board_post(request):
#     if request.method=='POST':
#         for data in datas:
#             tempdata={}
#             for i in data:
#                 if i=='병원명':
#                     tempdata['hospital_name']=data[i]
#                 elif i=='주소':
#                     tempdata['address']=data[i]

#                 elif i=='구':
#                     tempdata['gu']=data[i]
#                     # print(data[i])

#                 elif i=='예약가능여부':
#                     tempdata['reservation']=data[i]
#                 elif i=='방문자리뷰':
#                     tempdata['visitcnt']=data[i].split()[2]
#                     if ',' in tempdata['visitcnt']:
#                         tempdata['visitcnt']=tempdata['visitcnt'].replace(',',"")
#                 elif i=='블로그리뷰':
#                     try:
#                         tempdata['blogcnt']=data[i].split()[2]
#                         if ',' in tempdata['blogcnt']:
#                             tempdata['blogcnt']=tempdata['blogcnt'].replace(',',"")
#                             # 1000번대가 존재하는지 확인
#                     except:
#                         tempdata['blogcnt']=None
#                 elif i=='산부인과전문의수':
#                     try:
#                         tempdata['maindoctorcnt']=data[i].split()[1].replace('명','')
#                     except:
#                         tempdata['maindoctorcnt']=None
#             # print(tempdata)
            
#             serializer=BoardPostSerializer(data=tempdata)
#             if serializer.is_valid():
#                 save=serializer.save()
#                 # response=BoardPostSerializer(save)
#                 # return Response(response.data,status=status.HTTP_201_CREATED)

                



#         boards=Board.objects.all()
#         serializers=BoardPostSerializer(boards,many=True)




#         return Response(serializers.data,status=status.HTTP_201_CREATED)
                


# 여기까지 주석



#   오류 생겨서 주석처리 해놨습니다.
# from .serializers import SaveHospitalToDBSerializer

# class SaveDBAPI(APIView):
#     def post(self, request):
#         file_path = 'C:\\Users\\eunji\\OneDrive\\바탕 화면\\hack\\merged_df_UTF.json'


#         with open(file_path, 'r') as file:
#             hospitals_data = []
#             for line in file:
#                 hospital = json.loads(line.strip())
#                 serializer = SaveHospitalToDBSerializer(data=hospital)
#                 if serializer.is_valid():
#                     serializer.save()
#                     hospitals_data.append(serializer.data)
#                 else:
#                     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             return Response(hospitals_data, status=status.HTTP_201_CREATED)





# class HospitalAPIView(APIView):
#     def post(self, request):
#         serializer = HospitalSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)