from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
import re

# Create your views here.
class Home(generic.TemplateView):
    template_name='base/calculadora.html'

def calculation(request):
    result=0
    msj_no_error=True
    result_error = ''
    if request.method=="POST":
        valores=request.POST['values'] #string having whole ques
        values=valores.replace(',','.')
        values=values.replace('/', '÷')
        values=values.replace('*', 'x')
        print("STEP 1-",values)
        vals=re.findall(r"(\d+)",values) #extrect values
        print("STEP 2- ",re.findall(r"(\d+)",values))
        operators=['.','%','x','÷','+','-']
        opr=[]  
        for v in values:
            for o in operators:
                if v==o:
                    print("STEP 3(SIMBOLO DE OPERADOR)=>", o)
                    opr.append(o)
        print("STEP 4- array operador =>",opr)                      #extrect operators
        #print(re.findall(r"(\d+)",values))

        for o in opr:
            
            if o=='.':
                i=opr.index(o)
                print("STEP 5(POSICION DEL ARRAY OPERADOR) => ", i)
                res=vals[i]+"."+vals[i+1]
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=res
                print("STEP 6 =>", vals)
                print("STEP 7 =>", opr)
                
            elif o=='%':
                i=opr.index(o)
                mod= 0
                dec_por = float(vals[i+1])
                valor_por=float(vals[i])
                mod= dec_por%valor_por
                #res=float(vals[i])+valor_por
                res= float(mod)
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=res
                print(vals)
                print(opr)   
                
            elif o=='÷':
                i=opr.index(o)
                res=0
                try:
                    res=float(vals[i])/float(vals[i+1])
                except ZeroDivisionError:
                    msj_no_error=False
                    result_error = result_error + "ERROR_VALOR_INDEFINIDO"
                except Exception as e:
                    print(type(e))
                finally: 
                    vals.remove(vals[i+1])
                    opr.remove(opr[i])
                    vals[i]=str(res)
                    print(vals)
                    print(opr)
                    
            elif o=='x':
                i=opr.index(o)
                print("Step4- ", i)
                res=float(vals[i])*float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
                
            elif o=='+':
                i=opr.index(o)
                res=float(vals[i])+float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
                
            elif o=='-':
                i=opr.index(o)
                res=float(vals[i])-float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)

        # print(opr)
        if len(opr)!=0:
            if opr[0]=='÷':
                try:
                    result = float(vals[0])/float(vals[1])
                except ZeroDivisionError:
                    msj_no_error=False
                    result_error = result_error + "ERROR_VALOR_INDEFINIDO"
                except Exception as e:
                    print(type(e))
            elif opr[0]=='x':
                result = float(vals[0])*float(vals[1])
            elif opr[0]=='+':
                result = float(vals[0])+float(vals[1])
            #error  
            elif opr[0]=='%':
                mod=0
                conv_dec=float(vals[1])
                valor_porc=float(vals[0])
                #result = float(vals[0] + valor_porc)   
                result= float(mod) 
           # else :
               # result = float(vals[0])-float(vals[1])
                
        else:
            try:
                result = float(vals[0])
            except IndexError:
                msj_no_error=False
                result_error= result_error+"ERROR_INGRESE_VALOR_TIPO_NUMÉRICO"
                print(result_error)
            except Exception as e:
                print(type(e))
        
    if(msj_no_error):
        final_result=round(result,4)
        print("Resultado final =>", final_result)
        res=render(request,'base/calculadora.html',{'result':final_result,'values':values})
        return res
    else:
        res_error=render(request, 'base/calculadora.html', {'result': result_error, 'values': valores})
        print("retornamos valor erroneo")
        return res_error
    
def red_github(request):
    return HttpResponseRedirect("https://github.com/Ricardo-20/calculator_js_django")