import requests
from bs4 import BeautifulSoup as bs
def chal(chal_id:str):
    response=requests.request('GET',url='http://skyoj.tnfsh.tn.edu.tw/sky/index.php/chal/result/'+chal_id)
    dom = bs(response.text,'html.parser')

    s=dom.__str__().find('總得分')
    if s<0: raise RuntimeError('challenge does not exist')
    score=int(dom.__str__()[s+13:s+16].replace(' ','').replace(',',''))

    result=dom.find_all('a')

    meta_problem :str=result[11].__str__()
    meta_user :str=result[12].__str__()

    s=meta_problem.find('>')
    problem_name=meta_problem[s+1:-4].replace('\t','').replace('\n','')
    s=meta_problem.find('view')
    e=meta_problem.find('/">')
    problem_id=meta_problem[s+5:e]

    s=meta_user.find('>')
    user_name=meta_user[s+1:-4].replace('\t','').replace('\n','')
    s=meta_user.find('view')
    e=meta_user.find('">')
    user_id=meta_user[s+5:e]

    return {
        'chal_id':chal_id,
        'user_id':user_id,
        'user_name':user_name,
        'problem_id':problem_id,
        'problem_name':problem_name,
        'score':score,
    }
