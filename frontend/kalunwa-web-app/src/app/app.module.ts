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
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import { FilterProjectsDialogComponent } from './features/dialog/filter-projects-dialog/filter-projects-dialog.component';
import { MatDialogModule } from '@angular/material/dialog';
import { MembersDialogComponent } from './features/components/members-dialog/members-dialog.component';
import { IndiEventComponent } from './features/components/indi-event/indi-event.component';
import { NgImageSliderModule } from 'ng-image-slider';

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
    IndiEventComponent
    EventsPageComponent,
    EventPageListComponent,
    ProjectPageComponent,
    ProjectListComponent,
    FilterDialogComponent,
    FilterProjectsDialogComponent
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
    FormsModule
    MatDialogModule,
    NgImageSliderModule,

    MatCarouselModule.forRoot()
  ],
  schemas: [ CUSTOM_ELEMENTS_SCHEMA ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
