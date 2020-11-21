#include "uuid_cbr.h"


char *generate(int *err)
{
	//Инициализация модуля генерации УИД.
    if(!uid_init())
    {
		//Если инициализация не удалась, функция генерации УИД
		//не будет возвращать корректный результат
		*err = 1;
	}

    //буфер для УИД
    char buf[UID_BUFFER_SIZE];
    char *data = NULL;
		//Создание УИД
		if(uid_create(buf))
		{
		 data = calloc(UID_BUFFER_SIZE,sizeof(char));
            if(data != NULL)
            {
                strncpy(data,buf,UID_BUFFER_SIZE);
            }
            else
            {
                *err = 2;
            }

		 }
		 else
		 {
		    *err = 3;
		 }


    //Деинициализация модуля генерации УИД
    //(освобождение выделенных ресурсов)
    uid_deinit();

    return data;
}

char *err_string(int err)
{
    switch(err){
    case 1:return "Error initialization uuid library";
    case 2:return "Error allocate memory buffer";
    case 3:return "Error create uuid";
    default:return "unknown error";
    }
}