import { Location } from "@angular/common";
import { TestBed, fakeAsync, tick } from "@angular/core/testing";
import { RouterTestingModule } from "@angular/router/testing";
import { ActivatedRoute, Router} from "@angular/router";

import { routes } from "./app-routing.module";
import { HomepageComponent } from "./features/components/homepage/homepage.component";
import { AboutPageComponent } from "./features/components/about-page/about-page.component";
import { OrgStructureComponent } from "./features/components/org-structure/org-structure.component";
import { PageNotFoundComponent } from "./features/components/page-not-found/page-not-found.component";
import { AppComponent } from "./app.component";
import { HttpClientTestingModule } from "@angular/common/http/testing";
import { MatDialog, MatDialogModule, MatDialogRef, MAT_DIALOG_DATA } from "@angular/material/dialog";

describe('Router: App', () => {

  let location: Location;
  let router: Router;
  let fixture;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports:[RouterTestingModule.withRoutes(routes), HttpClientTestingModule, MatDialogModule],
      declarations: [
        HomepageComponent,
        AboutPageComponent,
        OrgStructureComponent,
        PageNotFoundComponent,
        AppComponent
      ],
    });

    router = TestBed.get(Router);
    location = TestBed.get(Location);
    fixture = TestBed.createComponent(AppComponent);
    router.initialNavigation();
  });


  it('navigate to "" redirects you to /home', fakeAsync(() => {
    router.navigate(['']);
    tick();
    expect(location.path()).toBe('/home');
  }));

  it('navigate to "about" takes you to /about', fakeAsync(() => {
    router.navigate(['about']);
    tick();
    expect(location.path()).toBe('/about');
  }));

  it('navigate to "org-struct" takes you to /org-struct', fakeAsync(() => {
    router.navigate(['org-struct']);
    tick();
    expect(location.path()).toBe('/org-struct');
  }));

});
