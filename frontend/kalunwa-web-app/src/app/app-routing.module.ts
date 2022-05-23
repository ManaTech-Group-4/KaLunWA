import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AboutPageComponent } from './features/components/about-page/about-page.component';
import { HomepageComponent } from './features/components/homepage/homepage.component';
import { OrgStructureComponent } from './features/components/org-structure/org-structure.component';
import { PageNotFoundComponent } from './features/components/page-not-found/page-not-found.component';
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
import { AdminHomeComponent } from './admin/components/admin-home/admin-home.component';
import { VisitorLandingComponent } from './features/components/visitor-landing/visitor-landing.component';
import { AuthGuard } from './admin/auth.guard';
import { DashboardComponent } from './features/components/CMS/dashboard/dashboard.component';
import { SinglePageListComponent } from './features/components/CMS/single-page/single-page-list/single-page-list.component';

export const routes: Routes = [
  {path: '', component: VisitorLandingComponent,
  children:[
    {path: '', redirectTo: 'home', pathMatch:"full"},
    {path: 'home', component: HomepageComponent},
    {path: "admin-login", component: AdminHomeComponent},
    {path: 'about',  component: AboutPageComponent},
    {path: 'org-struct',  component: OrgStructureComponent},
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
    {path: "contact-us", component: ContactUsComponent}]},
  {path: "admin", component: AdminHomeComponent},
  {path: "dashboard", component: DashboardComponent, canActivate: [AuthGuard]},
  {path: "single-page-list", component: SinglePageListComponent},
  {path: "**", component: PageNotFoundComponent}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
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
                                NewsComponent,
                                IndivNewsComponent,
                                JoinUsComponent,
                                BaybayonComponent,
                                LasangComponent,
                                SubaComponent,
                                ZeroWasteComponent,
                                ContactUsComponent,
                                AdminHomeComponent,
                                DashboardComponent,
                                SinglePageListComponent,
                              ];
