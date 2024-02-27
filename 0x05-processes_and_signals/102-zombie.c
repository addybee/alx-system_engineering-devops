#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
int main()
{
	pid_t cpid;
	int i;
	
	for (i = 0; i < 5; i++)
	{
		cpid = fork();
		if (cpid == -1)
		{
			return (1);
		}
		else if (cpid == 0)
			exit(0);
		else
		{
			printf("Zombie process created, PID: %d\n", cpid);
		}
	}
	infinite_while();
	return (0);
}
