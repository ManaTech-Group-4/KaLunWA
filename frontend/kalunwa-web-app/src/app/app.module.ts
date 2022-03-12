import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { MatDesignModule } from './features/shared/mat-design.module';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavBarComponent } from './features/components/nav-bar/nav-bar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { JumbotronComponent } from './features/components/jumbotron/jumbotron.component';
import { MatCarouselModule } from '@ngmodule/material-carousel';
import { HomepageComponent } from './features/components/homepage/homepage.component';

@NgModule({
  declarations: [
    AppComponent,
    NavBarComponent,
    JumbotronComponent,
    HomepageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatDesignModule,
    MatCarouselModule.forRoot()

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
