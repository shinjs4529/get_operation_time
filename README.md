\# get\_robot\_operation\_time

로봇 기기에서 ARMI(RM)가 실행되는 동안 저장되는 앱 동작 로그를 활용해, 로봇 동작시간 집계에 활용

* 로봇이 로아이젠 클라우드(aws-log, ~/Workspaces/RobotManager/apps/roai-back/public/localfs/files/robot-logs/)에 업로드한 .log 파일 다운로드
* 예시로서 넣어둔 로그파일들은 대부분의 내용을 ......으로 생략하였음
* 다운로드한 log 파일들을 logs/ 폴더에 위치시키고 get\_robot\_operation\_time.py 실행
* robotId 별로 요약된 second단위 동작시간에 summary\_output.csv로 일괄 출력



\# parse\_game\_play\_time

기억산책 인지게임 활용 시간 정리에 활용

* https://memorywalk.kr에 로그인하여 \[이용자 관리]-\[이용자] 탭에서 개별 이용자 선택-기간 통계 선택-"기간내 문제 풀이 시간"을 개별 기록
* 그 포맷은 2시간 53분 38초 형식이며, 여러 사용자의 풀이 시간을 기록한 예시가 korean\_time.txt 파일
* 예시와 같이 korean\_time.txt파일을 작성 후 parse\_game\_play\_time.py를 실행 시, second단위로 계산된 게임 실행 시간이 parsed\_time.csv로 일괄 출력



----------------------------------

위 2개 기록의 합산, 혹은 get\_robot\_operation\_time만을 활용하여 총 로봇 활용시간을 구하고,

필요 시 보고서 등에 활용

