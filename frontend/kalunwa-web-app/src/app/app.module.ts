import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
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

@NgModule({
  declarations: [
    AppComponent,
    NavBarComponent,
    JumbotronComponent,
    FooterComponent,
    routeComponents,
    AboutCampComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatDesignModule,
    MatCarouselModule.forRoot(),
    HttpClientModule

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
