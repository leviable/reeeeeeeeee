import curses
import time


def reeeeeeeeee():
    s = curses.initscr()
    # Do colors later
    # curses.start_color()
    # curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.noecho()
    curses.curs_set(0)
    s.nodelay(True)
    s.leaveok(True)
    s.scrollok(False)

    run_time = 3.0
    delay = 0.030

    start_at_x = int(curses.COLS / 2 - 39)
    start_at_y = int(curses.LINES / 2 - 20)

    for x in range(int(run_time // delay)):
        for y in range(len(frames[0])):
            # s.addstr(15, x, "reeeeeeeeeee", curses.color_pair(1))
            try:
                s.addstr(start_at_y + y, start_at_x, frames[x % 6][y])
            except curses.error:
                pass

        s.refresh()
        time.sleep(delay)

    curses.endwin()


frames = [
    [
        'ddddddddddddddddddddddolc:;:::::::cccllllooddddddddoolccccccllooodddddddddddddd',
        'ddddddddddddddddddddocc:::::::::::::::cccclooooollcc:::::::::cclloodddddddddddd',
        'dddddddddddddddddolc::::::::::::::::::::::cccc::::::::::::::::::ccllodddddddddd',
        'dddddddddddddddolc::::::::::::::::::::::::::::::::::::::::::::::::ccloddddddddd',
        'ddddddddddddddlc:::::::::::;;;;;;;:::::::::::::::::::::::::::::::::cllodddddddd',
        'ddddddddddddolc:::::::::;;;;:::::::::::::::::;;;;;::::::;;;;::::::::ccloddddddd',
        'dddddddddddolc::::::::::::::::::::::::::::::::;;;;;:::::::::::::::::::clllooddd',
        'ddddddddddolc:::::::::::::::::::::::::::::::::;;;:::::::::::::::::::::::::ccloo',
        'dddddddddolc:::::::::::::::::::;;;;;;;;;;;;:::;;;;;::::::::::::::;;;;;;;;;;;:cl',
        'dddddddolc::::::::::::::::::;;;;;;;;;;;;;;;:::;;;;;;::::::::;;;;;;;;;;;::;;;;::',
        'dddddlc::::::::::::::::::;;;;;;;;::cccccccc::::;;;;;:::;;;;;;;;;;::::::ccllccc:',
        'dddoc:::::::::::::::::;;;;;;;:clodxxxxxxxxddolcc::::;;;;;;;;;;::::cloddxxxxxddo',
        'ddlc:::::::::::::::::;;;;;::loxkkkkkkkkkkkkxdocclllc::;;;;:::clodxxkkkkkkxoooxx',
        'olc::::::::::::::::::::::::clodxxkkkkkkkkkkdlclodxxdoccccloddxkkkkkkkkkkdlcloxk',
        'lc:::::::::::::::::::::::::::cclloddxxxxxxxddooddollc:cloddxxxxxxxxxxxxxdolooll',
        'c:::::::::::::::::::::::::::::::::ccccccccccccc:::::;;:::ccccccclccccccccc::::c',
        ':::::;;;::::::::::::::::::::::::::::::::::::::::;;;;;:::::::::::::::::::::cclod',
        '::::;;;;:::::::::::::::::::::::::::::::::;;;;;;;;;::::::::::::;;;;;;;;::clodddd',
        '::;;;;;:::::::::::::::::;;;:::::::::::;;;;;;;;;;;;::::::::::;;;;;::::::cclooddd',
        '::;;:::::::::::::;;;;;;;;;;;;;;;;;;;;;:::;;;;;;;:::::::::::::::::::;;;;;::clodd',
        ':::::::::::::::;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::coddo',
        ':::::::::::::;;;;::;;,\'\'\'\'\'\'\'\'\'\'\',,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;::::;;:clodool',
        '::::::::::::;;;:;;,\'..................\'\'\'\'\',,,,,,;;;;;;;;;:::::::::cccloddddddd',
        '::::::::::;;;;:;,\'..................................\',;clllloooooodddddddoooodd',
        '::::::::::;;;:;,\'.........................\'\'.......\';lodddddddddddddollcc:::ccc',
        ':::;;;;;;;;;;;,\'..................\'\',,;;;;;;,,,\'\',;codddddddddddollc:::;;::::::',
        '::;;;;;:;;;;;;,\'...............\'\',;::;;;;;;;;;;;;;:ccclloooollcc::;::::ccllcc::',
        '::;;:::::;;;;,\'...............\';;:;;,\'\'.....\'\'\',,;:::::::::::;;;:::clodddddoooo',
        '::::::::;;;;;,\'..............\';;:;,\'..........\',:lllccc:::::::cclooddoooddddddd',
        '::::::::;;;;;,\'\'............\',;:;,\'...........,:ldddddoooooooddddddoooodddddddd',
        ':::::::::;;;;,,\'............\',;;;,\'..........\',:ldddddddddddddddddddddddddddddd',
        'c:::::::;;;;;;,,\'\'\'\'...\'\'\'\',,;;;;,,\'\'\'\'\'\'\'...\';:loooooooooooooooooooooddddddddd',
        ':::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,;;:::::::::::::::::::::ccloddddddd',
        ':::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:coddddolll',
        ':::::::::::::::;;;;;;;;::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::cclllodddddoc::c',
        ':::::::::::::::::::::::::::;;;:::;;;;;;;::::::::::::;;;;:ccloodddddddddddlc::::',
        ':::::::::::::::::::::::::;;;;:::::::;;;;;;;;;;;;;;;;;::clooddddddddddddoc:::::;',
        ':::::::::::::::::::::::;;;;:::::::::;;;;;;::::::::::::::ccllodddddddolc::::::::',
        '::::::::::::::::::::;;;;::::::::::::::;;;;:::::::::::::::::cclloollc:::::::::::',
        ':::::::::::::::::;;;;::::::::::::::;;;;;;::::::::::::::::::::cc::::::::::::::::',
    ], [
        'dddddddddddddddddddddddollccccccllloooddddddddddddddddooooooddddddddddddddddddd',
        'ddddddddddddddddddddolcc::::::::::ccclllooddddddoollccccccccllooddddddddddddddd',
        'dddddddddddddddddolc::::::::::::::::::::cclllllc::::::::::::::ccloodddddddddddd',
        'dddddddddddddddolc::::::::::::::::::::::::::::::::::::::::::::::ccloddddddddddd',
        'dddddddddddddolc:::::::::::::::::::::::::::::::::::::::::::::::::cclodddddddddd',
        'ddddddddddddoc::::::::::;;;;;;::::::::::::::::::::::::::::::::::::ccloddddddddd',
        'dddddddddddoc:::::::::;;::::::::::::::::::::;;;;;;;;;;;;;;;::::::;::clooddddddd',
        'ddddddddddoc:::::::::::::::::::::::::::::::::;;;;:::::::::::::::::::::ccllooddd',
        'dddddddddoc:::::::::::::::::::::::;;;;;:;;:::;;;;:::::::::::::::::;;;;;;:::clod',
        'dddddddolc:::::::::::::::::::;;;;;;;;;:::::::;;;;;::::::::::::;;;;;;;;;;;;;:ccl',
        'dddddol::::::::::::::::::;;;;;;;;;;;::::::::::;;;;;:::::::;;;;;;;;;:::::::::::c',
        'dddlc::::::::::::::::::;;;;;;;:clloooooollccc::::;;;;;;;;;;;;;;::::cclooooollcc',
        'dol:::::::::::::::::;;;;;;;:codxkkkkkkkkkxxdolccc:::;;;;;;;:::cclodxxkkkkxxdddd',
        'oc::::::::::::::::::::::::codxkkkkkkkkkkkkxolccodolcc::::cclodxkkkkkkkkxolloxkx',
        'c:::::::::::::::::::::::::clloddxxkkkkkkkxdooodxxdolcclldxxkkkkkkkkkkkxdllodddo',
        '::::::::::::::::::::::::::::::cclloooodddooooollcc::::clloooodddddddooolllcc::c',
        '::::;;::::::::::::::::::::::::::::::::::::::::::::;;;;:::::::::::::::::::::clod',
        ':::;;;;::::::::::::::::::::::::::::::::::::::;;;;;::::::::::::::::::::::clodddd',
        '::;;;;;::::::::::::::::::::::::::::::::;;;;;;;;;;::::::::::;;;;;;;:;;:clodddddd',
        ':;;;;:::::::::::::;;;;;;;;;;;::::::::::::;;;;;;;::::::::::::::::::::::::clodddd',
        ':::::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::::::::::::::::;;;;;;;;::cldddd',
        ':::::::::::::;;;;::;;;;,,,,,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::;;:clodooo',
        ':::::::::::;;;;:;;,\'\'..........\'\'\'\'\',,,,,;;;;;;;;;;;;;;;;;;;;;;:;;;::ccloddoooo',
        '::::::::::;;;;;;,\'.......................\'\'\'\'\'\',,,,,,,;:::ccccccllloodddddddddd',
        ':::::::::;;;;;,\'...................................\';clooodddddddddddoolllllooo',
        '::::::::;;;;;;\'.....................\'\'\'\'\'\'\'\'\'\'...\';loddddddddddddollc:::;:::::c',
        ':;;;;;;;;;;;;,\'.................\',,;;;;;;;;;;,,,;:lloodddddddoolc::;;;:::::::;:',
        ';;;;;:::;;;;,\'...............\',;;:;;,,\'\'\'\',,,,,;;::::cccccccc::;;;::cllooollccl',
        '::::::::;;;;,\'..............\',;:;;,\'.........\',;:c::::::;;;;;:::clooddddddddddd',
        '::::::::;;;;,\'.............\',;;;,\'...........,:loooollcccccclloddddoloodddddddd',
        '::::::::;;;;,\'\'............\',;;;,\'..........\',coddddddddddddddddddooodddddddddd',
        '::::::::;;;;,,\'\'..........\'\',;;,,\'\'.........\';coddddddddddddddddddddddddddddddd',
        '::::::::;;;;;;,,,,,\'\'\',,,,;;;;;;,,,,,,,,\'\'\'\',;:clllllllllllcccccccclloddddddddd',
        '::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::::::::::;;;;;;;;;::clodddddooo',
        ':::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::::clodddolcccl',
        ':::::::::::::::::;::::::::::::::;;;;;;;;::::::;;;;;;;;;;;::cllooooddddddol:::cc',
        ':::::::::::::::::::::::::;;;:::;;;;;;;::::::::::::;;;::clodddddddddddddoc::::::',
        ':::::::::::::::::::::::;;;;::::::::;;;;;;;;;;;:::::::ccllodddddddddddoc:::::::;',
        ':::::::::::::::::::::;;;:::::::::::::;;;::::::::::::::::cclloodddoolc::::::::::',
        '::::::::::::::::::;;;;:::::::::::::::;;;;:::::::::::::::::ccllolcc:::::::::::::',
    ], [
        'dddddddddddddddddddddoc::::::::::::::::::::cclloolc::::::::::::::cclloddddddddd',
        'dddddddddddddddddddolc:::::::::::::::::::::::cc:::::::::::::::::::ccllodddddddd',
        'dddddddddddddddddol:::::::::::::::::::::::::::::::::::::::::::::::::ccloddddddd',
        'ddddddddddddddddlc:::::::::::;;;;;;;::::::::::::::::::::::::::::::::::clodddddd',
        'ddddddddddddddolc:::::::::;;;:::::::::::::::::;;;;;;;:;;;;;;;;;;:::;;::cloddddd',
        'dddddddddddddolc::::::::::::::::::::::::::::::::;;;;;:::::::::::::::::::ccllood',
        'ddddddddddddolc::::::::::::::::::::::::::;;;;:::;;;::::::::::::::::::::::::::cl',
        'dddddddddddolc:::::::::::::::::::;;;;;;;;;;;:::::;;;;:::::::::::::;;;;;;;;;;;;:',
        'dddddddddolc:::::::::::::::::;;;;;;;;;;;;;;;:;;::;;;;;::::::::;;;;;;;;;:::;:;;:',
        'ddddddolc:::::::::::::::::;;;;;;;;;:cclllllccc::::;;;;::;;;;;;;;;;;:::::ccllllc',
        'dddddoc:::::::::::::::::;;;;;;;:codxxkkkkkxxxddolc::::;;;;;;;;;;:::cllodxkkkxxd',
        'dddolc:::::::::::::::::;;;;:::loxkkkkkkkkkkkkxdlcclollc::;;:::cllodxkkkkkkxdolo',
        'ddolc::::::::::::::::::::::::cloddxkkkkkkkkkkdllloxxxdocccloddxkkkkkkkkkkkdlclo',
        'dolc::::::::::::::::::::::::::::cclooddddxxxxdooooollcc::cloddddxxxxxxxxddoolll',
        'olc:::::;:::::::::::::::::::::::::::::ccccccccc:::::::;;;:::cccccccccccccc:::::',
        'lc::::;;;::::::::::::::::::::::::::::::;:::::::::;;;;;::::::::::::::::::::::clo',
        'c:::::;;;;:::::::::::::::::::::::::::::::::::;;;;;;;:::::::::::;;;;;;;;;::clddd',
        'c:::;;;;;::::::::::::::;;;;;;;;:::::::::::;;;;;;;;;;:::::::::::;;:::::::::cclod',
        ':::::::::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::::::::::::::::::;;;;;;;:clo',
        '::::::::::::::::;;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::;:cod',
        ':::::::::::::::;;;;:;;,,\'\'\'\'...\'\'\'\'\',,,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;::;;::clddo',
        '::::::::::::::;;;:;;,\'....................\'\'\'\'\'\',,,,,;;;;;;::::::::cccllooddddd',
        '::::::::::::;;;;;;,\'..................................\',:cloooooodddddddddooooo',
        '::::::::::::;;;;;,\'........................\'\'\'\'......,:lddddddddddddddolcc:::::',
        ':::::;;;;;;;;;;;,\'..................\',,,;;;;;;;,,,\',;cooddddddddddolc::;;;:::::',
        '::::;;;;;::;;;;;,\'...............\',;;:;;;;,,,,,,;;;;::ccclllllllc::;;;::ccllllc',
        ':::::::::::;;;;,\'\'..............\';;:;,\'\'\'......\'\'\',;::::::::::;;;;::ccloddddddo',
        'c::::::::::;;;;,\'..............\';;;;,\'..........\';clollcccc::::cclooddooooddddd',
        'c::::::::::;;;;,\'\'............\',;;;,\'\'..........,:ldddddddoooodddddddoooodddddd',
        'lc:::::::::;;;;,,\'............\',;;;,\'..........\',:ldddddddddddddddddddddddddddd',
        'llc:::::::;;;;;;;,,\'\'\'\'\'\'\'\'\'\',,;;;;,,\'\'\'\'\'\'\'\'\'\'\';:loooooooooooolllllllloodddddd',
        'lc:::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::::::::::::::::::::::cloddddd',
        ':::::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::::coddddol',
        '::::::::::::::::::::;::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::clllloodddddlc:',
        ':::::::::::::::::::::::::::::;;;:::;;;;:;;:::::::::::;;;;::cllodddddddddddolc::',
        ':::::::::::::::::::::::::::;;;::::::::;;;;;;;;;;;;:;;;;::clooddddddddddddlc::::',
        ':::::::::::::::::::::::::;;;::::::::::;;;;;;::::::::::::::ccllooddddddolc::::::',
        '::::::::::::::::::::::;;;:::::::::::::::;;;;:::::::::::::::::cclllllcc:::::::::',
        '::::::::::::::::::::::::::::::::::;;;;;;;::::::::::::::::::::::::::::::::::::::',
        ':::::::::::::::::::::::::::::::::;;;:::::::::::::::::::::::::::::::::::::::::::',
    ], [
        'dddddddddddddddddddddddddddoolllllooodddddddddddddddddddddddddddddddddddddddddd',
        'dddddddddddddddddddddddolcc::::::cccclllloodddddddddoollllllllooodddddddddddddd',
        'ddddddddddddddddddddolc:::::::::::::::::ccclloooolcc::::::::::ccclooddddddddddd',
        'ddddddddddddddddddoc::::::::::::::::::::::::cc:::::::::::::::::::cclooddddddddd',
        'ddddddddddddddddoc:::::::::::::::::::::::::::::::::::::::::::::::::cllodddddddd',
        'ddddddddddddddolc:::::::::::;;;;;;;;::::::::::::::::::::::::::::::::clloddddddd',
        'dddddddddddddoc:::::::::;;;;:::::::::::::::::;;;;;;::::;;;;;;::::::::cloodddddd',
        'ddddddddddddoc::::::::::::::::::::::::::::::::;;;;;;:::::::::::::::::::cclloodd',
        'dddddddddddoc:::::::::::::::::::::::::;;;::::::;;:::::::::::::::::::::;::::cclo',
        'ddddddddddoc::::::::::::::::::::;;;;;;;;;;;::::;;;;;:::::::::::::;;;;;;;;;;;;:c',
        'dddddddolc::::::::::::::::::;;;;;;;;;;;;;;::::::;;;;;::::::::;;;;;;;;;;;;::;;::',
        'dddddol::;;::::::::::::::;;;;;;;;;:ccllllcccc::::;;;;;;;;;;;;;;;;;:::::ccllllcc',
        'dddolc::::::::::::::::;;;;;;;;:codxxkkxxxxxddolcc::::;;;;;;;;;::::cloodxkkkxxdd',
        'ddol:::::::::::::::::;;;;:;:cldkkkkkkkkkkkkkxolcclllc::;;;:::cllodxkkkkkkxdoldx',
        'dol::::::::::::::::::::::::cloddxxkkkkkkkkkxdlcldxxxolcccloddxkkkkkkkkkkxollodx',
        'ol::::::::::::::::::::::::::::ccllodddxxxxxddooooollc::clodddxxxxxxxxxxxdolloll',
        'l:::::::::::::::::::::::::::::::::::cccccccccc::::::;;;:::cccccccccccccc::::::c',
        'c::::;;;::::::::::::::::::::::::::::::::::::::::;;;;;:::::::::::::::::::::cclod',
        ':::::;;;;::::::::::::::::::::::::::::::::::;;;;;;;;::::::::::::;;;;;;;;::lodddd',
        ':::;;;;:::::::::::::::::;;;;:::::::::::::;;;;;;;;;:::::::::::;;;;:::::::ccloddd',
        '::::::::::::::::::;;;;;;;;;;;;;;;;;;;;;:::;;;;;;::::::::::::::::::::;;;;;:clodd',
        ':::::::::::::::;;;;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:;;:lodd',
        ':::::::::::::;;;;::;;,\'\'\'\'\'\'\'\'\'\'\'\'\',,,,;;;;;;;;;;;;;;;;;;;;;;;;;::::;;;::coddol',
        '::::::::::::;;;;:;,\'....................\'\'\'\'\',,,,,,;;;;;;;::::::::ccccloddddddd',
        ':::::::::::;;;:;;,\'.................................\'\',:cllooooooddddddddoooooo',
        '::::::::::;;;;;;\'\'.......................\'\'\'\'\'.....\',codddddddddddddollc::::::c',
        '::::;;;;;;;;;;;,\'..................\',,;;;;;;;,,,\'\',:lodddddddddddolc::;;;;:::::',
        '::;;;;;::;;;;;,\'................\',;;:;;;;,,,,,,;;;::cccllloolllc::;;;::cclllcc:',
        ':::;:::::;;;;;,\'..............\',;;:;,\'\'......\'\'\',;:::::::::::;;;;::cloodddddooo',
        ':::::::::;;;;;,\'.............\',;;;;\'...........\';cllllccc:::::cclooddoooodddddd',
        ':::::::::;;;;;,\'.............\',;;;,\'..........\';codddddoooooodddddddooooddddddd',
        'c:::::::::;;;;,\'\'...........\'\',;;,,\'..........\';coddddddddddddddddddddddddddddd',
        'c::::::::;;;;;;,,,\'\'\'\'\'\'\'\'\',,,;;;,,,\'\'\'\'\'\'\'..\',;cloooooooooooollllllloodddddddd',
        'c:::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::::::::::::::::::::cclodddddd',
        '::::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::::loddddolc',
        ':::::::::::::::::;;;;;::::::::;;;:;;;;;;;;;;:;;;;;;;;;;;;;;;;::cllllooddddol:::',
        ':::::::::::::::::::::::::::;;;:::;;;;;;;:::::::::::::;;;::cloodddddddddddoc::::',
        ':::::::::::::::::::::::::;;;;::::::::;;;;;;;;;;;;;;;;;::cloddddddddddddolc::::;',
        '::::::::::::::::::::::::;;;::::::::::;;;;;;:::::::::::::ccclooodddddool::::::::',
        ':::::::::::::::::::::;;;;::::::::::::::::;;::::::::::::::::cclloddolc::::::::::',
    ], [

        'dddddddddddddddddddol:::::::::::::::::cccllooddolc::::::::::ccclloddddddddddddd',
        'dddddddddddddddddolc:::::::::::::::::::::cccccc:::::::::::::::ccclooddddddddddd',
        'dddddddddddddddoc::::::::::::::::::::::::::::::::::::::::::::::::cllodddddddddd',
        'dddddddddddddolc::::::::::::;;;;;:::::::::::::::::::::::::::::::::clloddddddddd',
        'ddddddddddddoc::::::::::;;;;:::::::::::::::::;;::::::::::::::::::::cllodddddddd',
        'dddddddddddoc:::::::::;;:::::::::::::::::::::;;;;;;;;;;;;:::::::::::ccloooddddd',
        'ddddddddddoc:::::::::::::::::::::::::::::::::;;;::::::::::::::::::::::::ccloodd',
        'dddddddddoc:::::::::::::::::::::;;;;;;;;;;:::;;;;;:::::::::::::::;;;;;;;;;::clo',
        'dddddddolc::::::::::::::::::;;;;;;;;;;;:::::::;;;;;::::::::::;;;;;;;;;;;;;;;:cc',
        'ddddolc:;::::::::::::::::;;;;;;;;;:::c:::::::::;;;;:::::;;;;;;;;;;::::::ccc::::',
        'ddolc:::::::::::::::::;;;;;;;;cloddddddddoollc::::;;;;;;;;;;;;;:::ccloddxdddoll',
        'dol:::::::::::::::::;;;;;;:cldxkkkkkkkkkkkkxolccccc:;;;;;;:::cclodxkkkkkkxddxxx',
        'oc::::::::::::::::::::::::cldxxkkkkkkkkkkkxoccloddolc:::cllodxkkkkkkkkkxoccldkk',
        'c:::::::::::::::::::::::::cccloodxxxkkkkkkxooddddoolcccodxxxkkkkkkkkkkxdoooodol',
        '::::::::::::::::::::::::::::::::ccllllllllllllcc:::::::cccllllllollllllcccc:::c',
        '::::;;::::::::::::::::::::::::::::::::::::::::::;;;;;:::::::::::::::::::::cllod',
        '::::;;;:::::::::::::::::::::::::::::::::::::;;;;;;::::::::::::::::::;;:cloddddd',
        '::;;;;;:::::::::::::::::::::::::::::::;;;;;;;;;;;::::::::::;;;;;;;;;::ccloddddd',
        ':;;;;::::::::::::;;;;;;;;;;;;;;;:::;;;:::;;;;;;:::::::::::::::::::::;;;:ccloddd',
        '::::::::::::::;;;;;;:;;;;;;;;;;;;;;;;;;;;;;;;;;:::::::::::::::;;;;;;;;;;:cloddd',
        '::::::::::::;;;;:::;;,,\'\'\'\'\',,,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::::;;:coddool',
        ':::::::::::;;;;:;;,\'..............\'\'\'\'\',,,,,;;;;;;;;;;;;;;;;;;:::::::cloddddood',
        '::::::::::;;;:;;,\'...........................\'\'\'\'\'\'\'\',;:ccclllllooooddddddddddd',
        ':::::::::;;;:;,\'...................................,:lodddddddddddddoolccccclll',
        '::::;;::;;;;;;,\'...................\'\',,,,,,,,\'\'\'\',:ldddddddddddddolc::;;;;;::::',
        ':;;;;;;;;;;;;,\'................\'\',;;;;;;;;;;;;,;;:cllooooddooolc:::::::cccc::;:',
        ';;;;;:::;;;;;,\'..............\',;;:;;,\'\'\'\'\'\'\'\',,,;;:::::::cc:::;;;::clooddooolll',
        '::::::::;;;;,\'\'.............\',;:;;\'..........\',;cccc:::::;;::::clloddoddddddddd',
        '::::::::;;;;,\'\'............\',;;;,\'...........\';loddoooollllloodddddollodddddddd',
        '::::::::;;;;,,\'............\',;;;,\'...........,:lddddddddddddddddddddddddddddddd',
        ':::::::;;;;;;,,\'\'........\'\',,;;;,\'\'\'........\',:loddddddddddddddoooooddddddddddd',
        ':::::::::;;;;;;;,,,,,,,,;;;;;;;;;;;;;,,,,,,,,;:ccccccccccccccc::::ccloodddddddd',
        ':;::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:cloddddollo',
        '::::::::::::::;;;;;;;;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::ccccloddddolc:cl',
        ':::::::::::::;;::::::::::::;;:::;;;;;;:::::::::::::;;;;;::clloddddddddddoc:::cc',
        '::::::::::::::::::::::;:;;;;::::;:::;;;::::::;;;;;;;;::clodddddddddddddlc:::::;',
        ':::::::::::::::::::::::;;;;::::::::;;;;;;;::::::::::::ccllooddddddddolc::::::::',
        '::::::::::::::::::::;;;;::::::::::::::;;;::::::::::::::::cclloodoolc:::::::::::',
        ':::::::::::::::::;;;:::::::::::::;;;;;;;::::::::::::::::::::ccc::::::::::::::::',
        '::::::::::::::::::::::::::::::;;;;;:::::::::::::::::::::::::::::::::::::::::::c',
    ], [
        'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd',
        'dddddddddddddddddddddddoollcccccllloooddddddddddddddddooooooddddddddddddddddddd',
        'ddddddddddddddddddddolc::::::::::::cccllloodddddoolcccc:::ccclloodddddddddddddd',
        'dddddddddddddddddolc:::::::::::::::::::::cclllcc:::::::::::::::cllodddddddddddd',
        'dddddddddddddddolc:::::::::::::::::::::::::::::::::::::::::::::::cllodddddddddd',
        'dddddddddddddolc::::::::::::::::::::::::::::::::::::::::::::::::::clooddddddddd',
        'ddddddddddddol::::::::::;;;;;::::::::::::::::::::::::::::::::::::::cllodddddddd',
        'dddddddddddol:::::::::;;;:::::::::::::::::::;;;;;;;;;;;;;;::::::::::ccloodddddd',
        'ddddddddddolc::::::::::::::::::::::::::::::::;;;;::::::::::::::::::::::cclloodd',
        'dddddddddol::::::::::::::::::::::;;;;;;;;;;::;;;;:::::::::::::::::;;;;;;;;:cclo',
        'ddddddddlc:::::::::::::::::::;;;;;;;;;;;;;;:::;;;;;:::::::::::;;;;;;;;;;;;;;:cl',
        'dddddol::::::::::::::::::;;;;;;;;;;::::::::::::;;;;::::::;;;;;;;;;;::::::::::::',
        'dddoc:::::::::::::::::;;;;;;;;:cloodddoooollcc:::;;;;;;;;;;;;;;::::clloddddolll',
        'dolc::::::::::::::::;;;;;;;:codxkkkkkkkkkkxxdlcccc::;;;;;;;:::cllodxkkkkkxdddxd',
        'olc::::::::::::::::::::;;:cldxkkkkkkkkkkkkxolccoddolc::::cllodxkkkkkkkkxolcldxk',
        'l:::::::::::::::::::::::::cclloddxxkkkkkkkxooodxxdolcccloxxkkkkkkkkkkkkxooooddo',
        'c::::::::::::::::::::::::::::::cclllooooooollllcc::::::clllooooooooooolllccc::c',
        '::::;;;::::::::::::::::::::::::::::::::::::::::::;;;;;:::::::::::::::::::::clod',
        ':::;;;;::::::::::::::::::::::::::::::::::::::;;;;;::::::::::::::::::;;::clodddd',
        '::;;;;;::::::::::::::::::::::::::::::::;;;;;;;;;;::::::::::;;;;;;;;;;::cloddddd',
        ':;;;;:::::::::::::;;;;;;;;;;;;;;:::::::::;;;;;;;:::::::::::::::::::::;::clloddd',
        ':::::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::::::::::::::::;;;;;;;;;:cloddd',
        ':::::::::::::;;;;::;;;,,,,,,,,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::;;:clodooo',
        ':::::::::::;;;;:;;,\'\'............\'\'\'\',,,,,,;;;;;;;;;;;;;;;;;;;;::::::cloodddooo',
        '::::::::::;;;;;;,\'.........................\'\'\'\'\'\'\',,,,;:ccccccllllloodddddddddd',
        ':::::::::;;;;;;,\'..................................\';coddddddddddddddolllcclllo',
        '::::::::;;;;;;,\'...................\'\'\'\',,,,\'\'\'\'..\';coddddddddddddolcc:;;:;;:::c',
        '::;;;;;;;;;;;,\'.................\',;;;;;;;;;;;;,,;:cloooddddddollc::;;;:::::::::',
        ';;;;;:::;;;;;,\'..............\'\',;:;;,,\'\'\'\'\'\',,,;;;::::cccccc:::;;;::clooooollcl',
        ':::::::::;;;,\'\'.............\',;:;;,\'.........\',;:cc::::::;;;::::clodddddddddddd',
        '::::::::;;;;,\'\'............\',;;;;,\'..........\';codooollllllllooddddollodddddddd',
        ':::::::::;;;,\'\'............\',;;;,,\'..........,:ldddddddddddddddddddoodddddddddd',
        '::::::::;;;;;,,\'\'.........\',,;;;,\'\'.........\',:lodddddddddddddddddddddddddddddd',
        ':::::::::;;;;;;,,,,,,,,,,,;;;;;;;;,,,,,,,,\'\',;:clllllllcccccccccccccloodddddddd',
        ':::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::::::::;;;;;;;;;;;;:clodddddooo',
        '::::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::::ccloddddlc:cl',
        '::::::::::::::::::::::::::::;:::;;;;;;;;::::::::;:::;;;;;::cllooodddddddol:::cc',
        ':::::::::::::::::::;:::::;;;::::;;::;;;:::::::::;;;;;::clodddddddddddddoc:::::;',
        '::::::::::::::::::::::::;;;::::::::;;;;;;;;:::::::::::cclooddddddddddoc::::::::',
        '::::::::::::::::::::::;;;:::::::::::::;:::::::::::::::::cclloddddddoc::::::::::',
    ]
]
