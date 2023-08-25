from django.shortcuts import render,redirect
from django.contrib import messages
from .models import lessonplanBatch,courseoutcomes,textbooks,referencebooks,targetproficiency,lectureplan,co_pso_Matrix,course_end_survey,details_of_instructors,teachers
from django.contrib.auth.decorators import login_required
from .models import CustomUser

# Create your views here.
def login(request):
     if request.method == "POST":
          name=request.POST['name']
          passwd=request.POST['passwd']
          if teachers.objects.filter(name=name).exists():
               obj=teachers.objects.get(name=name)
               if(obj.passwd==passwd):
                    return redirect('mainpage')
               else:
                    messages.error(request,'invalid passwod please try again')
                    return redirect('login')
          else:
               messages.error(request,'invalid username please try again')
     return render(request,'obeapp/obapp/login.html')
@login_required(login_url='/user_login')
def mainpage(request):
     #usname=teachers.objects.get(name=name)
     #return render(request,'obeapp/obapp/mainpage.html',{'usname':usname})
     if request.session.get('user_id', None):
          return render(request,'obeapp/obapp/mainpage.html')
     else:
         return redirect('course_view')
# def mainpageview(request):
#     return render(request,'obeapp/obapp/mainpageview.html')
@login_required(login_url='/user_login')
def inputform(request):
    if request.session.get('user_id', None):
        return render(request,'obeapp/obapp/inputform.html')
    else:
        return redirect('course_view')
        
