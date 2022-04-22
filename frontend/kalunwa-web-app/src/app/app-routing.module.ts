import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AboutPageComponent } from './features/components/about-page/about-page.component';
import { HomepageComponent } from './features/components/homepage/homepage.component';
import { OrgStructureComponent } from './features/components/org-structure/org-structure.component';
import { PageNotFoundComponent } from './features/components/page-not-found/page-not-found.component';
import { IndiEventComponent } from './features/components/indi-event/indi-event.component';

export const routes: Routes = [
  {path: '', redirectTo: 'home', pathMatch: 'full'},
  {path: 'home', component: HomepageComponent},
  {path: 'about',  component: AboutPageComponent},
  {path: 'org-struct',  component: OrgStructureComponent},
  {path: "indiv-event", component: IndiEventComponent},
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
                                PageNotFoundComponent];
