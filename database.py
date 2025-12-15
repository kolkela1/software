import sqlite3
dp=sqlite3.connect("system.db")
cr=dp.cursor()
cr.execute("PRAGMA foreign_keys = ON;")
cr.execute("create table if not exists state (id integer primary key autoincrement,name text)")
cr.execute("create table if not exists group_state (code integer primary key autoincrement,day text,hour text,state_id int,CONSTRAINT group_state_fk foreign key(state_id) references state(id))")
cr.execute("create table if not exists money_state (code integer primary key autoincrement,money real,state_id int,CONSTRAINT money_state_fk foreign key(state_id) references state(id))")
cr.execute("""create table if not exists student(
code_st integer primary key autoincrement,
name_st text not null,
phone_st text,
phone_father_st text,
group_st text not null,
gender_st text not null,
plock_st int ,
constraint ck_st check(LENGTH(phone_st)=11),
constraint ck_st2 check(gender_st in ('male','female')),
constraint ck_st23 check(plock_st in (0,1)),
constraint uq_st unique(phone_st)




)""")

cr.execute("""create table if not exists ticket (
code_t integer primary key autoincrement,
money_t real not null,
student_id int,
date text not null,
CONSTRAINT money_st_fk foreign key(student_id) references student(code_st))""")


cr.execute("""create table if not exists month(
code_m integer primary key autoincrement,
num_m int,
history text

)""")


cr.execute("""create table if not exists lisson(
code_lisson integer primary key autoincrement,
code_month_l int ,
state_l text not null,
day_l text not null,
hour_l text not null,
CONSTRAINT lisson_fk foreign key(code_month_l) references month(code_m)
)""")



cr.execute("""create table if not exists elhedore(
code_el integer primary key autoincrement,
code_l_el int ,
code_s_el int ,
num_l_el real ,
num_s_el real ,
CONSTRAINT elhedore_fk1 foreign key(code_l_el) references lisson(code_lisson),
CONSTRAINT elhedore_fk2 foreign key(code_s_el) references student(code_st)
)""")

cr.execute("""create table if not exists exam(
code_exam integer primary key autoincrement,
code_m_ex int ,
code_s_ex int,
num_exam real,
num_s_ex real,

CONSTRAINT exam_fk foreign key(code_m_ex) references month(code_m),
CONSTRAINT exam_fk2 foreign key(code_s_ex)  references student(code_st)


)""")


cr.execute("""create table if not exists pay(
code_pay integer primary key autoincrement,
name text not null,
date text not null,
money real not null


)""")


dp.commit()
dp.close()
