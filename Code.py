from PIL import Image, ImageDraw, ImageFont

facebook = Image.open("facebook.jfif").convert("RGBA")
flag = Image.open("flag.png").convert("RGBA")
molotov = Image.open("molotov.png").convert("RGBA")
sign = Image.open("sign.png").convert("RGBA")
smoke = Image.open("Smoke.png").convert("RGBA")

flag = flag.resize((450, 400)).rotate(-15, expand=True)
molotov = molotov.resize((150, 150))
sign = sign.resize((150, 150)).rotate(0, expand=True)
smoke = smoke.resize((500, 500))

width, height = 1080, 900
background = Image.new("RGBA", (width, height), (255, 255, 255, 255))

background.paste(facebook, (0, height - facebook.height), facebook)
background.paste(flag, (500, height - flag.height - 300), flag)
background.paste(sign, (600, height - sign.height - 100), sign)

sign1 = sign.rotate(0, expand=True)
sign2 = sign.resize((120, 120)).rotate(0, expand=True)
sign3 = sign.resize((180, 180)).rotate(-10, expand=True)
background.paste(sign1, (40, height - sign1.height - 250), sign1)
background.paste(sign2, (370, height - sign2.height - 280), sign2)
background.paste(sign3, (850, height - sign3.height - 300), sign3)

background.paste(smoke, (-50, height - smoke.height + 150), smoke)
smoke2 = smoke.resize((400, 400))
background.paste(smoke2, (700, height - smoke2.height + 150), smoke2)

molotov1 = molotov.rotate(10, expand=True)
molotov2 = molotov.rotate(-20, expand=True)
molotov3 = molotov.rotate(45, expand=True)
background.paste(molotov, (150, height - molotov.height - 400), molotov)
background.paste(molotov1, (300, height - molotov1.height - 350), molotov1)
background.paste(molotov2, (450, height - molotov2.height - 300), molotov2)
background.paste(molotov3, (700, height - molotov3.height - 450), molotov3)

draw = ImageDraw.Draw(background)
font = ImageFont.truetype(r"C:\Windows\Fonts\ARLRDBD.TTF", 100)
draw.text((200, 20), "September 21: ", font=font, fill="red")

background.save("poster_result.png")
background.convert("RGB").show()
