import { HttpClientTestingModule,} from '@angular/common/http/testing';
import { ComponentFixture, inject, TestBed } from '@angular/core/testing';
import { AboutpageService } from '../../service/aboutpage.service';

import { AboutPageComponent } from './about-page.component';

describe('AboutPageComponent', () => {
  let component: AboutPageComponent;
  let fixture: ComponentFixture<AboutPageComponent>;
  let testBedService : AboutpageService;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AboutPageComponent ],
      imports : [ HttpClientTestingModule ],
      providers: [AboutpageService]

    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AboutPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();

    testBedService = TestBed.get(AboutpageService);
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });


  it('Service injected via inject() and TestBed.get() should be the same (AboutpageService)',
    inject([AboutpageService], (injectService: AboutpageService) => {
      expect(injectService).toBe(testBedService);
  }));
});
