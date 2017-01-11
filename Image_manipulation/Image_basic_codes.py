# -*- coding: utf-8 -*-
'''
Created on 9 Oca 2017

@author: Purgoufr
'''
# 
# #Renklerin Standart rgba değeri, Standard Color Names and Their RGBA Values
# 
# from PIL import ImageColor
# print(ImageColor.getcolor('red', 'RGBA'))
# print(ImageColor.getcolor('RED', 'RGBA'))
# print(ImageColor.getcolor('Black', 'RGBA'))
# print(ImageColor.getcolor('chocolate', 'RGBA'))
# print(ImageColor.getcolor('CornflowerBlue', 'RGBA'))

#----------------------------------------------------------------------------------------
# #Resim dosyası açma
# from PIL import Image
# catIm = Image.open('zophie.png')
# print(catIm.size)
# 
# #Resim boyutunu getir
# width, height = catIm.size
# print(width)
# print(height)
# 
# #Resim adını getir
# print(catIm.filename)
# 
# #Resim formatını getir
# print(catIm.format)
# print(catIm.format_description)
# 
# #Resim formatını değiştirme 
# catIm.save('zophie.jpg')

#----------------------------------------------------------------------------------------
# # Resim dosyası oluşturma
# from PIL import Image
# im = Image.new('RGBA', (100, 200), 'purple')
# im.save('purpleImage.png')
# im2 = Image.new('RGBA', (20, 20))
# im2.save('transparentImage.png')

#----------------------------------------------------------------------------------------
# # Resimin bir parça kesme 
# from PIL import Image
# catIm = Image.open('zophie.png')
# print(catIm.size)
# croppedIm = catIm.crop((335, 345, 565, 560))
# croppedIm.save('cropped.png')

#----------------------------------------------------------------------------------------
# #Resim kopyalama     
# from PIL import Image
# catIm = Image.open('zophie.png')
# catCopyIm = catIm.copy()
# 
# #Resimi kes
# faceIm = catIm.crop((335, 345, 565, 560))
# print(faceIm.size)
# 
# #Resim yapıştırma
# catCopyIm.paste(faceIm, (0, 0))
# #Resim yapıştırma 
# catCopyIm.paste(faceIm, (400, 500))
# catCopyIm.save('pasted.png')

#----------------------------------------------------------------------------------------
# #Resimden bir parça kopyalayıp resimin tamamına yapıştırma
# from PIL import Image
# catIm = Image.open('zophie.png')
# catImWidth, catImHeight = catIm.size
# 
# faceIm = catIm.crop((335, 345, 565, 560))
# 
# faceImWidth, faceImHeight = faceIm.size
# catCopyTwo = catIm.copy()
# 
# for left in range(0, catImWidth, faceImWidth):
#     for top in range(0, catImHeight, faceImHeight):
#         print(left, top)
#         catCopyTwo.paste(faceIm, (left, top))
# catCopyTwo.save('tiled.png')

#----------------------------------------------------------------------------------------
# #Resimin boyutlarını değiştirme
# 
# from PIL import Image
# #Orijinal resim boyutu
# catIm = Image.open('zophie.png')
# width, height = catIm.size
# 
# #yüksekliği ve genişliği 2 ye böldük
# quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
# quartersizedIm.save('quartersized.png')
# 
# #yüksekliğe ve genişliğe 500 ekledik
# svelteIm = catIm.resize((width+500, height + 500))
# svelteIm.save('svelte.png')

#----------------------------------------------------------------------------------------
# #Resimi döndürme
# from PIL import Image
# 
# catIm = Image.open('zophie.png')
# catIm.rotate(90).save('rotated90.png')
# catIm.rotate(180).save('rotated180.png')
# 
# # Rotate() yönteminde, döndürülen yeni görüntünün tümüne uyacak şekilde olması için True anahtarını kullan
# 
# catIm.rotate(6).save('rotated6.png')
# catIm.rotate(6, expand=True).save('rotated6_expanded.png')
# 
# #Ayna (mirror) yöntemiyle sağa sola yukarı aşşağı döndürme
# catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
# catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

