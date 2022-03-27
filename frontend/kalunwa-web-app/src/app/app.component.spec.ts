import { ComponentFixture, fakeAsync, TestBed, tick } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { AppComponent } from './app.component';
import{ DebugElement} from '@angular/core';
import {By} from '@angular/platform-browser';
import { NavService } from './features/service/nav.service';

describe('AppComponent', () => {

  let component: AppComponent;
  let service: NavService;
  let fixture: ComponentFixture<AppComponent>;
  let el: DebugElement;
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [
        RouterTestingModule
      ],
      declarations: [
        AppComponent
      ],
    }).compileComponents();
  });


  beforeEach(() => {
    service = new NavService();
    fixture = TestBed.createComponent(AppComponent);
    component = fixture.componentInstance;

  });


  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it(`should have as title 'kalunwa-web-app'`, () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app.title).toEqual('kalunwa-web-app');
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
});
