import { ComponentFixture, inject, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { HomepageComponent } from './homepage.component';
import { HomepageService } from '../../service/homepage.service';

describe('HomepageComponent', () => {
  let component: HomepageComponent;
  let fixture: ComponentFixture<HomepageComponent>;
  let testBedService : HomepageService;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HomepageComponent ],
      imports : [ HttpClientTestingModule ],
      providers: [HomepageService]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HomepageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();

    testBedService = TestBed.get(HomepageService);
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('Service injected via inject() and TestBed.get() should be the same instance (HomepageService)',
    inject([HomepageService], (injectService: HomepageService) => {
      expect(injectService).toBe(testBedService);
  }));
});
