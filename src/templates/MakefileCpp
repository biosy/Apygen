CC = g++
CFLAGS = -W -Wall -g
LDFLAGS = 
 
SRC = $(wildcard *.cpp)
OBJS = $(SRC:.cpp=.o)
AOUT = prog
 
all : $(AOUT) 
 
prog : $(OBJS)
	$(CC) $(LDFLAGS) -o $@ $^
%.o : %.cpp
	$(CC) $(CFLAGS) -o $@ -c $<
clean :
	@rm *.o
cleaner : clean
	@rm $(AOUT)
