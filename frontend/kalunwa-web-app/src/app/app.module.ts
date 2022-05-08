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
import { BaybayonComponent } from './features/components/indiv-camps/baybayon/baybayon.component';
import { LasangComponent } from './features/components/indiv-camps/lasang/lasang.component';
import { SubaComponent } from './features/components/indiv-camps/suba/suba.component';
import { ZeroWasteComponent } from './features/components/indiv-camps/zero-waste/zero-waste.component';
import { NextDirectiveModule } from './features/shared/directives/next/next.directive';
import { PrevDirectiveModule } from './features/shared/directives/prev/prev.directive';


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
    BaybayonComponent,
    LasangComponent,
    SubaComponent,
    ZeroWasteComponent
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
    PrevDirectiveModule
  ],
  schemas: [ CUSTOM_ELEMENTS_SCHEMA ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
