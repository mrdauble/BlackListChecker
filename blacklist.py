import urllib3, argparse, dns.resolver

http = urllib3.PoolManager()


def checkblacklist(ip):
    blserver = ["access.redhawk.org",
"all.s5h.net",
"b.barracudacentral.org",
"bl.spamcop.net",
"bl.tiopan.com",
 "blackholes.wirehub.net",
 "blacklist.sci.kun.nl",	
 "block.dnsbl.sorbs.net",
 "blocked.hilli.dk",
 "bogons.cymru.com",
 "dnsbl.spfbl.net",
"cbl.abuseat.org",
 "dev.null.dk",	
 "dialup.blacklist.jippg.org",
 "dialups.mail-abuse.org",	
 "dialups.visi.com",
 "dnsbl.abuse.ch",	
 "dnsbl.anticaptcha.net",
 "dnsbl.antispam.or.id",	
 "dnsbl.dronebl.org",
 "dnsbl.justspam.org",	
 "dnsbl.kempt.net",
 "dnsbl.sorbs.net",	
 "dnsbl.tornevall.org",
 "dnsbl-1.uceprotect.net",	
 "duinv.aupads.org",
 "dnsbl-2.uceprotect.net",	
 "dnsbl-3.uceprotect.net",
 "dul.dnsbl.sorbs.net",	
 "escalations.dnsbl.sorbs.net",
 "hil.habeas.com", 
"black.junkemailfilter.com",
 "http.dnsbl.sorbs.net",	 
"intruders.docs.uu.se",
 "ips.backscatterer.org",	
 "korea.services.net",
 "mail-abuse.blacklist.jippg.org",	
 "misc.dnsbl.sorbs.net",
 "msgid.bl.gweep.ca",	
 "new.dnsbl.sorbs.net",
 "no-more-funn.moensted.dk",	
 "old.dnsbl.sorbs.net",
 "opm.tornevall.org",
 "pbl.spamhaus.org",
 "proxy.bl.gweep.ca",	
 "psbl.surriel.com",
 "pss.spambusters.org.ar",	 
"rbl.schulte.org",
 "rbl.snark.net",	 
"recent.dnsbl.sorbs.net",
 "relays.bl.gweep.ca",	
 "relays.mail-abuse.org",
 "relays.nether.net",	
 "rsbl.aupads.org",
 "sbl.spamhaus.org",	
 "smtp.dnsbl.sorbs.net",
 "socks.dnsbl.sorbs.net",	
 "spam.dnsbl.sorbs.net",
 "spam.olsentech.net",	
 "spamguard.leadmon.net",
 "spamsources.fabel.dk",	
 "ubl.unsubscore.com",
 "web.dnsbl.sorbs.net",	
 "xbl.spamhaus.org",
 "zen.spamhaus.org",
 "zombie.dnsbl.sorbs.net",
 "dnsbl.inps.de",
"bl.mailspike.net",
 "all.s5h.net",	
 "b.barracudacentral.org",	
 "bl.spamcop.net",
 "blacklist.woody.ch",	
 "bogons.cymru.com",	
 "cbl.abuseat.org",
 "combined.abuse.ch",	
 "db.wpbl.info",	
 "dnsbl-1.uceprotect.net",
 "dnsbl-2.uceprotect.net",
"dnsbl-3.uceprotect.net",	 
"dnsbl.anticaptcha.net",
 "dnsbl.dronebl.org",	
 "dnsbl.inps.de",	
 "dnsbl.sorbs.net",
 "dnsbl.spfbl.net",	
 "drone.abuse.ch",
 "dyna.spamrats.com",	
 "dynip.rothen.com",
 "http.dnsbl.sorbs.net",	
 "ix.dnsbl.manitu.net",
 "korea.services.net",	
 "misc.dnsbl.sorbs.net",	
 "noptr.spamrats.com",
 "orvedb.aupads.org",	
 "pbl.spamhaus.org",	
 "proxy.bl.gweep.ca",
 "psbl.surriel.com",	
 "relays.nether.net",
 "singular.ttk.pte.hu",	
 "spam.abuse.ch",	
 "spam.dnsbl.anonmails.de",
 "spam.dnsbl.sorbs.net",	
 "spam.spamrats.com",	
 "spambot.bls.digibase.ca",
 "spamrbl.imp.ch",	
 "ubl.lashback.com",
 "ubl.unsubscore.com",	
 "virus.rbl.jp",	
 "web.dnsbl.sorbs.net",
 "wormrbl.imp.ch",	
 "xbl.spamhaus.org",	
 "z.mailspike.net",
"zombie.dnsbl.sorbs.net",	]

    GOOD = []
    BAD = []
    total = 0
    failed = 0
    for bl in blserver:

        try:
            my_resolver = dns.resolver.Resolver()
            query = '.'.join(reversed(str(ip).split("."))) + "." + bl
            my_resolver.timeout = 5
            my_resolver.lifetime = 5
            answers = my_resolver.query(query, "A")
            answer_txt = my_resolver.query(query, "TXT")
            BAD.append("Blacklisted at %s : %s" % (bl, answer_txt[0]))
            total = total + 1

        except dns.resolver.NXDOMAIN:
            GOOD.append(bl)
            total = total + 1

        except dns.resolver.Timeout:
            failed = failed + 1

        except dns.resolver.NoNameservers:
            failed = failed + 1

        except dns.resolver.NoAnswer:
            failed = failed + 1

    print("Black-List report for IP {0}".format(ip))
    print("White Listed in %d" % (len(GOOD)))
    print("Black Listed in %d" % (len(BAD)))
    for i in BAD:
        print(i)
    print("Failed in %d" % (failed))


if __name__ == "__main__":
    iplists = []
    print("IP Black-List Check Başlatılıyor")
    parser = argparse.ArgumentParser(description='IP Black-List Checker - GG')
    parser.add_argument('-i', '--ip', help='IP address to check-(Kontrol edilecek IP adresi)')
    parser.add_argument('-f', '--file', help='IP address to check(Kontrol edilecek IP adresleri bir txt içinde alt alta olması lazım)')
    parser.add_argument('--success', help='Also display GOOD', required=False, action="store_true")
    args = parser.parse_args()
    if args is not None and args.ip is not None and len(args.ip) > 0:
        badip = args.ip
        iplists.append(badip)
    else:
        if args is not None and args.file is not None and len(args.file) > 0:
            for i in open(args.file):
                iplists.append(i.rstrip())
        else:
            my_ip = http.request('GET', 'http://icanhazip.com').data.rstrip().decode("utf-8")
            print('IP adresiniz: %s\n' % (my_ip))
            # Get IP To Check
            resp = input('Kontrol etmek ister misin {0} ? (Y/N):'.format(my_ip))
            if resp.lower() in ["yes", "y"]:
                badip = my_ip
            else:
                badip = input(blue("\nHangi IP'yi kontrol etmek istersiniz?: "))
                if badip is None or badip == "":
                    sys.exit("Kontrol edilecek IP adresi yok.")
            iplists.append(badip)
    for i in iplists:
        checkblacklist(i)
