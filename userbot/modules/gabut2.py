from time import sleep
from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import hiro_cmd


@hiro_cmd(pattern='Hiro(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku Hiroshi`")
    sleep(3)
    await typew.edit("`19 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Di Banten, Salam Brody:)`")
# Create by myself @localheart


@hiro_cmd(pattern='sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Kamu Tay Kata Hiroshi`")
    sleep(1)
    await typew.edit("`Fak Cinta Fak Fak Fak Tayπ`")
# Create by myself @localheart


@hiro_cmd(pattern='semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


CMD_HELP.update({
    "oi": f"πΎπ€π’π’ππ£π: `{cmd}Hiro`\
    \nβ³ : perkenalan Hiro\
    \n\nπΎπ€π’π’ππ£π: `{cmd}sayang`\
    \nβ³ : Gombalan maut`\
    \n\nπΎπ€π’π’ππ£π: `{cmd}semangat`\
    \nβ³ : Jan Lupa Semangat."
})
