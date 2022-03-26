import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AboutPageComponent } from './features/components/about-page/about-page.component';
import { HomepageComponent } from './features/components/homepage/homepage.component';
import { PageNotFoundComponent } from './features/components/page-not-found/page-not-found.component';

const routes: Routes = [
  {path: '', redirectTo: 'home', pathMatch: 'full'},
  {path: 'home', component: HomepageComponent},
  {path: 'about',  component: AboutPageComponent},
  {path: "**", component: PageNotFoundComponent}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

export const routeComponents = [HomepageComponent,
                                AboutPageComponent,
                                PageNotFoundComponent];
