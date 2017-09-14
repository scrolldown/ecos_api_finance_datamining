# ecos_api_finance_datamining

**This program is finance datamining program using Bank of Korea's ecos api.
First, Write statistic code of ECOS API in the 'ecos 데이터 변수.xlsx'
Second, In the 'ecos_prog.py', Write Extract_csv function's parameter,Start date and End date,like YYYY-MM-DD.
And, Run.
(Optionally, You can use os library to delete files that are created during runtime.)
**
# 전체적인 실행 개념
1. 프로그램은 Extract_csv 함수만 사용합니다.
    그외 함수들은 모두 Extract_csv 안에서 사용하는 함수들입니다.
2. 추출될 csv의 데이터의 시작날짜와 끝날짜는 Extract_csv 함수의 파라미터로 제어하며,  시작날짜는 fromdate, 끝날짜는 todate 입니다.
fromdate와 todate가 YYYY-MM-DD 형식인지 검사를 우선 진행합니다.
그다음 ecos_log 파일 작성을 위해 프로그램은 with ~ logfp 안에서 돌아갑니다.
대략적인 프로그램의 순서입니다.
1. ecos_var_desc 를 불러와 df_varDesc 이라는 dataframe 변수에 집어넣는다.
2. Create_csv_Form 함수를 사용하여 ecos_result.csv의 폼을 만들고, 만들어진 폼을 df_Result 이라는 dataframe 변수에 read_csv 함수를 사용하여 집어 넣는다.  이때, low_memory=False를 하지 않으면 데이터 양이 많을 경우에 데이터가 손실되어나오기 때문에 *꼭* 집어넣는다.
3. FileManger의 CODE 컬럼을 리스트화 시킨 statCodelists 변수의 element 들을 순서대로 반복문을 이용하여 불러오는 방식을 사용하여 ecos_result.csv의 컬럼을 하나씩 채워나간다.
4. Load_period 함수를 사용하여 현재 통계코드의 UPDATE_CYCLE 을 알아낸다.
UPDATE_CYCLE의 종류는 YY,QQ,MM,DD가 있다.
5. statCode,itemCoe,restItemCode를 초기화시킵니다.
6. Find_url 함수를 사용하여 uuu에 프로그램에서 사용할 url을 찾습니다.
7. Find_nowdate 함수를 사용하여 todate를 현재 코드의 UPDATE_CYCLE에 맞게 변환시킵니다. 예) 20160811 을 MM에 맞춰 변환하면 201608 이 됩니다.
8. uuu의 주소에 있는 내용을 (코드).txt에 저장한 후, 
etree로 이름지은(as) xml.etree.ElementTree 라이브러리를 사용하여 
(코드).txt의 내용을 파싱 후 가장 윗계층(root)를 찾아 root 변수에 저장합니다.
9. findall 함수를 사용하여 모든 TIME과 DATA_VALUE 값을 zip함수로 묶은 뒤 반복문을 사용하여 (filename).txt 에 저장합니다.
10. df_Result에 각 itemCount 를 이름으로 하는 새로운 컬럼을 추가한 뒤, 에러체킹을 한다.
11. df_varDesc 에 변수이름, code, UPDATE_CYCLE, 에러코드, 업데이트된 날짜를 추가합니다.
12. Count, STAT_CODE, ITEM_CODE, STAT_NAME, ITEM_NAME1, ITEM_NAME2, ITEM_NAME3, UNIT_NAME, UPDATE_CYCLE 을 root에서 찾아내어 writerow를 이용, (statCode_itemCode[1]).csv 에 작성한다.
13. csv_in은 (filename).txt의 내용을 읽어들여 반복문을 사용하여 모든 (TIME,DATA_VALUE)를 writerow를 이용, (statCode_itemCode[1]).csv 에 작성한다.
14.  (statCode_itemCode[1]).csv의 내용을 df_Current 라는 dataframe 변수에 저장한다.
15. 이중반복문을 이용, df_Result 의 날짜부분과 df_Current의 날짜부분이 일치하면, df_Current의 DATA_VALUE 값을 df_Result 의 DATA_VALUE에 넣는다.
16. deletFileList 에 삭제할 파일들의 이름을 추가한다.
17. 4~14의 내용은 3에서도 말했듯이 반복문입니다. statCoelists가 끝날때까지 반복됩니다.
18. df_varDesc은 ecos_var_desc.csv로 추출합니다.
19. df_Result 이라는 dataframe은 sort_values를 이용하여 내림차순 정렬하여 가장 최신의 날짜가 가장 위로 올라오게 합니다.
20. 정렬된 데이터는 ecos_result.csv 로 추출합니다.
21. 끝입니다.
