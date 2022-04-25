import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { ComponentFixture, inject, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { AboutpageService } from '../../service/aboutpage.service';
import { MatDesignModule } from '../../shared/mat-design.module';
import { AboutCampModel } from '../../models/about-camp-model';
import { AboutCampComponent } from './about-camp.component';
import { of } from 'rxjs/internal/observable/of';

  const mockData: AboutCampModel[] = [
    {'camp_name': 'Baybayon',
      'description': 'asd',
      'camp_image' : 'image1',
      'camp_leader': {'name':'Juan Tamad', 'image': 'image_profile', 'motto': 'you are my fire'}},
    {'camp_name': 'Lasang',
      'description': 'asd',
      'camp_image' : 'image1',
      'camp_leader': {'name':'Juan Tamad', 'image': 'image_profile', 'motto': 'you are my fire'}},
    {'camp_name': 'Suba',
      'description': 'asd',
      'camp_image' : 'image1',
      'camp_leader':  {'name':'Juan Tamad', 'image': 'image_profile', 'motto': 'you are my fire'}}
  ];

describe('AboutCampComponent', () => {
  let component: AboutCampComponent;
  let fixture: ComponentFixture<AboutCampComponent>;
  let testBedService : AboutpageService;
  let mockCamps = mockData;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AboutCampComponent ],
      imports: [ MatDesignModule,
                  HttpClientTestingModule ],
      providers: [AboutpageService]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AboutCampComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();

    testBedService = TestBed.get(AboutpageService);
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should switch to other camp after click', () => {
    let value = fixture.debugElement.query(By.css('.sidenav')).nativeElement.getAttribute('value');
    value = 2;
    expect(value).toEqual(2);
  });


  it('Service injected via inject() and TestBed.get() should be the same (AboutpageService)',
    inject([AboutpageService], (injectService: AboutpageService) => {
      expect(injectService).toBe(testBedService);
  }));

  it('switch to the display camp',() => {
    component.ngOnInit();
    const mockRetrieve$ = of(mockCamps);
    component.onSelect(1);
    mockRetrieve$.subscribe((camps)=>{
        expect(camps[1].camp_name).toEqual(component.displayCamp.camp_name);
      });
  });
});
