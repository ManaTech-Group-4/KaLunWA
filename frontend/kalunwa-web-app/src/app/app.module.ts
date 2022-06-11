import { BrowserModule } from '@angular/platform-browser';
import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { MatDesignModule } from './features/shared/mat-design.module';
import { AppRoutingModule, routeComponents } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavBarComponent } from './features/components/nav-bar/nav-bar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { JumbotronComponent } from './features/components/jumbotron/jumbotron.component';
import { MatCarouselModule } from '@ngmodule/material-carousel';
import { FooterComponent } from './features/components/footer/footer.component';
import { AboutCampComponent } from './features/components/about-camp/about-camp.component';
import { HttpClientModule } from '@angular/common/http';
import { OrgStructureComponent } from './features/components/org-structure/org-structure.component';
import { EventsPageComponent } from './features/components/events-page/events-page.component';
import { EventPageListComponent } from './features/components/event-page-list/event-page-list.component';
import { ProjectPageComponent } from './features/components/projects/project-page/project-page.component';
import { ProjectListComponent } from './features/components/projects/project-list/project-list.component';
import { FilterDialogComponent } from './features/dialog/filter-dialog/filter-dialog.component';
import { FormsModule, ReactiveFormsModule} from '@angular/forms';
import { FilterProjectsDialogComponent } from './features/dialog/filter-projects-dialog/filter-projects-dialog.component';
import { MatDialogModule } from '@angular/material/dialog';
import { MembersDialogComponent } from './features/components/members-dialog/members-dialog.component';
import { IndiEventComponent } from './features/components/indi-event/indi-event.component';
import { IndivProjectComponent } from './features/components/indiv-project/indiv-project.component';
import { NewsComponent } from './features/components/news/news/news.component';
import { NewsListComponent } from './features/components/news/news-list/news-list.component';
import { IndivNewsComponent } from './features/components/news/indiv-news/indiv-news.component';
import { JoinUsComponent } from './features/components/join-us/join-us.component';
import { BaybayonComponent } from './features/components/indiv-camps/baybayon/baybayon.component';
import { LasangComponent } from './features/components/indiv-camps/lasang/lasang.component';
import { SubaComponent } from './features/components/indiv-camps/suba/suba.component';
import { ZeroWasteComponent } from './features/components/indiv-camps/zero-waste/zero-waste.component';
import { NextDirectiveModule } from './features/shared/directives/next/next.directive';
import { PrevDirectiveModule } from './features/shared/directives/prev/prev.directive';
import { ContactUsComponent } from './features/components/contact-us/contact-us.component';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatDividerModule} from '@angular/material/divider';
import { MatListModule} from '@angular/material/list';
import { DashboardComponent } from './features/components/CMS/dashboard/dashboard.component';
import { HeaderComponent } from './features/components/CMS/header/header.component';
import { SidenavComponent } from './features/components/CMS/sidenav/sidenav.component';
import { AppPaginationComponent } from './features/components/app-pagination/app-pagination.component';
import { SinglePageListComponent } from './features/components/CMS/single-page/single-page-list/single-page-list.component';
import { AdminHomeComponent } from './admin/components/admin-home/admin-home.component';
import { VisitorLandingComponent } from './features/components/visitor-landing/visitor-landing.component';
import { CmsHomepageComponent } from './features/components/CMS/single-page/cms-homepage/cms-homepage.component';
import { CmsOrgStructComponent } from 'src/app/features/components/CMS/single-page/cms-org-struct/cms-org-struct.component';
import { AdminTemplateComponent } from './admin/components/admin-template/admin-template.component';
import { CollectivePageListComponent } from './admin/components/collective-page-list/collective-page-list.component';
import { AddCollectiveComponent } from './admin/components/add-collective/add-collective.component';
import { NewsletterComponent } from './features/components/CMS/newsletter/newsletter.component';
import { AuditLogsComponent } from './features/components/CMS/audit-logs/audit-logs.component';
import { CmsCampComponent } from 'src/app/features/components/CMS/single-page/cms-camp/cms-camp.component';
import { AdminListComponent } from './features/components/CMS/administrators/admin-list/admin-list.component';


@NgModule({
  declarations: [
    AppComponent,
    NavBarComponent,
    JumbotronComponent,
    FooterComponent,
    AboutCampComponent,
    routeComponents,
    OrgStructureComponent,
    MembersDialogComponent,
    IndiEventComponent,
    IndivProjectComponent,
    EventsPageComponent,
    EventPageListComponent,
    ProjectPageComponent,
    ProjectListComponent,
    FilterDialogComponent,
    FilterProjectsDialogComponent,
    MembersDialogComponent,
    FilterProjectsDialogComponent,
    NewsComponent,
    NewsListComponent,
    IndivNewsComponent,
    JoinUsComponent,
    BaybayonComponent,
    LasangComponent,
    SubaComponent,
    ZeroWasteComponent,
    ContactUsComponent,
    DashboardComponent,
    HeaderComponent,
    SidenavComponent,
    AppPaginationComponent,
    AdminHomeComponent,
    SinglePageListComponent,
    VisitorLandingComponent,
    CmsOrgStructComponent,
    CmsHomepageComponent,
    AdminTemplateComponent,
    CollectivePageListComponent,
    AddCollectiveComponent,
    NewsletterComponent,
    AuditLogsComponent,
    CmsCampComponent,
    AdminListComponent,
  ],
  entryComponents:[
    MembersDialogComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatDesignModule,
    HttpClientModule,
    MatCarouselModule.forRoot(),
    ReactiveFormsModule,
    FormsModule,
    MatDialogModule,
    NextDirectiveModule,
    PrevDirectiveModule,
    MatSidenavModule,
    MatToolbarModule,
    MatIconModule,
    MatDividerModule,
    MatListModule
  ],
  schemas: [ CUSTOM_ELEMENTS_SCHEMA ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
