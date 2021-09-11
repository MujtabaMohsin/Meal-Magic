PGDMP                         y         
   Meal-Magic    13.3    13.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    41181 
   Meal-Magic    DATABASE     n   CREATE DATABASE "Meal-Magic" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Arabic_Saudi Arabia.1256';
    DROP DATABASE "Meal-Magic";
                postgres    false            �            1259    41251    alembic_version    TABLE     X   CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);
 #   DROP TABLE public.alembic_version;
       public         heap    postgres    false            �            1259    41226    cuisine_id_seq    SEQUENCE        CREATE SEQUENCE public.cuisine_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;
 %   DROP SEQUENCE public.cuisine_id_seq;
       public          postgres    false            �            1259    41190    cuisine    TABLE     �   CREATE TABLE public.cuisine (
    id integer DEFAULT nextval('public.cuisine_id_seq'::regclass) NOT NULL,
    name character varying(120)
);
    DROP TABLE public.cuisine;
       public         heap    postgres    false    203            �            1259    41224    product_id_seq    SEQUENCE        CREATE SEQUENCE public.product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;
 %   DROP SEQUENCE public.product_id_seq;
       public          postgres    false            �            1259    41182    product    TABLE     5  CREATE TABLE public.product (
    description character varying(5555),
    id integer DEFAULT nextval('public.product_id_seq'::regclass) NOT NULL,
    name character varying(120),
    date_created date,
    last_updated date,
    image_url character varying(555),
    price integer,
    cuisine_id integer
);
    DROP TABLE public.product;
       public         heap    postgres    false    202            �          0    41251    alembic_version 
   TABLE DATA           6   COPY public.alembic_version (version_num) FROM stdin;
    public          postgres    false    204          �          0    41190    cuisine 
   TABLE DATA           +   COPY public.cuisine (id, name) FROM stdin;
    public          postgres    false    201   �       �          0    41182    product 
   TABLE DATA           r   COPY public.product (description, id, name, date_created, last_updated, image_url, price, cuisine_id) FROM stdin;
    public          postgres    false    200   
       �           0    0    cuisine_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.cuisine_id_seq', 38, true);
          public          postgres    false    203            �           0    0    product_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.product_id_seq', 79, true);
          public          postgres    false    202            4           2606    41255 #   alembic_version alembic_version_pkc 
   CONSTRAINT     j   ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
 M   ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
       public            postgres    false    204            2           2606    41194    cuisine cuisine_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.cuisine
    ADD CONSTRAINT cuisine_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.cuisine DROP CONSTRAINT cuisine_pkey;
       public            postgres    false    201            0           2606    41215    product product_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.product DROP CONSTRAINT product_pkey;
       public            postgres    false    200            �      x�37�H136O3MN������ *��      �   Q   x�3�t,JL�2�t���K-N�2�H-*�L��2���K1L9=Ks@,3���.sΒ�bC�.cs�	�:F��� ��      �      x��[[���u~n�
:����Ӽ�m�؝��H;�ٙٛ���H��f��,rzz�� H�$	0b���&y�_d�C$@�C�a�_�;��ݽ����>Hv���b�9�9�;�>��Z~��/�#�B5�J�X�M�.e�׎�N��}ə��e��\;�E�v�Z-�]|���Z�"�;�k)���뵈��������6�;�\:��+Y�%R�}�`�P*'Qm��#A���8��FT�t�\ϝ��K;q�뼔}g)y�u�mܦ��Q�U)q8�_�q2�8�llD�/Z���L�Uޘ=�J%|6��Zf�*�9���r��'�E6��E%��a�</!�L��(��)�R��|��U�N�Źj5����#�ڡ�lΞ��\Ԓ�͛��F8����3HAj{dG,�K:��*��/e���׻�����Ù덶/�޼i*}�� _f�!n���eS�� V�/�Wz)��`U�Y6mU(���M���g���áw�����y��A�g��an�m��hQKS�$o lQСI��((y�ll�Ĺ��9ή�xN��'#Q�;$��u���sK4��Kp�_A� [j�6�W����bݤ{�u�_�d�ZbWu[B��ԬD��8��
��6�2��բ��("Lg���(ժ��Tkd��8oR�}��I,	 ����`�J�i�Q�+t�����(�}NP��"U&t���Z����+l�n�<���N`"�]��o��)�𝀁i�x��M'�t�3b\鍆�?
���x� �wa��Jg��<�Dɚ�ȸ['EgccJ���}U�R6}��IsH�/"Q��|��vZ(�'N6~p���6�HS(�\��*Σs�#�k�&��2zH�,��j��@O[�/ '� a�d�f92�Ao�;�{����e'�d]�|)29��r�%K^\��Q���x���4/�~f>�_��/�o|mv@K�8��c���Y�ޕe)��J�Z�F�7�Ùy�Kr3# V��j��u�䐂��Mj}
�	l��NG���7k��\t�!� ��4�,� !8��nm6�U�5I٘iߩ�/*(D@�
��7 a�a�x=c���Y�\o���"�0]���Nw�.$V+���KY��x�%��խ��BC%K�*�p��py#�׫UQ��Ց���NZph�#c(�K�<�R��^���|x?�e�\��ؚ�54j) %en=�"cpT^z��,oQ����U����^Y9�G�9��ew��<���v�7����B�2�H�c�6�P_���<DkZ�ȸﰭ����x�"$��n�ގ���R�X���Q�a���r�Ao
�ӣ��1���C�خk�˲C��MU,��8Wu�G�V�k1HH�i���(��$�S(��8O(�%�oJH�$E�B���mC���ڒ�V��%|8"�\;�d��&�ZB�,v�HD?X�2"�z����YD�ԃެ���aKߟb;	�s�B<�>U�+.9~�)��a>�+��:1DR��Z���h����g��g�ʧ�1�Mk\�j:֫��V��M&��3���r��-ص AVB7�t�� ]mjv�h�Ȟ�#�
���pmI����J򽢢�WG��}��a�=|�CW�$�ڧ�!V扬q,����pD�029��]0Ha}�%�ח`�1Xʚ�O�ӹ�4�� %"�F�����%y�ph��0���1^�uQ�st��K��
�4j�쵅�
��Vs�7�`<��P��59�鎳$���*ȥf4����m���X,��;�0uqa�e���jEXW5P�Y��|�Y�^�9��/��w��,~z�:�%�����$�@����V���ұ(��������ֈ�{���o��&f}��1�b��{+U�F֮��Nf�������`��@x�8	��sKE:�x��P�?b�	��W5e
��12���9,�
�6W�[]�k%jSV�6����R�-/���k�����l�y����HVyBѪԢ�D�R9�b�A�VH� m�Lr��o� n=W�Z�N��xIZv�ćE-rx�Ja��G���F��3ʧhMvL������r�e*C.`�;y?�a��~|�$��Y���AZ��M�F'���ڀƠwHb��Q�$}�=i>8I���A��W��J\���?9����-����vrrpu��>�P��s�$I�QO�I8�H�3�"���H�&�1����5�b7Y��5%��K3T�ZVDyHgk��u�"��)�&�%�]�ŋ��3Ǣu�=���g�e)�$j�)�sĜ� Bo���5�ǥ�E�%�  #��4�@��1P��L�)/�l�e�B6��ޏ*%��PL���K��v��R�4~�f;qQ1�]��֨��DY�dtS�!�J�>y�2a{ a{a����,�����0<��{�N�g��������7��n�&7�0��[���d��3ކ���4J'�̦�N��x:��Q4#�3^p�[�0�\p%eS�]m�������N� �	<�2q�RU�\�����EH�e�����	T��.��";.</�%-r�r��aE��*6�V�p4�&�[o��R	�+�pG��kk] G�7��331��r9U;4�_qI/�7Xv����ިg��<�}H���z����O�N�����Q0u������6.��
Q�'0'd  g�@���5�t��t�QM��NrY�g5�����^N�q4J}��ğM#8N9c�L�Q%mh�ɃI[���{��"�ҖR�D�9jQ��Z���b�[R��U����&�h���@*׷� ��M)�\wqJ�i�98{�i�s:�1�C���=��)��T�5�;^�ԓủ�����gO]���'w�`�����L��p]�K��3�a|כÉ�G�P$����x�M$>�������s~tv���������(E*M�a<����]	�B>����t�ińX|N�R�� ﱆ�S=�ԥ�M,E��2$�b��h'Sg�Z��
8�[�HD`��9a��|%RG{��v5$U�(7a�=���n��xHn����鋜Z�x!��XW^_SH�C��ͨ�D�v�,�1�l.��Oz$ȿ��I�?x��<�c1�ޫ���(Z�+�V3�-����vԵ3���� I�(�{c�ˑ�cJ9��K�&�0�E3SN7��,3Q���y�5N��5�%��5�rjaxż�hA�1n��Ū�,�P\q�`ٮɽ)�f�N����Ps'���ni��"Iǥ�� ֢H)	%��@i�-��`M�2�li�P�˦ �i�.1wNj��X(ַ^�<��-�*��c��/�U|�4�`�6x6Kحh�;,;��=��H&�$I� ��P��0�+�:��F��[����I%������9�1L%��*$�K2<��:8��dc_J��e����s��s�D��
&�ғm�@ƥ�p��V�lL�h=Ȋ�� ��0�;/��Y��{�>��Ų�{խp�>�q���_�� :���ͼ�8j�68*e�.��e+%�,	X�d��j0J�ԟ$�l�d<�Fә�$�D����2�u�h�ښ;����NLrĹ���M�[�4#8�0�7��0�6���(Ȁ�Uݾ4���@�\�7��-Zg{+i�|0��bJ���$������%��bjd"�ܶ)���?�t�l�����9M���B���Zi�p����o�Dk�ٶfH�*gC�`8=x���у'��p������O����?��S���r�m��).-�}�,3ճ��A'�"O���d��(^/���E뜉�e�-b�{ۯ��U|��=���Կuo4�s������=�<���§GO��7�ë�����7LY�R1���-Ҵ�q�%���zJi3Q�,+$&�c�Z��M�:�C����UҺf�B5�Z:�X���i	$c���0��Ͷ�$g���ޕα���>��}AQg����.Ă��_����Zp�ygw��n��=>�ߝ<9<<z�����Ln�z��{j��c:�w��$X���L���ɮ|�H�=VD�)�i�k�$��R�lq3���+e� �����R\O��	R��}� �  {�}?�n�?8
�w'w߽���Y�~���M�u�Z�8YEd�4rr+�r����W���/~��O>��}��O�ӹ��Cg�鿕/�}�q�q3����>�*_�d�j_|�g��2$K�4.8�`�XGԂ�����0���n�� �l���7 )��
<QT��	��|���5<X�pî^*�3]�|mOK���}ނ��$u��&�c�E�-�;TI].�x`��<Q#h�Q+�(�ʖ.$Âj?EP'F���*��"X��Q���r�L'��{�Wל�t�,�q'
�t�*!3��)I��Ș�ǖ6؉4.jPZ��5�we��o�ؐ�GQ�I����
�C���Z��3e1�0J�1�� �q���	�{���m�w�mp��݊y��*��e@i��f���p��?�&B��Y�.��4���«�l< &���sG��%� ��ǔ������_~��?�����o���/�����Z֟��N?�U�?��������*���M	�@U*�L��x�N�YI,D��~H�t�M�|gp4�q�L�H��O��~�o�p�~8�ĵ�wM�Z
R�6�5@��6�6��m�OK�}�����ٝ,����hqӛ5��YwW�f'6� V4)a�0�.4X��֚W��mK��J�d�u6�º��u��`(*S�ݜ�T���N}�+�i���1͸n�N�k ��)��x�*:n�����y�M��x�	�*rM)�x2������,�ٳ�:��oAr������?����?�g�����gŲ��,ے�$a���N��DPS�r	��Bg.	Wy�nP	<�l>MV!�mt�/3������7�a����:t��p�i��Α�G��xw�_�~q'î��vG�m�H��õ�Y��&3p����X���K+U�E�ʳ�HF�=��¹s��=V�1����7�ɔ��p⏼�)��)�(�p���L�Q��P
X�����_�����O�O_��?8By�;������o���d/
� ������L�+v�P��O0]�]�\7V�6�,7��S��6�Q}�vAA����F�cmn��?�R���m�,�U0��p@�V��.��R9�F�V�6�#��n�ބ�W@�a��JwgRrp�������b\Ȭ���U�!�V+&��Q8��h�q0,�6�MM�����ꅈx>���#ޙ�UX�e���A)�YH�"˴-����]$\��q��C�X:�;U�9x�>.�3�b@���_2s��Q8o�;N��|)����X/Eշm��`�_`۽JN���t)b���«}�ҹOC��Fܜ�a�`�0�T��QtfJ%���c���x�"
��ft?�c_s��+�\�M)���p�(�����p��YMW�ي��k��̮#ִp�\���ie��A����b.�4t���)fPw0;��D�D�2�nh"v�� �AP�GB�dܵΨ�����P�|���# �HH�m/��M	�cc�DRc�����-AR5�B&��;�t��T^������(Z�9���-*T�-����ptp���F8r�L]�<;�ϕ�{B����`Fߘ��I�͠i$l8��SwpS��ǩe$��L��&���á�IŹj�Ǐ��'�}����z�Z�@l���nh�o�
�����Y��ܒ{
�@}k`���2'��=ςymf��*�yn:vd��?�E�����;H������\���i`��&�ȟ��ax���PD�L/V�fZ~:6�R��7K
uJk�����[ܢ�3Â~ ]��ʣ���h?5c�x�ﺔ��eJ�&Q�j�JiΏ�Aվ��Z�7h�K�e\�;������l�9]*�O8{���RR���|�d�����};�gѡ*����� w�6�.Eպ��؇�M5m�K�x��֜�j�.��t�3o�{��)UY
F�=E��dݱP,nJD��|7:H4ہc�Hke@A��mW�B�QE#.M��x�����k�7H�5p�ϴu��3�B�l)���_|�/0%�3�b��(��ɪy-��n��D%�mvNc_z��M�U۶b��� Lڕ��&_�M�$1?���KS��?|�S;�G�0U�r��LnF�,RS��:�[�C6�S�B�4��O�:��V��w��lđW�l#/��D=IX~�����C�9��æ��X����m}l��������s��\����ۯ��o�k��\�}����5׼�\�M/��.}�V(��&�
�}�ҳ�;���k i     