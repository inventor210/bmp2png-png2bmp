#---------------------------------------------------------------------
#  bmp2png & png2bmp
#  makefile for gcc/gmake
#  Thanks to Gary Aviv for this file.
#  Modified for MacOSX Darwin kernel by Beau Johnston: beau@inbeta.org
#---------------------------------------------------------------------

UNAME := $(shell uname -s)

ifndef BINDIR
BINDIR  = /usr/local/bin
endif

CC      = gcc
LD      = gcc

ifndef INSTALL
INSTALL = install -s -m 755
endif
ifndef CFLAGS
CFLAGS  = -O2 -g -Wall
endif

ifeq ($(UNAME),Darwin)
LIBS    = -framework libpng -lz -lm
else
LIBS    = -lpng -lz -lm
endif

B2POBJ  = bmp2png.o common.o
P2BOBJ  = png2bmp.o common.o


all : bmp2png png2bmp

bmp2png : $(B2POBJ)
	$(LD) $(LDFLAGS) -o bmp2png $(B2POBJ) $(LIBS)

png2bmp : $(P2BOBJ)
	$(LD) $(LDFLAGS) -o png2bmp $(P2BOBJ) $(LIBS)

%.o : %.c
	$(CC) $(CFLAGS) -c -o $@ $<

install :
	$(INSTALL) bmp2png png2bmp $(BINDIR)

uninstall :
	rm -f $(BINDIR)/bmp2png $(BINDIR)/png2bmp

clean :
	rm -f $(B2POBJ) $(P2BOBJ) bmp2png png2bmp

bmp2png.o : bmp2png.c common.h bmphed.h
png2bmp.o : png2bmp.c common.h bmphed.h
common.o  : common.c  common.h