def storeinput(request):
    if request.method == "POST":
        coursecode=request.POST['coursecode']
        if lessonplanBatch.objects.filter(course_code=coursecode).exists():
                messages.info(request,'course code Already Used')
                return redirect('inputform')
        else:
             #lessonplanBatch table 1
             fl=0
             batch=request.POST['batch']
             academicyear=request.POST['academicyear']
             programme=request.POST['programme']
             semester=request.POST['semester']
             section=request.POST['section']
             nameofthecourse=request.POST['nameofthecourse']
             batch_lp=lessonplanBatch.objects.create(batch=batch,academicyear=academicyear,programme=programme,semester=semester,section=section,name_of_the_course=nameofthecourse,course_code=coursecode)
             batch_lp.save();
             numco=int(request.POST['numco'])
             

             #***************** course outcomes **************
             for i in range(1,numco+1):
                  co=str(i)
                  course_outcome="-"
                  knowledge_level="-"
                  #courseoutcome=request.POST["coo"+str(i)]
                  if(request.POST["coo"+str(i)]):
                       course_outcome=request.POST["coo"+str(i)]
               
                  if(request.POST["kl"+str(i)]):
                       knowledge_level=request.POST["kl"+str(i)]
                 
                  #knowledge_level=request.POST["kl"+str(i)]
                  
                 
                  co_lp=courseoutcomes.objects.create(co=co,courseoutcome=course_outcome,knowledge_level=knowledge_level,course_code=coursecode)
                  co_lp.save();
             #textbooks table 3
             count_tb1=request.POST['copytexbook']
             count_tb2=int(count_tb1)
             list_textbook=['tb1','tb2','tb3','tb4','tb5','tb6','tb7','tb8','tb9','tb10','tb11','tb12','tb13','tb14','tb15','tb16','tb17','tb18','tb19','tb20','tb21','tb22','tb23','tb24','tb25','tb26','tb27','tb28','tb29','tb30']
             for i in range(count_tb2):
                  textbook="-"
                  ele=list_textbook[i]
                  
                  if(request.POST[ele]):
                      textbook=request.POST[ele] 
                  
                  tb_lp=textbooks.objects.create(sno=i+1,textbook_details=textbook,course_code=coursecode)              
                  tb_lp.save();
             #referencebooks table 4
             count_rb1=request.POST['copyreferencebook']
             count_rb2=int(count_rb1)
             list_referencebook=['rb1','rb2','rb3','rb4','rb5','rb6','rb7','rb8','rb9','rb10','rb11','rb12','rb13','rb14','rb15','rb16','rb17','rb18','rb19','rb20','rb21','rb22','rb23','rb24','rb25','rb26','rb27','rb28','rb29','rb30']
             for i in range(count_rb2):
                  ele=list_referencebook[i]
                  referencebook="-"
                  if(request.POST[ele]):
                    referencebook=request.POST[ele]
                  rb_lp=referencebooks.objects.create(sno=i+1,rfbook_details=referencebook,course_code=coursecode)              
                  rb_lp.save();
        
            #*********** target proficiency table****************
             for i in range(numco):
                  co="CO"+str(i+1)
                  tpl="-"
                  l3="-"
                  l2="-"
                  l1="-"
                  if(request.POST['co'+str(i+1)+'l']):    
                    tpl=request.POST['co'+str(i+1)+'l']
                  if(request.POST['co'+str(i+1)+'l3']):
                    l3=request.POST['co'+str(i+1)+'l3']
                  if(request.POST['co'+str(i+1)+'l2']):
                    l2=request.POST['co'+str(i+1)+'l2']
                  if(request.POST['co'+str(i+1)+'l1']):
                    l1=request.POST['co'+str(i+1)+'l1']
                  tptb=targetproficiency.objects.create(co=co,tpl=tpl,l3=l3,l2=l2,l1=l1,course_code=coursecode)
                  tptb.save();
    #tpl=models.CharField(max_length=50,default="Target Proficiency Level")
    #course_code=models.CharField(max_length=15)            

            #***********lecture plan **************
             for i in range(numco):
                  temp=int(request.POST["tempinp"+str(i+1)])
                  for j in range(1,temp+1):
                       sno=str(j)
                       ilo="-"
                       knowledgelevel="-"
                       noof_hours="-"
                       pedagogy="-"
                       teachingaids="-"
                       course_outcome="CO"+str(i+1)
                       if(request.POST["co"+str(i)+"ilo"+str(j)]):
                         ilo=request.POST["co"+str(i)+"ilo"+str(j)]
                       if(request.POST["co"+str(i)+"knilo"+str(j)]):
                         knowledgelevel=request.POST["co"+str(i)+"knilo"+str(j)]
                       if(request.POST["co"+str(i)+"nfhr"+str(j)]):
                         noof_hours=request.POST["co"+str(i)+"nfhr"+str(j)]
                       if(request.POST["co"+str(i)+"pedgy"+str(j)]):
                         pedagogy=request.POST["co"+str(i)+"pedgy"+str(j)]
                       if(request.POST["co"+str(i)+"tds"+str(j)]):
                         teachingaids=request.POST["co"+str(i)+"tds"+str(j)]
                       #course_code="v20123"
                       co1_lp=lectureplan.objects.create(sno=sno,course_outcome=course_outcome,ilo=ilo,knowledgelevel=knowledgelevel,noof_hours=noof_hours,pedagogy=pedagogy,teachingaids=teachingaids,course_code=coursecode)
                       co1_lp.save();
             #******* co&pso matrix***************
             for k in range(numco+1):
                temp="co"+str(k+1)
                co="CO"+str(k+1)
                if(k==numco):
                    temp="Course"
                    co="Course"
                po1="-"
                po2="-"
                po3="-"
                po4="-"
                po5="-"
                po6="-"
                po7="-"
                po8="-"
                po9="-"
                po10="-"
                po11="-"
                po12="-"
                pso1="-"
                pso2="-"
                if(request.POST[temp+"po1"]):
                    po1=request.POST[temp+"po1"]
                if(request.POST[temp+"po2"]):
                    po2=request.POST[temp+"po2"]
                if(request.POST[temp+"po3"]):
                    po3=request.POST[temp+"po3"]
                if(request.POST[temp+"po4"]):
                    po4=request.POST[temp+"po4"]
                if(request.POST[temp+"po5"]):
                    po5=request.POST[temp+"po5"]
                if(request.POST[temp+"po6"]):
                    po6=request.POST[temp+"po6"]
                if(request.POST[temp+"po7"]):
                    po7=request.POST[temp+"po7"]
                if(request.POST[temp+"po8"]):
                    po8=request.POST[temp+"po8"]
                if(request.POST[temp+"po9"]):
                    po9=request.POST[temp+"po9"]
                if(request.POST[temp+"po10"]):
                    po10=request.POST[temp+"po10"]
                if(request.POST[temp+"po11"]):
                    po11=request.POST[temp+"po11"]
                if(request.POST[temp+"po12"]):
                    po12=request.POST[temp+"po12"]
                if(request.POST[temp+"pso1"]):
                    pso1=request.POST[temp+"pso1"]
                if(request.POST[temp+"pso2"]):
                    pso2=request.POST[temp+"pso2"]
                
                co_pso=co_pso_Matrix.objects.create(cos=co,po1=po1,po2=po2,po3=po3,po4=po4,po5=po5,po6=po6,po7=po7,po8=po8,po9=po9,po10=po10,po11=po11,po12=po12,pso1=pso1,pso2=pso2,course_code=coursecode)
                co_pso.save();
             #*************course end survey questionery**************
             for i in range(numco):
                   qs="-"
                   if(request.POST["qs"+str(i+1)]):
                         qs=request.POST["qs"+str(i+1)]
                   qs_co="CO"+str(i+1)
                   lp_qs=course_end_survey.objects.create(sno=str(i+1),cos=qs_co,question=qs,course_code=coursecode)
                   lp_qs.save();
             name,designation,year,section,contactno,email = "-","-","-","-","-","-"
             name=request.POST['insname']
             designation=request.POST['insdes']
             year=request.POST['insyear']
             section=request.POST['inssec']
             contactno=request.POST['inscno']
             email=request.POST['insemail']
             lp_ins=details_of_instructors.objects.create(sno='1',name=name,designation=designation,year=year,section=section,contactno=contactno,email=email,course_code=coursecode)
             lp_ins.save();
        #return redirect('mainpage') 
        return render(request,'obeapp/obapp/mainpage.html')
                
    return render(request,"obeapp/obapp/storeinput.html")
