# Quebec Emergency Room Weekly Occupancy

**Source:** https://sante.handled.tools/en/hebdo

---

The ministry’s ER file only ever shows the current hour. We’ve been saving every hour of it since August 10 for the Urgences Québec app, so here it is rolled up by week (Monday to Sunday). The bars are the average stretcher occupancy across every ER and every hour they reported; over 100% means more people on stretchers than there are stretchers.

(an ER needs at least 84 reported hours that week to make the list)

hebdo-quebec.csv — one row per week, all of Quebec (13)

hebdo-urgences.csv — one row per ER per week (1,560)

Both files rebuild every week. Hourly raw data is on GitHub if you want it.

CC BY 4.0 , so use it in a story, a thesis, whatever. The underlying MSSS data on Données Québec is under the same licence. If you use it, credit “MSSS, compiled by the Urgences Québec app (sante.handled.tools/en/hebdo)”.

A couple of caveats. Occupancy is crowding, not how long you’ll wait, triage takes the sickest first. Six hospitals don’t report anything and are left out. Week one starts August 10 at 2 pm because that’s when we started.
