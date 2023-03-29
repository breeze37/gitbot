import os

def makeCommits (days : int):
    if days < 1:
        #push
        os.system('git push')
    else:
        dates = f"{days} days ago"
        with open('data.txt', 'a') as file:
            file.write(f'{dates} <- this is the commit for the day!\n')    
            
            
        os.system('git add data.txt')
        
        
        os.system('git commit --date="'+ dates +' "-m "New Commit!"')  
          
        return days * makeCommits(days - 1)
makeCommits(360)      