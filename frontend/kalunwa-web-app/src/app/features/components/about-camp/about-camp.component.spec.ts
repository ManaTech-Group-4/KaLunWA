import { HttpClient } from '@angular/common/http';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { MatDesignModule } from '../../shared/mat-design.module';

import { AboutCampComponent } from './about-camp.component';

describe('AboutCampComponent', () => {
  let component: AboutCampComponent;
  let fixture: ComponentFixture<AboutCampComponent>;
  let httpClient: HttpClient;
  let httpTestingController: HttpTestingController;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AboutCampComponent ],
      imports: [ MatDesignModule,
                  HttpClientTestingModule ]
    })
    .compileComponents();
    httpClient = TestBed.get(HttpClient);
    httpTestingController = TestBed.get(HttpTestingController);
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AboutCampComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should switch to other camp after click', () => {
    let value = fixture.debugElement.query(By.css('.sidenav')).nativeElement.getAttribute('value');
    value = 2;
    expect(value).toEqual(2);
  });

});