'''def viewresult(request):
    if request.method=="POST":
        numco=request.POST['numco']
        messages.info(request,numco)
    return render(request,"viewresult.html")'''
def viewplan(request):
        coursecode=request.POST['coursecode']
        t=lessonplanBatch.objects.filter(course_code=coursecode).first()
        if(t==None):
           messages.info(request,'course code does not exist')
           try:
               if CustomUser.objects.get(Biometricid=str(request.session.get('user_id', None))):
                    return redirect('inputcoursecode')
           except:
               return redirect('course_view')
        if(t.section=='CSE(AI)'):
             branch='Computer Science & Engineering(Artificial Intelligence)'
        elif(t.section=='CSE'):
             branch='Computer Science & Engineering'
        elif(t.section=='CST'):
             branch='Computer Science & Technology'
        elif(t.section=='EEE'):
             branch='Electrical & Electronic engineering'
        elif(t.section=='ECE'):
             branch='Electronics & Communication Engineering'
        elif(t.section=='CIVIL'):
             branch='Civil Engineering'
        elif(t.section=='ME'):
             branch='Mechanical Engineering'
        else:
             branch=t.programme
        bat=lessonplanBatch.objects.get(course_code=coursecode)
        result_co=courseoutcomes.objects.filter(course_code=coursecode)
        textbook=textbooks.objects.filter(course_code=coursecode)
        l=len(result_co)
        lst=[]
        for i in range(1,l+1):
          
             course_outcome="CO"+str(i)
             lp_co=lectureplan.objects.filter(course_code=coursecode,course_outcome=course_outcome)
             #print("***************************")
             print(lp_co)
             lst.append(lp_co)    
        rfbook=referencebooks.objects.filter(course_code=coursecode)
        tp=targetproficiency.objects.filter(course_code=coursecode)
        copsomat=co_pso_Matrix.objects.filter(course_code=coursecode)
        question=course_end_survey.objects.filter(course_code=coursecode)
        instructor=details_of_instructors.objects.filter(course_code=coursecode)
        d={'branch':branch,'bat':bat,'result_co':result_co,'textbook':textbook,'rfbook':rfbook,'tp':tp,'lst':lst,'copsomat':copsomat,'question':question,'instructor':instructor,'l':l}
        return render(request,'obeapp/obapp/viewplan.html',d)

