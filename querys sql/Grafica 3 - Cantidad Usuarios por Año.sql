--Grafica 3: Cantidad de usuarios por año
declare @tolPersona table (
	numPersona int,
	cantidaViajes int
)

insert into @tolPersona(numPersona, cantidaViajes)
select distinct po.passenger_count, COUNT(po.passenger_count)
from dbo.[01/22GreenTrip] po
where po.passenger_count is not null and po.passenger_count!=0 and po.passenger_count<=6
group by po.passenger_count

insert into @tolPersona(numPersona, cantidaViajes)
select distinct po.passenger_count, COUNT(po.passenger_count)
from dbo.[02/22GreenTrip] po
where po.passenger_count is not null and po.passenger_count!=0 and po.passenger_count<=6
group by po.passenger_count

insert into @tolPersona(numPersona, cantidaViajes)
select distinct po.passenger_count, COUNT(po.passenger_count)
from dbo.[03/22GreenTrip] po
where po.passenger_count is not null and po.passenger_count!=0 and po.passenger_count<=6
group by po.passenger_count

insert into @tolPersona(numPersona, cantidaViajes)
select distinct po.passenger_count, COUNT(po.passenger_count)
from dbo.[04/22GreenTrip] po
where po.passenger_count is not null and po.passenger_count!=0 and po.passenger_count<=6
group by po.passenger_count

insert into @tolPersona(numPersona, cantidaViajes)
select distinct po.passenger_count, COUNT(po.passenger_count)
from dbo.[05/22GreenTrip] po
where po.passenger_count is not null and po.passenger_count!=0 and po.passenger_count<=6
group by po.passenger_count

insert into @tolPersona(numPersona, cantidaViajes)
select distinct po.passenger_count, COUNT(po.passenger_count)
from dbo.[06/22GreenTrip] po
where po.passenger_count is not null and po.passenger_count!=0 and po.passenger_count<=6
group by po.passenger_count

insert into @tolPersona(numPersona, cantidaViajes)
select distinct po.passenger_count, COUNT(po.passenger_count)
from dbo.[07/22GreenTrip] po
where po.passenger_count is not null and po.passenger_count!=0 and po.passenger_count<=6
group by po.passenger_count

insert into @tolPersona(numPersona, cantidaViajes)
select distinct po.passenger_count, COUNT(po.passenger_count)
from dbo.[08/22GreenTrip] po
where po.passenger_count is not null and po.passenger_count!=0 and po.passenger_count<=6
group by po.passenger_count

insert into @tolPersona(numPersona, cantidaViajes)
select distinct po.passenger_count, COUNT(po.passenger_count)
from dbo.[09/22GreenTrip] po
where po.passenger_count is not null and po.passenger_count!=0 and po.passenger_count<=6
group by po.passenger_count

insert into @tolPersona(numPersona, cantidaViajes)
select distinct po.passenger_count, COUNT(po.passenger_count)
from dbo.[10/22GreenTrip] po
where po.passenger_count is not null and po.passenger_count!=0 and po.passenger_count<=6
group by po.passenger_count

insert into @tolPersona(numPersona, cantidaViajes)
select distinct po.passenger_count, COUNT(po.passenger_count)
from dbo.[11/22GreenTrip] po
where po.passenger_count is not null and po.passenger_count!=0 and po.passenger_count<=6
group by po.passenger_count

insert into @tolPersona(numPersona, cantidaViajes)
select distinct po.passenger_count, COUNT(po.passenger_count)
from dbo.[12/22GreenTrip] po
where po.passenger_count is not null and po.passenger_count!=0 and po.passenger_count<=6
group by po.passenger_count

select h.numPersona as "Num. pasajeros", sum(h.cantidaViajes) as "Viajes por Num. pasajeros"
from @tolPersona h
group by h.numPersona