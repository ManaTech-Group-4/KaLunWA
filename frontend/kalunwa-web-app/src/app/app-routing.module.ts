import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AboutPageComponent } from './features/components/about-page/about-page.component';
import { HomepageComponent } from './features/components/homepage/homepage.component';
import { OrgStructureComponent } from './features/components/org-structure/org-structure.component';
import { PageNotFoundComponent } from './features/components/page-not-found/page-not-found.component';
<<<<<<< HEAD
=======
import { IndiEventComponent } from './features/components/indi-event/indi-event.component';
import { IndivProjectComponent } from './features/components/indiv-project/indiv-project.component';
import { ProjectPageComponent } from './features/components/projects/project-page/project-page.component';
import { NewsComponent } from './features/components/news/news/news.component';
import { IndivNewsComponent } from './features/components/news/indiv-news/indiv-news.component';
import { JoinUsComponent } from './features/components/join-us/join-us.component';
import { BaybayonComponent } from './features/components/indiv-camps/baybayon/baybayon.component';
import { LasangComponent } from './features/components/indiv-camps/lasang/lasang.component';
import { SubaComponent } from './features/components/indiv-camps/suba/suba.component';
import { ZeroWasteComponent } from './features/components/indiv-camps/zero-waste/zero-waste.component';
import { ContactUsComponent } from './features/components/contact-us/contact-us.component';
>>>>>>> main

export const routes: Routes = [
  {path: '', redirectTo: 'home', pathMatch: 'full'},
  {path: 'home', component: HomepageComponent},
  {path: 'about',  component: AboutPageComponent},
  {path: 'org-struct',  component: OrgStructureComponent},
<<<<<<< HEAD
=======
  {path: "indiv-event/:id", component: IndiEventComponent},
  {path: "indiv-project/:id", component: IndivProjectComponent},
  {path: 'events', component:EventsPageComponent},
  {path: 'projects', component:ProjectPageComponent},
  {path: 'news', component:NewsComponent},
  {path: "indiv-news/:id", component: IndivNewsComponent},
  {path: 'join-us', component:JoinUsComponent},
  {path: 'baybayon', component:BaybayonComponent},
  {path: 'lasang', component:LasangComponent},
  {path: 'suba', component:SubaComponent},
  {path: 'zero-waste', component:ZeroWasteComponent},
  {path: "contact-us", component: ContactUsComponent},
>>>>>>> main
  {path: "**", component: PageNotFoundComponent}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routeComponents = [HomepageComponent,
                                AboutPageComponent,
                                OrgStructureComponent,
<<<<<<< HEAD
                                PageNotFoundComponent];
=======
                                IndiEventComponent,
                                IndivProjectComponent,
                                PageNotFoundComponent,
                                EventsPageComponent,
                                ProjectPageComponent,
                                NewsComponent,
                                IndivNewsComponent,
                                JoinUsComponent,
                                BaybayonComponent,
                                LasangComponent,
                                SubaComponent,
                                ZeroWasteComponent,
                                ContactUsComponent];
>>>>>>> main
