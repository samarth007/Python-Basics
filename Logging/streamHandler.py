import logging as lg

lg.basicConfig(filename='stream.log',level=lg.INFO)
console_log=lg.StreamHandler()
console_log.setLevel(lg.INFO)
format='%(asctime)s %(levelname)s %(message)s'
console_log.setFormatter(format)
lg.getLogger('').addHandler(console_log)
log1=lg.getLogger('Logger1')
log2=lg.getLogger('Logger2')
log1.info("log1111")
log2.debug("debug log222")  #debug is not logged
log2.info('log22222')