@login_required(login_url='/user_login')
def inputcoursecode(request):
     # print(request.session.get('user_id', None))
     if request.session.get('user_id', None):
          obj = CustomUser.objects.get(Biometricid=str(request.session.get('user_id', None)))
          codes = obj.Permissions.split(",")
          return render(request,'obeapp/obapp/inputcoursecode.html',{'codes':codes})
     return redirect('faculty_dashboard')
@login_required(login_url='/user_login')
def updatecoursecode(request):
     if request.session.get('user_id', None):
          return render(request,'obeapp/obapp/updatecoursecode.html')
     else:
         return redirect('course_view')
@login_required(login_url='/user_login')
def updateplan(request):
        coursecode=request.POST['coursecode']
        t=lessonplanBatch.objects.filter(course_code=coursecode).first()
        if(t==None):
           messages.info(request,'course code does not exist')
           return redirect('inputcoursecode')
        if(t.section=='CSE(AI)'):
             branch='Computer Science & Engineering(Artificial Intelligence)'
        elif(t.section=='CSE'):
             branch='Computer Science & Engineering'
        elif(t.section=='CST'):
             branch='Computer Science & Technology'
        elif(t.section=='EEE'):
             branch='Electrical & Electronic engineering'
        elif(t.section=='ECE'):
             branch='Electronics & Communication Engineering'
        elif(t.section=='CIVIL'):
             branch='Civil Engineering'
        elif(t.section=='ME'):
             branch='Mechanical Engineering'
        else:
             branch=t.programme
        bat=lessonplanBatch.objects.get(course_code=coursecode)
        result_co=courseoutcomes.objects.filter(course_code=coursecode)
        result_coNm=[[str(i+1),'coo'+str(i),'kl'+str(i)] for i in range(len(result_co))]
        result_coF=zip(result_co,result_coNm)
        textbook=textbooks.objects.filter(course_code=coursecode)
        textbook_len=len(textbook)
        textbookNm=['tb'+str(i) for i in range(textbook_len)]
        textbookF=zip(textbook,textbookNm)
        l=len(result_co)
        lst=[]
        len_lst=[]
        for i in range(1,l+1):
                       
             course_outcome="CO"+str(i)
             lp_co=lectureplan.objects.filter(course_code=coursecode,course_outcome=course_outcome)
             len_lst.append(len(lp_co))
            # lp_coNm=[[str(i+1),"CO"+str(i+1),"co"+str(i)+"ilo"+str(j),"co"+str(i)+"knilo"+str(j),"co"+str(i)+"nfhr"+str(j),"co"+str(i)+"pedgy"+str(j),"co"+str(i)+"tds"+str(j)] for j in range(len(lp_co))]
             lp_coNm=[[str(j+1),"CO"+str(i+1),"co"+str(i-1)+"ilo"+str(j),"co"+str(i-1)+"knilo"+str(j),"co"+str(i-1)+"nfhr"+str(j),"co"+str(i-1)+"pedgy"+str(j),"co"+str(i-1)+"tds"+str(j)] for j in range(len(lp_co))]
             lp_coF=zip(lp_co,lp_coNm)
             print("***************************")
             #print(lp_co)
             lst.append(lp_coF) 
        lst_len=len(lst)
        lstF=zip(lst,[i for i in range(lst_len)])   
        rfbook=referencebooks.objects.filter(course_code=coursecode)
        rfbook_len=len(rfbook)
        rfbookNm=['rb'+str(i) for i in range(rfbook_len)]
        rfbookF=zip(rfbook,rfbookNm)
        tp=targetproficiency.objects.filter(course_code=coursecode)
        tpNm=[['co'+str(i),'co'+str(i+1)+'l','co'+str(i+1)+'l3','co'+str(i+1)+'l2','co'+str(i+1)+'l1'] for i in range(len(tp))]
        tpF=zip(tp,tpNm)
        copsomat=co_pso_Matrix.objects.filter(course_code=coursecode)
        temp="co"
        copsomatNm=[]
        for i in range(len(copsomat)-1):
             t=[]
             t.append("CO"+str(i+1))
             for k in range(1,13):
                  t.append("co"+str(i+1)+"po"+str(k))
             t.append("co"+str(i+1)+"pso1")
             t.append("co"+str(i+1)+"pso2")
             copsomatNm.append(t)
        m=[]
        m.append("Course")
        for i in range(1,13):
             m.append("Coursepo"+str(i))
        m.append("Coursepso1")
        m.append("Coursepso2")
        copsomatNm.append(m)
        copsomatF=zip(copsomat,copsomatNm)
        question=course_end_survey.objects.filter(course_code=coursecode)
        questionNm=[[str(i+1),"co"+str(i),'qs'+str(i)] for i in range(len(question))]
        questionF=zip(question,questionNm)
        instructor=details_of_instructors.objects.filter(course_code=coursecode)
        numco1=len(result_co)
        d={'branch':branch,'numco':numco1,'result_coF':result_coF,'bat':bat,'result_co':result_co,'textbookF':textbookF,'textbook_len':textbook_len,'rfbookF':rfbookF,"rfbook_len":rfbook_len,'tpF':tpF,'lstF':lstF,"lst_len":lst_len,"len_lst":len_lst,'copsomatF':copsomatF,'questionF':questionF,'instructor':instructor,'l':l}
        return render(request,'obeapp/obapp/updateform.html',d)
