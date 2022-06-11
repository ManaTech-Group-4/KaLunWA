import { DebugElement } from '@angular/core';
import { ComponentFixture, fakeAsync, TestBed, tick } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { RouterTestingModule } from '@angular/router/testing';
import { NavService } from '../../service/nav.service';

import { VisitorLandingComponent } from './visitor-landing.component';

describe('VisitorLandingComponent', () => {
  let component: VisitorLandingComponent;
  let service: NavService;
  let fixture: ComponentFixture<VisitorLandingComponent>;
  let el: DebugElement;
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [
        RouterTestingModule
      ],
      declarations: [
        VisitorLandingComponent
      ],
    }).compileComponents();
  });


  beforeEach(() => {
    service = new NavService();
    fixture = TestBed.createComponent(VisitorLandingComponent);
    component = fixture.componentInstance;

  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(VisitorLandingComponent);
    const app =  fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it('navBar is closed naturally', () => {
    expect(fixture.debugElement.query(By.css('.dropdowns'))).toBeNull();
  });

  it('navBar is opened when clicked', fakeAsync(() => {
      spyOn(component, 'onSelect');

      let button = fixture.debugElement.nativeElement.querySelector('.drop-triggers');
      button.click();

      tick();
      expect(component.whatWeDo).toBeTruthy();
  }));


  it('should set sidenav after view init to service sidenav', () => {
    component.ngAfterViewInit();
    expect(component.sidenav).toEqual(service.sidenav);
  });


  it('should close all opened dropdowns in the nav after exiting or rerouting', () => {
    component.onSelect();
    expect(component.whatWeDo).toBe(false);
  });
});
