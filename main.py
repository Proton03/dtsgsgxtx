from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
import requests
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
from pyrogram import Client, filters
from p_bar import progress_bar
from subprocess import getstatusoutput
import helper
from logger import logging
import time

import asyncio

from pyrogram.types import User, Message

import sys
import re
import os

bot = Client("bot",
             bot_token="5329315203:AAHMDv5R9K3DCKq1Cl_6NJx1atcUPAjLEpA",
             api_id=7886972,
             api_hash="c138f7cc5f92871bc47c84f0ce71c7af")


@bot.on_message(filters.command(["start"]) & ~filters.edited)
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Send passcode**")
    input0: Message = await bot.listen(editable.chat.id)
    txt0 = (input0.text)
    if txt0 == "a827182718271":
        pass
        await input0.delete(True)
    else:
        await m.reply_text("Password Wrong Not For You Bye")
        await input0.delete(True)
        return

    editable = await m.reply_text("Hi\nPress /pyro")


@bot.on_message(filters.command(["cancel"]))
async def cancel(_, m):
    editable = await m.reply_text("Send passcode**")
    input0: Message = await bot.listen(editable.chat.id)
    txt0 = (input0.text)
    if txt0 == "a827182718271":
        pass
        await input0.delete(True)
    else:
        await m.reply_text("Password Wrong Not For You Bye")
        await input0.delete(True)
        return

    editable = await m.reply_text("Canceling All process Plz wait")
    global cancel
    cancel = True
    await editable.edit("cancled")
    return


@bot.on_message(filters.command("restart"))
async def restart_handler(_, m):
    editable = await m.reply_text("Send passcode**")
    input0: Message = await bot.listen(editable.chat.id)
    txt0 = (input0.text)
    if txt0 == "a827182718271":
        pass
        await input0.delete(True)
    else:
        await m.reply_text("Password Wrong Not For You Bye")
        await input0.delete(True)
        return

    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


@bot.on_message(filters.command(["pyro"]) & ~filters.edited)
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Send passcode**")
    input0: Message = await bot.listen(editable.chat.id)
    txt0 = (input0.text)
    if txt0 == "a827182718271":
        pass
        await input0.delete(True)
    else:
        await m.reply_text("Password Wrong Not For You Bye")
        await input0.delete(True)
        return
    editable = await m.reply_text("Send txt file**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")

        links = []

