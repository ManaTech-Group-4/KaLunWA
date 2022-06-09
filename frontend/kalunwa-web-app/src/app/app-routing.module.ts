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
import { AuthGuard } from './admin/helper/auth.guard';
import { DashboardComponent } from './features/components/CMS/dashboard/dashboard.component';
import { AdminTemplateComponent } from './admin/components/admin-template/admin-template.component';
import { CollectivePageListComponent } from './admin/components/collective-page-list/collective-page-list.component';
import { AddCollectiveComponent } from './admin/components/add-collective/add-collective.component';
import { SinglePageListComponent } from './features/components/CMS/single-page/single-page-list/single-page-list.component';
import { CmsHomepageComponent } from './features/components/CMS/single-page/cms-homepage/cms-homepage.component';
import { CmsOrgStructComponent } from './features/components/CMS/single-page/cms-org-struct/cms-org-struct.component';
import { NewsletterComponent } from './features/components/CMS/newsletter/newsletter.component';
import { AuditLogsComponent } from './features/components/CMS/audit-logs/audit-logs.component';
import { CmsCampComponent } from './features/components/CMS/single-page/cms-camp/cms-camp.component';
import { AdminListComponent } from './features/components/CMS/administrators/admin-list/admin-list.component';

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
  {path: "login", component: AdminHomeComponent},
  {path: "admin", component: AdminTemplateComponent, canActivate: [AuthGuard],
    children:[
      {path: '', redirectTo: 'dashboard', pathMatch:"full"},
      {path: "dashboard", component: DashboardComponent},
      {path: "single-page-list", component: SinglePageListComponent},
      {path: "cms-homepage", component: CmsHomepageComponent},
      {path: "cms-org-struct", component: CmsOrgStructComponent},
      {path: "collective", component: CollectivePageListComponent},
      {path: "collective-add-edit/:collective-type", redirectTo: "collective-add-edit/:collective-type/", pathMatch: "full" },
      {path: "collective-add-edit/:collective-type/:id", component:AddCollectiveComponent},
      {path: "newsletter", component:NewsletterComponent},
      {path: "audit", component:AuditLogsComponent},
      {path: "cms-camp/:camp-type", component:CmsCampComponent},
      {path: "admin-list", component: AdminListComponent},
    ]
  },
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
                                CmsOrgStructComponent,
                                CmsHomepageComponent,
                                NewsletterComponent,
                                AuditLogsComponent,
                                CmsCampComponent,
                                AdminListComponent,
                                CmsHomepageComponent,
                              ];
