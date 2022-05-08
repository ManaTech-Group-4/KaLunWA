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
import { FilterDialogComponent } from './features/dialog/filter-dialog/filter-dialog.component';
import { FormsModule, ReactiveFormsModule} from '@angular/forms';
import { FilterProjectsDialogComponent } from './features/dialog/filter-projects-dialog/filter-projects-dialog.component';
import { MatDialogModule } from '@angular/material/dialog';
import { MembersDialogComponent } from './features/components/members-dialog/members-dialog.component';
import { IndiEventComponent } from './features/components/indi-event/indi-event.component';
import { IndivProjectComponent } from './features/components/indiv-project/indiv-project.component';
import { JoinUsComponent } from './features/components/join-us/join-us.component';
import { ContactUsComponent } from './features/components/contact-us/contact-us.component';

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
    FilterDialogComponent,
    FilterProjectsDialogComponent,
    JoinUsComponent,
    ContactUsComponent,
    MembersDialogComponent,
    FilterProjectsDialogComponent,
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
    ReactiveFormsModule,
    FormsModule,
    MatDialogModule,

    MatCarouselModule.forRoot()
  ],
  schemas: [ CUSTOM_ELEMENTS_SCHEMA ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