#         if "referer" in content[0]:
#             refererx = f'--referer "{content[0].split(",")[-1]}"'
#             logging.info(refererx)
#             for i in content[1:]:
#                 links.append(i.split(":", 1))
#         else:
        for i in content:
            links.append(i.split(":", 1))
        refererx = 9

        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return
    editable = await m.reply_text("Send referer \n Example :- htpps://www.google.com/ \n or send **no**")
    inputx: Message = await bot.listen(editable.chat.id)
    raw_textx = inputx.text
    if raw_textx != "no":
          refererx = f'--referer "{raw_textx}"'
    else:
          refererx = 9
          
    
    
    editable = await m.reply_text(
        f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    editable = await m.reply_text("**Enter Batch Name**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text

    await m.reply_text("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text

    editable4 = await m.reply_text(
        "Now send the **Thumb url**\nEg : ```https://telegra.ph/file/7b2c6ae187bb574ab73f6.jpg```\n\nor Send **no**"
    )
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if raw_text == '0':
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(arg, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace(
                "/",
                "").replace("+", "").replace("#", "").replace("|", "").replace(
                    "@", "").replace("*", "").replace(".", "").strip()

            if raw_text2 == "144":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '256x144' in out:
                    ytf = f"{out['256x144']}"
                elif '320x180' in out:
                    ytf = out['320x180']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"

            elif raw_text2 == "180":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '320x180' in out:
                    ytf = out['320x180']
                elif '426x240' in out:
                    ytf = out['426x240']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"

            elif raw_text2 == "240":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '426x240' in out:
                    ytf = out['426x240']
                elif '426x234' in out:
                    ytf = out['426x234']
                elif '480x270' in out:
                    ytf = out['480x270']
                elif '480x272' in out:
                    ytf = out['480x272']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"

            elif raw_text2 == "360":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '640x360' in out:
                    ytf = out['640x360']
                elif '638x360' in out:
                    ytf = out['638x360']
                elif '636x360' in out:
                    ytf = out['636x360']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '638x358' in out:
                    ytf = out['638x358']
                elif '852x316' in out:
                    ytf = out['852x316']
                elif '850x480' in out:
                    ytf = out['850x480']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['852x470']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"

            elif raw_text2 == "480":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['854x470']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '850x480' in out:
                    ytf = ['850x480']
                elif '960x540' in out:
                    ytf = out['960x540']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"

            elif raw_text2 == "720":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '1280x720' in out:
                    ytf = out['1280x720']
                elif '1280x704' in out:
                    ytf = out['1280x704']
                elif '1280x474' in out:
                    ytf = out['1280x474']
                elif '1920x712' in out:
                    ytf = out['1920x712']
                elif '1920x1056' in out:
                    ytf = out['1920x1056']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"
            elif "player.vimeo" in url:
                if raw_text2 == '144':
                    ytf = 'http-240p'
                elif raw_text2 == "240":
                    ytf = 'http-240p'
                elif raw_text2 == '360':
                    ytf = 'http-360p'
                elif raw_text2 == '480':
                    ytf = 'http-540p'
                elif raw_text2 == '720':
                    ytf = 'http-720p'
                else:
                    ytf = 'http-360p'
            else:
                ytf = "no"

            if ytf == "0":
                res = "0"
            elif ytf == "no" or ytf == "mp4":
                res = "NA"
            else:
                res = list(out.keys())[list(out.values()).index(ytf)]

            name = f'{str(count).zfill(3)}) {name1} {res}'

            if "youtu" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={int(raw_text2)}]+bestaudio" --no-keep-video --remux-video mkv "{url}"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "bestvideo+bestaudio" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s" {refererx if refererx!= 9 else ""}'
                logging.info(cmd)
            elif "m3u8" or "livestream" in url:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ytf == "0" or "unknown" in out:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ".pdf" in url:
                cmd = "pdf"
            elif "drive" in url:
                cmd = "pdf"
            elif ytf == "no":
                cmd = f'yt-dlp -o "{name}.mp4" --no-keep-video --remux-video mkv "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'

            try:
                Show = f"**Downloading:-**\n\n** Video Name :-** `{name}\nQuality - {raw_text2}`\n\n **Downloading By Bhartiya Yuva Bot**"
                prog = await m.reply_text(Show)
                cc = f'**File No. =>>** {str(count).zfill(3)}\n**VIDEO NAME =>>** {name1} {res}{aryan}.mkv\n**BATCH NAME =>>** {raw_text0}\n\n **These Files Downloaded By Aryan keep support Us**\n**For Extracting Message Here - @batchExtractor**'
                cc1 = f'**File No. =>>** {str(count).zfill(3)}\n**VIDEO NAME =>>** {name1} {res}{aryan}.pdf\n**BATCH NAME =>>**{raw_text0}\n\n **These Files Downloaded By Aryan keep support Us**\n**For Extracting Message Here - @batchExtractor**'
                if cmd == "pdf" or "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        await prog.delete(True)
                        time.sleep(1)
                        # await helper.send_doc(bot,m,cc,ka,cc1,prog,count,name)
                        reply = await m.reply_text(f"Uploading - `{name}`")
                        time.sleep(1)
                        start_time = time.time()
                        await m.reply_document(ka, caption=cc1)
                        count += 1
                        await reply.delete(True)
                        time.sleep(1)
                        os.remove(ka)
                        time.sleep(3)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                elif cmd == "pdf" or ".pdf" in url:
                    try:
                        ka = await helper.aio(url, name)
                        await prog.delete(True)
                        time.sleep(1)
                        reply = await m.reply_text(f"Uploading - ```{name}```")
                        time.sleep(1)
                        start_time = time.time()
                        await m.reply_document(
                            ka,
                            caption=
                            f'**Title »** {name1} {res}.pdf\n**Caption »** {raw_text0}\n**Index »** {str(count).zfill(3)}'
                        )
                        count += 1
                        # time.sleep(1)
                        await reply.delete(True)
                        time.sleep(1)
                        os.remove(ka)
                        time.sleep(3)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await helper.send_vid(bot, m, cc, filename, thumb, name,
                                          prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")


@bot.on_message(filters.command(["top"]) & ~filters.edited)
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Send passcode**")
    input0: Message = await bot.listen(editable.chat.id)
    txt0 = (input0.text)
    if txt0 == "a827182718271":
        pass
        await input0.delete(True)
    else:
        await m.reply_text("Password Wrong Not For You Bye")
        await input0.delete(True)
        return

    editable = await m.reply_text(f"**Hi im Topranker dl**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    editable = await m.reply_text(
        f"**Copy Paste the App Name of which you want to download videos.**\n\n`vikramjeet`\n\n`sure60`\n\n`theoptimistclasses`"
    )
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text

    editable2 = await m.reply_text("**Enter Title**")
    input5: Message = await bot.listen(editable.chat.id)
    raw_text5 = input5.text

    editable4 = await m.reply_text(
        "Now send the **Thumb url**\nEg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**"
    )
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if raw_text == '0':
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(arg, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace("/", "").replace(
                "+",
                "").replace("#", "").replace("|", "").replace("@", "").replace(
                    ":", "").replace("*", "").replace(".", "").strip()
            # await m.reply_text(name +":"+ url)

            # Show = f"**Downloading:-**\n\n**Name :-** ```{name}\nQuality - {raw_text2}```\n\n**Url :-** ```{url}```"
            # prog = await m.reply_text(Show)
            # cc = f'>> **Name :** {name}\n>> **Title :** {raw_text0}\n\n>> **Index :** {count}'

            if raw_text0 in "vikramjeet":

                y = url.replace("/", "%2F")
                #                 rout = f"https://www.toprankers.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fsignedsec.toprankers.com%2Flivehttporigin%2F{y[56:-14]}%2Fmaster.m3u8"
                rout = f"https://www.toprankers.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fsignedsec.toprankers.com%2F{y[39:-14]}%2Fmaster.m3u8"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')
                cook = "cookie.txt"
                # print (rout)
                # print(url)
            elif raw_text0 in "sure60":
                y1 = url.replace("/", "%2F")
                #                 rout = f"https://onlinetest.sure60.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.sure60.com%2Flivehttporigin%2F{y[49:-14]}%2Fmaster.m3u8"
                rout = f"https://onlinetest.sure60.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.sure60.com%2F{y1[32:-14]}%2Fmaster.m3u8"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')
                cook = "cookie.txt"
            elif raw_text0 in "theoptimistclasses":
                y = url.replace("/", "%2F")
                rout = f"https://live.theoptimistclasses.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.theoptimistclasses.com%2F{y[44:-14]}%2Fmaster.m3u8"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')
                cook = "cookie.txt"

            name = f'{str(count).zfill(3)}) {name1}'
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url}`\n\n**rout** :- `{rout}`"
            prog = await m.reply_text(Show)
            cc = f'**Title »** {name1}.mp4\n**Caption »** {raw_text5}\n**Index »** {str(count).zfill(3)}'

            cmd = f'yt-dlp -o "{name}.mp4" --cookies {cook} "{url}"'
            try:
                download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                os.system(download_cmd)
                filename = f"{name}.mp4"
                subprocess.run(
                    f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"',
                    shell=True)
                await prog.delete(True)
                reply = await m.reply_text(f"Uploading - ```{name}```")
                try:
                    if thumb == "no":
                        thumbnail = f"{filename}.jpg"
                    else:
                        thumbnail = thumb
                except Exception as e:
                    await m.reply_text(str(e))

                dur = int(helper.duration(filename))

                start_time = time.time()

                await m.reply_video(f"{name}.mp4",
                                    supports_streaming=True,
                                    height=720,
                                    width=1280,
                                    caption=cc,
                                    duration=dur,
                                    thumb=thumbnail,
                                    progress=progress_bar,
                                    progress_args=(reply, start_time))
                count += 1
                os.remove(f"{name}.mp4")

                os.remove(f"{filename}.jpg")
                os.remove(cook)
                await reply.delete(True)
                time.sleep(1)
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n\n**rout** :- `{rout}`"
                )
                continue
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done")


@bot.on_message(filters.command(["adda_pdf"]) & ~filters.edited)
async def adda_pdf(bot: Client, m: Message):
    editable = await m.reply_text("Send passcode**")
    input0: Message = await bot.listen(editable.chat.id)
    txt0 = (input0.text)
    if txt0 == "a827182718271":
        pass
        await input0.delete(True)
    else:
        await m.reply_text("Password Wrong Not For You Bye")
        await input0.delete(True)
        return

    editable = await m.reply_text(f"**Hi im Pdf Adda pdf dl**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    editable2 = await m.reply_text("**Enter Token**")
    input5: Message = await bot.listen(editable.chat.id)
    raw_text5 = input5.text

    if raw_text == '0':
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(arg, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace("/", "").replace(
                "+",
                "").replace("#", "").replace("|", "").replace("@", "").replace(
                    ":", "").replace("*", "").replace(".", "").replace(
                        "'", "").replace('"', '').strip()
            name = f'{str(count).zfill(3)} {name1}'
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url}`"
            prog = await m.reply_text(Show)
            cc = f'{str(count).zfill(3)}. {name1}.pdf\n'
            try:
                getstatusoutput(
                    f'curl --http2 -X GET -H "Host:store.adda247.com" -H "user-agent:Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-8; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36" -H "accept:*/*" -H "x-requested-with:com.adda247.app" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://store.adda247.com/build/pdf.worker.js" -H "accept-encoding:gzip, deflate" -H "accept-language:en-US,en;q=0.9" -H "cookie:cp_token={raw_text5}" "{url}" --output "{name}.pdf"'
                )
                await m.reply_document(f"{name}.pdf", caption=cc)
                count += 1
                await prog.delete(True)
                os.remove(f"{name}.pdf")
                time.sleep(2)
            except Exception as e:
                await m.reply_text(
                    f"{e}\nDownload Failed\n\nName : {name}\n\nLink : {url}")
                continue
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")


bot.run()
