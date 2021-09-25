
from json import load
 
class Quiz:
    def takeQuiz(self,data):
        print(" \n ###########     Welcome to Quiz   ###########  \n ")
        print("Please select your subject : ")
        for i,j in enumerate(data['quiz']):        # printing available subjects
            print(i+1," - ",j)
            
        opted = int(input())   
        switcher = {1: 'sport', 2:'maths'}         # add more subjects here if added in JSON
        temp = data['quiz'][switcher[opted]]
        result = 0
        
        for i in temp.keys():                      # traversing thr every question  in chosen subject
            print("\n",i,": ",temp[i]['question'],"\n")
            for k,v in enumerate(temp[i]['options']):     # printing available options 
                print(k+1,"- ",v)
            t = int(input("\nenter your option : "))
            
            chosen = temp[i]['options'][t-1]
        
            if temp[i]['answer'] == str(chosen):
                result+=1
        print("\nYou have answered ",result ," question correctly !")


if __name__=="__main__":
    try:
        f = open('data.json',)          # Opening JSON file
        data = load(f)                  # returns JSON object as a dictionary
        f.close()                       # Closing file
        obj = Quiz()
        obj.takeQuiz(data)
    except Exception as e:
        print("Exception occured : ",e)

    
