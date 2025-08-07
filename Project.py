import pygame
print(
    "!!!!********************WORD AND SENTENCE*********************!!!!\n"
)
print("\t1. Hello")
print("\t2. Goodbye")
print("\t3. Baby")
print("\t4. Brother")
print("\t5. Love")
print("\t6. Can't")
print("\t7. Change")
print("\t8. Correct")
print("\t9. Don't")
print("\t10. Father")
print("\t11. Friend")
print("\t12. Happy")
print("\t13. House")
print("\t14. Intelligent")
print("\t15. Justice")
print("\t16. Line")
print("\t17. Mother")
print("\t18. Movie")
print("\t19. Night")
print("\t20. No")
print("\t21. Past")
print("\t22. Pay")
print("\t23. Please")
print("\t24. School")
print("\t25. See")
print("\t26. Sentence")
print("\t27. Taste")
print("\t28. Thank you")
print("\t29. You're Welcome")
print("\t30. Yes")
print("\t31. I Love You")
print("\t32. OK")
print("\t33. Science")
print("\t34. Sorry")
print("\t35. How")
print("\t36. Which")
print("\t37. Why")
print("\t38. Where")
print("\t39. When")
print("\t40. What")
print("\t41. Who")
print("\t42. Bored")
print("\t43. Eat")
print("\t44. Finished")
print("\t45. More")
print("\t46. Help")
print("\t47. Bed")
print("\t48. Book")
print("\t49. bath")
print("\t50. Smart")
print("\t51. Sit")
print("\t52. Share")
print("\t53. quiet")
print("\t54. Proud")
print("\t55. Listen")
print("\t56. Wait")
print("\t57. play")
print("\t58. Stop")
a= str(input("Enter any word or sentence from above list to know the sign languge of it:-\n "))
b=a.upper()
if (b=="HELLO"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\hello.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="GOODBYE"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\goodbye.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="BABY"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\baby.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="BROTHER"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\brother.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="LOVE"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\love.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="CAN'T"):
   
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r"C:\Users\Nayra\Desktop\Python\me\can't.jpg")
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="CHANGE"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\change.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="CORRECT"):
   
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\correct.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="DON'T"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r"C:\Users\Nayra\Desktop\Python\me\don't.jpg")
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="FATHER"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\father.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="FRIEND"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\friend.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="HAPPY"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\happy.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="HOUSE"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\house.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="INTELLIGENT"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\intelligent.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="JUSTICE"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\justice.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="LINE"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\line.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()

elif (b=="MOTHER"):
   
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\mother.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="MOVIE"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\movie.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="NIGHT"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\night.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="NO"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\no.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="PAST"):
   
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\past.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="PAY"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\pay.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="PLEASE"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\please.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="SCHOOL"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\school.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="SCIENCE"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\science.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="SEE"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\see.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="SENTENCE"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\sentence.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="TASTE"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\taste.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="THANK YOU"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\thankyou.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="YOU'RE WELCOME"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\welcome.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="YES"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\yes.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="I LOVE YOU"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\iloveyou.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="OK"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\ok.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="SORRY"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\sorry.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="HOW"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\how.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="WHICH"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\which.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="WHY"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\why.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="WHERE"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\where.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="WHEN"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\when.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="WHAT"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\what.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="WHO"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\who.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="STOP"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\stop.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="BORED"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\bored.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="EAT"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\eat.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="FINISHED"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\finished.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="MORE"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\more.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="HELP"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\help.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="BED"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\bed.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="BOOK"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\book.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="BATH"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\bath.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="SMART"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\smart.png')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="SIT"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\sit.png')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="SHARE"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\share.png')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="QUIET"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\quiet.png')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="PROUD"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\proud.png')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="LISTEN"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\listen.png')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="WAIT"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\wait.png')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
elif (b=="PLAY"):
    
    pygame.init()
    displaywidth=800
    displayheight =600
    surface = pygame.display.set_mode((displaywidth,displayheight))
    displayimage = pygame.image.load(r'C:\Users\Nayra\Desktop\Python\me\play.jpg')
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
else:
    print("Not found")