def updateinput(request):
    if request.method == "POST":
        coursecode=request.POST['coursecode']
        if lessonplanBatch.objects.filter(course_code=coursecode).exists():
                #messages.info(request,'course code Already Used')
                #return redirect('inputform')
               #else:
             #deleting codeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee**********************
             #lessonplanBatch table 1
             dt=lessonplanBatch.objects.filter(course_code=coursecode).first()
             #dt.delete()
             dbat=lessonplanBatch.objects.get(course_code=coursecode)
             dbat.delete()
             dresult_co=courseoutcomes.objects.filter(course_code=coursecode)
             dresult_co.delete()
             dtextbook=textbooks.objects.filter(course_code=coursecode)
             dtextbook.delete()
             dlp_co=lectureplan.objects.filter(course_code=coursecode)
             dlp_co.delete()
             drfbook=referencebooks.objects.filter(course_code=coursecode)
             drfbook.delete()
             dtp=targetproficiency.objects.filter(course_code=coursecode)
             dtp.delete()
             dcopsomat=co_pso_Matrix.objects.filter(course_code=coursecode)
             dcopsomat.delete()
             dquestion=course_end_survey.objects.filter(course_code=coursecode)
             dquestion.delete()
             dinstructor=details_of_instructors.objects.filter(course_code=coursecode)
             dinstructor.delete()
             fl=0
             batch=request.POST['batch']
             academicyear=request.POST['academicyear']
             programme=request.POST['programme']
             semester=request.POST['semester']
             section=request.POST['section']
             nameofthecourse=request.POST['nameofthecourse']
             batch_lp=lessonplanBatch.objects.create(batch=batch,academicyear=academicyear,programme=programme,semester=semester,section=section,name_of_the_course=nameofthecourse,course_code=coursecode)
             batch_lp.save();
             numco=int(request.POST['numco'])
             

             #***************** course outcomes **************
             for i in range(0,numco):
                  co=str(i+1)
                  course_outcome="-"
                  knowledge_level="-"
                  #courseoutcome=request.POST["coo"+str(i)]
                  if(request.POST["coo"+str(i)]):
                       courseoutcome=request.POST["coo"+str(i)]
               
                  if(request.POST["kl"+str(i)]):
                       knowledge_level=request.POST["kl"+str(i)]
                  #courseoutcome=request.POST["coo"+str(i)]
                  #knowledge_level=request.POST["kl"+str(i)]
                  co_lp=courseoutcomes.objects.create(co=co,courseoutcome=courseoutcome,knowledge_level=knowledge_level,course_code=coursecode)
                  co_lp.save();
             #textbooks table 3
             count_tb1=request.POST['copytexbook']
             count_tb2=int(count_tb1)
             #list_textbook=['tb1','tb2','tb3','tb4','tb5','tb6','tb7','tb8','tb9','tb10','tb11','tb12','tb13','tb14','tb15','tb16','tb17','tb18','tb19','tb20','tb21','tb22','tb23','tb24','tb25','tb26','tb27','tb28','tb29','tb30']
             for i in range(count_tb2):
                  #ele=list_textbook[i]
                  #textbook=request.POST["tb"+str(i)]
                  textbook="-"
                  #ele=list_textbook[i]
                  
                  if(request.POST["tb"+str(i)]):
                      textbook=request.POST["tb"+str(i)]
                  tb_lp=textbooks.objects.create(sno=i+1,textbook_details=textbook,course_code=coursecode)              
                  tb_lp.save();
             #referencebooks table 4
             count_rb1=request.POST['copyreferencebook']
             count_rb2=int(count_rb1)
             #list_referencebook=['rb1','rb2','rb3','rb4','rb5','rb6','rb7','rb8','rb9','rb10','rb11','rb12','rb13','rb14','rb15','rb16','rb17','rb18','rb19','rb20','rb21','rb22','rb23','rb24','rb25','rb26','rb27','rb28','rb29','rb30']
             for i in range(count_rb2):
                  #ele=list_referencebook[i]
                  referencebook="-"
                  if(request.POST["rb"+str(i)]):
                    referencebook=request.POST["rb"+str(i)]
                  #referencebook=request.POST["rb"+str(i)]
                  rb_lp=referencebooks.objects.create(sno=i+1,rfbook_details=referencebook,course_code=coursecode)              
                  rb_lp.save();
        
            #*********** target proficiency table****************
             for i in range(numco):
                  co="CO"+str(i+1)
                  tpl="-"
                  l3="-"
                  l2="-"
                  l1="-"
                  if(request.POST['co'+str(i+1)+'l']):    
                    tpl=request.POST['co'+str(i+1)+'l']
                  if(request.POST['co'+str(i+1)+'l3']):
                    l3=request.POST['co'+str(i+1)+'l3']
                  if(request.POST['co'+str(i+1)+'l2']):
                    l2=request.POST['co'+str(i+1)+'l2']
                  if(request.POST['co'+str(i+1)+'l1']):
                    l1=request.POST['co'+str(i+1)+'l1']
               #    tpl=request.POST['co'+str(i+1)+'l']
               #    l3=request.POST['co'+str(i+1)+'l3']
               #    l2=request.POST['co'+str(i+1)+'l2']
               #    l1=request.POST['co'+str(i+1)+'l1']
                  tptb=targetproficiency.objects.create(co=co,tpl=tpl,l3=l3,l2=l2,l1=l1,course_code=coursecode)
                  tptb.save();
    #tpl=models.CharField(max_length=50,default="Target Proficiency Level")
    #course_code=models.CharField(max_length=15)            

            #***********lecture plan **************
             for i in range(numco):
                  temp=int(request.POST["tempinp"+str(i)])
                  #print(temp,"********************************")
                  for j in range(0,temp):
                       sno=str(j)

                       ilo="-"
                       knowledgelevel="-"
                       noof_hours="-"
                       pedagogy="-"
                       teachingaids="-"
                       course_outcome="CO"+str(i+1)
                       if(request.POST["co"+str(i)+"ilo"+str(j)]):
                         ilo=request.POST["co"+str(i)+"ilo"+str(j)]
                       if(request.POST["co"+str(i)+"knilo"+str(j)]):
                         knowledgelevel=request.POST["co"+str(i)+"knilo"+str(j)]
                       if(request.POST["co"+str(i)+"nfhr"+str(j)]):
                         noof_hours=request.POST["co"+str(i)+"nfhr"+str(j)]
                       if(request.POST["co"+str(i)+"pedgy"+str(j)]):
                         pedagogy=request.POST["co"+str(i)+"pedgy"+str(j)]
                       if(request.POST["co"+str(i)+"tds"+str(j)]):
                         teachingaids=request.POST["co"+str(i)+"tds"+str(j)]
                       #course_outcome="CO"+str(i+1)
                    #    print("co"+str(i)+"ilo"+str(j))
                    #    ilo=request.POST["co"+str(i)+"ilo"+str(j)]
                    #    knowledgelevel=request.POST["co"+str(i)+"knilo"+str(j)]
                    #    noof_hours=request.POST["co"+str(i)+"nfhr"+str(j)]
                    #    pedagogy=request.POST["co"+str(i)+"pedgy"+str(j)]
                    #    teachingaids=request.POST["co"+str(i)+"tds"+str(j)]
                       #course_code="v20123"
                       co1_lp=lectureplan.objects.create(sno=sno,course_outcome=course_outcome,ilo=ilo,knowledgelevel=knowledgelevel,noof_hours=noof_hours,pedagogy=pedagogy,teachingaids=teachingaids,course_code=coursecode)
                       co1_lp.save();
             #******* co&pso matrix***************
             for k in range(numco+1):
                temp="co"+str(k+1)
                co="CO"+str(k+1)
                if(k==numco):
                    temp="Course"
                    co="Course"
               #  po1=request.POST[temp+"po1"]
               #  po2=request.POST[temp+"po2"]
               #  po3=request.POST[temp+"po3"]
               #  po4=request.POST[temp+"po4"]
               #  po5=request.POST[temp+"po5"]
               #  po6=request.POST[temp+"po6"]
               #  po7=request.POST[temp+"po7"]
               #  po8=request.POST[temp+"po8"]
               #  po9=request.POST[temp+"po9"]
               #  po10=request.POST[temp+"po10"]
               #  po11=request.POST[temp+"po11"]
               #  po12=request.POST[temp+"po12"]
               #  pso1=request.POST[temp+"pso1"]
               #  pso2=request.POST[temp+"pso2"]
                po1="-"
                po2="-"
                po3="-"
                po4="-"
                po5="-"
                po6="-"
                po7="-"
                po8="-"
                po9="-"
                po10="-"
                po11="-"
                po12="-"
                pso1="-"
                pso2="-"
                if(request.POST[temp+"po1"]):
                    po1=request.POST[temp+"po1"]
                if(request.POST[temp+"po2"]):
                    po2=request.POST[temp+"po2"]
                if(request.POST[temp+"po3"]):
                    po3=request.POST[temp+"po3"]
                if(request.POST[temp+"po4"]):
                    po4=request.POST[temp+"po4"]
                if(request.POST[temp+"po5"]):
                    po5=request.POST[temp+"po5"]
                if(request.POST[temp+"po6"]):
                    po6=request.POST[temp+"po6"]
                if(request.POST[temp+"po7"]):
                    po7=request.POST[temp+"po7"]
                if(request.POST[temp+"po8"]):
                    po8=request.POST[temp+"po8"]
                if(request.POST[temp+"po9"]):
                    po9=request.POST[temp+"po9"]
                if(request.POST[temp+"po10"]):
                    po10=request.POST[temp+"po10"]
                if(request.POST[temp+"po11"]):
                    po11=request.POST[temp+"po11"]
                if(request.POST[temp+"po12"]):
                    po12=request.POST[temp+"po12"]
                if(request.POST[temp+"pso1"]):
                    pso1=request.POST[temp+"pso1"]
                if(request.POST[temp+"pso2"]):
                    pso2=request.POST[temp+"pso2"]
                
                co_pso=co_pso_Matrix.objects.create(cos=co,po1=po1,po2=po2,po3=po3,po4=po4,po5=po5,po6=po6,po7=po7,po8=po8,po9=po9,po10=po10,po11=po11,po12=po12,pso1=pso1,pso2=pso2,course_code=coursecode)
                co_pso.save();
             #*************course end survey questionery**************
             for i in range(numco):
                   qs="-"
                   if(request.POST["qs"+str(i)]):
                         qs=request.POST["qs"+str(i)]
                   #qs=request.POST["qs"+str(i)]
                   qs_co="CO"+str(i+1)
                   lp_qs=course_end_survey.objects.create(sno=str(i+1),cos=qs_co,question=qs,course_code=coursecode)
                   lp_qs.save();
             name,designation,year,section,contactno,email = "-","-","-","-","-","-"
             name=request.POST['insname']
             designation=request.POST['insdes']
             year=request.POST['insyear']
             section=request.POST['inssec']
             contactno=request.POST['inscno']
             email=request.POST['insemail']
             lp_ins=details_of_instructors.objects.create(sno='1',name=name,designation=designation,year=year,section=section,contactno=contactno,email=email,course_code=coursecode)
             lp_ins.save();
        #return redirect('obeapp/obapp/updatecoursecode')           
        return render(request,'obeapp/obapp/mainpage.html')
    return render(request,"obeapp/obapp/storeinput.html")