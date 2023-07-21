Git을 이용한 버전 관리
# Github를 이용한 포트폴리오 + 협업용
# 파일 이름에 파일 작성 시간 적기(버전관리에 도움)
# 원격 저장소 중간 프로세스를 정확히 숙지(암기)!!
# 

# ex) ~~~~~_변경사항_230713_1540.docx
# ex) ~~~~~_변경사항_230713_1541.docx.
# ex) ~~~~~_변경사항_230713_1542.docx
# ex) ~~~~~_230713_1540.docx
# 변경사항만 체크 하고 최종본만 저장
# 
# 변경사항을 통해 이전 버전으로 복구 가능(Git을 통해서)
# 
# Git -------> 분산 버전 관리 프로그램
# 
# Github(블로그?) (이동욱개발자)
# 

# git init (파일들을 git로 관리 선언)
# [working area(directory) / staging area(directory) / git directory] ->       local area(github 원격)(Remote)

—————————————————————————————————————————--

            a.txt         ----------->    a.txt   --------------->   a.txt   -------------------------->
                             git add                 git commit                       git push
           git 관리 x                   git 관리 시작
gi
                         <-----------     a.txt

                             a.txt를 수정해서 working area 로 이동

        a.txt (수정후)                  a.txt(수정전)
       (modified file)

                          ---------->     a.txt (수정 된 a.txt를 add해줘야 최신화가 된다)

#  새로운 파일 - c.txt(new)                 ===> untracted file (git가 관리 x)
#  a_1.txt(수정된 파일) ===> modified file      

——————————————————————————————————————————-

 - tracted file - Git의 관리대상에 있는 file, add과정을 한번이라도 거칠경우 tracted file
 - working directory - 내가 작업을 시작하는 실제 폴더(디렉토리)
 - staging directory - 내가 커밋을 통해 git으로 버전관리를 하고 싶은 파일을 모아놓은 공간
 - git repository - 커밋을 통해 버전관리를 하고 있는 파일을 모아놓은 공간

 -  다시 git add를 통해 스테이징 디렉토리로 올려줘야 한다

———————————————————————————————————————————-
vs code  

폴더에 터미널 열고 git init입력 --> .git 폴더 생성
 git config --global user.name 이름
 git config --global user.email 이메일
 git config --global -l                 // 등록 확인

 git status                                 //파일 현재 상태 확인
 echo helloworld! > a.txt                   //언트랙티드 파일 생성
 echo > b.txt > c.txt                       //b, c텍스트 파일 생성
 git add a.txt                              //a.txt를 스테이징 디렉토리 올림
 git add *.txt                            //txt확장자 파일을 전부 스테이징 디렉토리로 이동
 git rm --cached *.txt                  //txt확장자 파일을 스테이징 디렉토리에서 제거
 git add .                                  //폴더 내 모든 파일을 스테이징 디렉토리로 이동

 git ignore(반드시 working에 있을때 걸러야함)    // 원격저장소에 올리지 않을 파일
git commit -m "파일명"               // commit으로 git directory로 옮기기
git push                                   // 원격 저장소로 파일 올리기
git push -u origin +master            // 원격 오류 없이 올리기

파일 가져오기
git pull                                      // 연결(내 컴퓨터와 원격 파일이 동기화 되었을때) 파일만 가져올수 있음
git clone                                    // 처음 불러올때 ( 파일 가져옴과 동시에 내 컴퓨터와 원격 파일을 동기화)
git log	  		           // git directory 에 파일 

cd ./TIL2                                      // 가져온 파일 장소 지정


git clone URL
git. init
git add .
git commit -m

git remote add URL

  파이썬 도장깨기


ssafy git - dntjr5741@naver.com / dntjr008*12
git lab - dntjr5741@naver.com / dntjr008*12
git hub - dntjr5741@naver.com / dntjr008**12
edu.ssafy - dntjr5741@naver.com / dntjr008**12
mm  - dntjr5741@naver.com / Sdntjr5741@naver.com10
chat gpt - dntjr5741@naver.com / tladn123
백준 dntjr5741  / dntjr008
