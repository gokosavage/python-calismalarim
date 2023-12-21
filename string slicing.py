name = "Göks mar"

#indexing[] or slice()
#[start:stop:step]

#firs_name = name[:3] #ikinci kısımda girdiğimiz değerin bir eksiğine karşılık gelen değeri yazdırır
#last_name = name[5:]
#funky_name = name[::3] #step(en sondaki index)girdiğimiz değerin katı olan indexlerin karşılığını yazdırır
#reversed_name = name[::-1] #ters yazdırmak için step'e -1

#print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4) #negatif index(com'un m'sini -1 olarak başlatıp sola doğru say)

print(website1[slice])
print(website2[slice])