#----------------------------------------------------------------------------------------
# # Piksellerle resim oluşturma (getpixel() ve putpixel() Kullanımı) 

# from PIL import Image
# im = Image.new('RGBA', (100, 100))
# im.getpixel((0, 0))
# 
# for x in range(100):
#     for y in range(50):
#         im.putpixel((x, y), (210, 210, 210))
#         
# from PIL import ImageColor
# for x in range(100):
#     for y in range(50, 100):
#         im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
# im.getpixel((0, 0))
# im.getpixel((0, 50))
# im.save('putPixel.png')

#----------------------------------------------------------------------------------------
# #Resime logo ekleme
# import os
# from PIL import Image
# 
# SQUARE_FIT_SIZE = 300
# LOGO_FILENAME = 'logo.png'
# 
# logoIm = Image.open(LOGO_FILENAME)
# logoWidth, logoHeight = logoIm.size
# print(logoWidth)
# print(logoHeight)
# os.makedirs('withLogo', exist_ok=True)   #exist_ok=True bu dosya zaten var diye hata vermesini önler
# 
# # Loop over all files in the working directory. 
# #Eğer çalışma alanında jpg,png veya senin tanımladığın isimde logo yoksa açmaz varsa im değişkenine atar
# 
# for filename in os.listdir('.'):
# #     if not (filename.endswith('.png') or filename.endswith('.jpg')) \
# #         or filename == LOGO_FILENAME:   
#     if not (filename.endswith('.png') or filename.endswith('.jpg') or filename == LOGO_FILENAME):
#         continue # skip non-image files and the logo file itself
# 
#     im = Image.open(filename)
#     width, height = im.size
# 
# # Check if image needs to be resized.
# #Logo ekleyeceğimiz resimin boyutunu 300x300 yapıyoruz
#     if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
#         # Calculate the new width and height to resize to.
#         if width > height:
#             height = int((SQUARE_FIT_SIZE / width) * height)
#             width = SQUARE_FIT_SIZE
#         else:
#             width = int((SQUARE_FIT_SIZE / height) * width)
#             height = SQUARE_FIT_SIZE
#             
#         # Resize the image.
#         print('Resizing %s...' % (filename))
#         im = im.resize((width, height))
#         
#         # Resize the LOGo. LOGO nun boyutunu değiştirdik
#         logoIm=logoIm.resize((75,100))
#         logoWidth, logoHeight = logoIm.size
#         
#         print('Adding logo to %s...' % (filename))
#         im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
# 
#         # Save changes.
#         im.save(os.path.join('withLogo', filename))

#----------------------------------------------------------------------------------------
# #Geometrik şekillerle resim oluşturma Draw function
# from PIL import Image, ImageDraw
# im = Image.new('RGBA', (200, 200), 'white')
# draw = ImageDraw.Draw(im)
# 
# #koordinat sisteminde düşün her parantez iki boyutu ifade eder (x,y)
# draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black') #siyah çerçeve
# 
# draw.rectangle((20, 30, 60, 60), fill='blue')
# 
# draw.ellipse((120, 30, 160, 60), fill='red')
# 
# draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)),fill='brown')
# 
# #For döngüsü ile çizilmiş bir yeşil çizgi deseni
# for i in range(100, 200, 10):
#     draw.line([(i, 0), (200, i - 100)], fill='green')
# 
# im.save('drawing.png')

#----------------------------------------------------------------------------------------
# # text png oluşturma. Yazı yazarak resim dosyası oluşturma
# from PIL import Image, ImageDraw, ImageFont
# import os
# 
# im = Image.new('RGBA', (200, 200), 'white')
# draw = ImageDraw.Draw(im)
# 
# draw.text((20, 150), 'Hello', fill='purple')
# 
# fontsFolder = 'FONT_FOLDER' # e.g. 'Library/Fonts'
# arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)  #yazı fontu ve yazı boyutu belirleme
# 
# draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
# im.save('text.png')

#----------------------------------------------------------------------------------------





















    