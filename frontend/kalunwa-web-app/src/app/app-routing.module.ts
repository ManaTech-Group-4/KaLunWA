import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AboutPageComponent } from './features/components/about-page/about-page.component';
import { EventsPageComponent } from './features/components/events-page/events-page.component';
import { HomepageComponent } from './features/components/homepage/homepage.component';
import { OrgStructureComponent } from './features/components/org-structure/org-structure.component';
import { PageNotFoundComponent } from './features/components/page-not-found/page-not-found.component';
import { IndiEventComponent } from './features/components/indi-event/indi-event.component';
import { IndivProjectComponent } from './features/components/indiv-project/indiv-project.component';
import { ProjectPageComponent } from './features/components/projects/project-page/project-page.component';
import { BaybayonComponent } from './features/components/indiv-camps/baybayon/baybayon.component';
import { SubaComponent } from './features/components/indiv-camps/suba/suba.component';
import { ZeroWasteComponent } from './features/components/indiv-camps/zero-waste/zero-waste.component';
import { LasangComponent } from './features/components/indiv-camps/lasang/lasang.component';
import { JoinUsComponent } from './features/components/join-us/join-us.component';

export const routes: Routes = [
  {path: '', redirectTo: 'home', pathMatch: 'full'},
  {path: 'home', component: HomepageComponent},
  {path: 'about',  component: AboutPageComponent},
  {path: 'org-struct',  component: OrgStructureComponent},
  {path: "indiv-event", component: IndiEventComponent},
  {path: "indiv-project", component: IndivProjectComponent},
  {path: 'events', component:EventsPageComponent},
  {path: 'projects', component:ProjectPageComponent},
  {path: 'baybayon', component:BaybayonComponent},
  {path: 'suba', component:SubaComponent},
  {path: 'lasang', component:LasangComponent},
  {path: 'zero-waste', component:ZeroWasteComponent},
  {path: 'join-us', component:JoinUsComponent},
  {path: "**", component: PageNotFoundComponent}];

@NgModule({
  imports: [RouterModule.forRoot(routes, {scrollPositionRestoration: 'enabled'})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routeComponents = [HomepageComponent,
                                AboutPageComponent,
                                OrgStructureComponent,
                                IndiEventComponent,
                                IndivProjectComponent,
                                PageNotFoundComponent,
                                EventsPageComponent,
                                ProjectPageComponent,
                                BaybayonComponent,
                                SubaComponent,
                                LasangComponent,
                                ZeroWasteComponent,
                                JoinUsComponent];
