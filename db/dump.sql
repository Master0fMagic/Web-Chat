PGDMP     ;    :                x           web-chat    12.4    12.4                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    24703    web-chat    DATABASE     �   CREATE DATABASE "web-chat" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Russian_Ukraine.1251' LC_CTYPE = 'Russian_Ukraine.1251';
    DROP DATABASE "web-chat";
                postgres    false                      0    24747    message 
   TABLE DATA           J   COPY public.message (id, text, sent_time, from_nick, to_nick) FROM stdin;
    public          postgres    false    205   �                 0    24737    user 
   TABLE DATA           G   COPY public."user" (id, nickname, password, register_time) FROM stdin;
    public          postgres    false    203   >                  0    0    message_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.message_id_seq', 6, true);
          public          postgres    false    204                       0    0    user_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('public.user_id_seq', 4, true);
          public          postgres    false    202               �   x�m�1
1E��9��d&�&�����,��F�qeQ�~ndp�e�f���8�=�ЗV�`���&�d�B#v���>�J�SC�|bGlT�8��S�/t˟}�ɹ�hV�W���刼P�Ti�T�0��5���|+\*�@��aj|�`���Q�<\i)��7b�         �   x�mͱN1E�z�S��8����h��BH4Nl�h�X���hy�ޡ�������E>]_4�v�
k�׸��޾�>m�3�Q�A�[���]!�
���9&2k�޺�ݰ�69��Ԟ�/���/O��7���Dn"a^��1#y.ʂ�T�X�`
_��y!���c�&RI�GJ���Cc     