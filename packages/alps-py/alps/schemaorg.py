from .descriptors import Semantic


# noinspection PyPep8,SpellCheckingInspection
class SchemaOrg:

    NEWS_MEDIA_ORGANIZATION = Semantic(
        id="NewsMediaOrganization",
        ref="schema:NewsMediaOrganization",
        text="""A News/Media organization such as a newspaper or TV station.""",
    )

    PLAN_ACTION = Semantic(
        id="PlanAction",
        ref="schema:PlanAction",
        text="""The act of planning the execution of an event/task/action/reservation/plan to a future date.""",
    )

    GEO_MIDPOINT = Semantic(
        id="geoMidpoint",
        ref="schema:geoMidpoint",
        text="""Indicates the GeoCoordinates at the centre of a GeoShape e.g. GeoCircle.""",
    )

    NONPROFIT501C2 = Semantic(
        id="Nonprofit501c2",
        ref="schema:Nonprofit501c2",
        text="""Nonprofit501c2: Non-profit type referring to Title-holding Corporations for Exempt Organizations.""",
    )

    CHARACTER_NAME = Semantic(
        id="characterName",
        ref="schema:characterName",
        text="""The name of a character played in some acting or performing role, i.e. in a PerformanceRole.""",
    )

    EVENT_CANCELLED = Semantic(
        id="EventCancelled",
        ref="schema:EventCancelled",
        text="""The event has been cancelled. If the event has multiple startDate values, all are assumed to be cancelled. Either startDate or previousStartDate may be used to specify the event\'s cancelled date(s).""",
    )

    CALORIES = Semantic(
        id="calories", ref="schema:calories", text="""The number of calories."""
    )

    MENU_ADD_ON = Semantic(
        id="menuAddOn",
        ref="schema:menuAddOn",
        text="""Additional menu item(s) such as a side dish of salad or side order of fries that can be added to this menu item. Additionally it can be a menu section containing allowed add-on menu items for this menu item.""",
    )

    SIZE_SYSTEM = Semantic(
        id="sizeSystem",
        ref="schema:sizeSystem",
        text="""The size system used to identify a product\'s size. Typically either a standard (for example, "GS1" or "ISO-EN13402"), country code (for example "US" or "JP"), or a measuring system (for example "Metric" or "Imperial").""",
    )

    CODE_REPOSITORY = Semantic(
        id="codeRepository",
        ref="schema:codeRepository",
        text="""Link to the repository where the un-compiled, human readable code and related code is located (SVN, github, CodePlex).""",
    )

    GEO = Semantic(
        id="geo", ref="schema:geo", text="""The geo coordinates of the place."""
    )

    POST_OP = Semantic(
        id="postOp",
        ref="schema:postOp",
        text="""A description of the postoperative procedures, care, and/or followups for this device.""",
    )

    BODY_MEASUREMENT_HEAD = Semantic(
        id="BodyMeasurementHead",
        ref="schema:BodyMeasurementHead",
        text="""Maximum girth of head above the ears. Used, for example, to fit hats.""",
    )

    BROADCAST_CHANNEL_ID = Semantic(
        id="broadcastChannelId",
        ref="schema:broadcastChannelId",
        text="""The unique address by which the BroadcastService can be identified in a provider lineup. In US, this is typically a number.""",
    )

    SIGNIFICANT_LINK = Semantic(
        id="significantLink",
        ref="schema:significantLink",
        text="""One of the more significant URLs on the page. Typically, these are the non-navigation links that are clicked on the most.""",
    )

    LISTEN_ACTION = Semantic(
        id="ListenAction",
        ref="schema:ListenAction",
        text="""The act of consuming audio content.""",
    )

    PART_OF_SEASON = Semantic(
        id="partOfSeason",
        ref="schema:partOfSeason",
        text="""The season to which this episode belongs.""",
    )

    BIO_CHEM_SIMILARITY = Semantic(
        id="bioChemSimilarity",
        ref="schema:bioChemSimilarity",
        text="""A similar BioChemEntity, e.g., obtained by fingerprint similarity algorithms.""",
    )

    TRADE_ACTION = Semantic(
        id="TradeAction",
        ref="schema:TradeAction",
        text="""The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.""",
    )

    PATTERN = Semantic(
        id="pattern",
        ref="schema:pattern",
        text="""A pattern that something has, for example \'polka dot\', \'striped\', \'Canadian flag\'. Values are typically expressed as text, although links to controlled value schemes are also supported.""",
    )

    UROLOGIC = Semantic(
        id="Urologic",
        ref="schema:Urologic",
        text="""A specific branch of medical science that is concerned with the diagnosis and treatment of diseases pertaining to the urinary tract and the urogenital system.""",
    )

    PRESENTATION_DIGITAL_DOCUMENT = Semantic(
        id="PresentationDigitalDocument",
        ref="schema:PresentationDigitalDocument",
        text="""A file containing slides or used for a presentation.""",
    )

    EXERCISE_PLAN = Semantic(
        id="exercisePlan",
        ref="schema:exercisePlan",
        text="""A sub property of instrument. The exercise plan used on this action.""",
    )

    CREDIT_TEXT = Semantic(
        id="creditText",
        ref="schema:creditText",
        text="""Text that can be used to credit person(s) and/or organization(s) associated with a published Creative Work.""",
    )

    CHIROPRACTIC = Semantic(
        id="Chiropractic",
        ref="schema:Chiropractic",
        text="""A system of medicine focused on the relationship between the body\'s structure, mainly the spine, and its functioning.""",
    )

    RESERVATION = Semantic(
        id="Reservation",
        ref="schema:Reservation",
        text="""Describes a reservation for travel, dining or an event. Some reservations require tickets. \\n\\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, restaurant reservations, flights, or rental cars, use [[Offer]].""",
    )

    ANESTHESIA = Semantic(
        id="Anesthesia",
        ref="schema:Anesthesia",
        text="""A specific branch of medical science that pertains to study of anesthetics and their application.""",
    )

    BACKSTORY = Semantic(
        id="backstory",
        ref="schema:backstory",
        text="""For an [[Article]], typically a [[NewsArticle]], the backstory property provides a textual summary giving a brief explanation of why and how an article was created. In a journalistic setting this could include information about reporting process, methods, interviews, data sources, etc.""",
    )

    WEARABLE_MEASUREMENT_HIPS = Semantic(
        id="WearableMeasurementHips",
        ref="schema:WearableMeasurementHips",
        text="""Measurement of the hip section, for example of a skirt""",
    )

    ALIGNMENT_TYPE = Semantic(
        id="alignmentType",
        ref="schema:alignmentType",
        text="""A category of alignment between the learning resource and the framework node. Recommended values include: \'requires\', \'textComplexity\', \'readingLevel\', and \'educationalSubject\'.""",
    )

    GEO_EQUALS = Semantic(
        id="geoEquals",
        ref="schema:geoEquals",
        text="""Represents spatial relations in which two geometries (or the places they represent) are topologically equal, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM). "Two geometries are topologically equal if their interiors intersect and no part of the interior or boundary of one geometry intersects the exterior of the other" (a symmetric relationship)""",
    )

    APPLICATION_SUB_CATEGORY = Semantic(
        id="applicationSubCategory",
        ref="schema:applicationSubCategory",
        text="""Subcategory of the application, e.g. \'Arcade Game\'.""",
    )

    SAFETY_CONSIDERATION = Semantic(
        id="safetyConsideration",
        ref="schema:safetyConsideration",
        text="""Any potential safety concern associated with the supplement. May include interactions with other drugs and foods, pregnancy, breastfeeding, known adverse reactions, and documented efficacy of the supplement.""",
    )

    ALIGNMENT_OBJECT = Semantic(
        id="AlignmentObject",
        ref="schema:AlignmentObject",
        text="""An intangible item that describes an alignment between a learning resource and a node in an educational framework.

Should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [[teaches]] or [[assesses]] a competency.""",
    )

    BED_AND_BREAKFAST = Semantic(
        id="BedAndBreakfast",
        ref="schema:BedAndBreakfast",
        text="""Bed and breakfast.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
""",
    )

    BUSINESS_AUDIENCE = Semantic(
        id="BusinessAudience",
        ref="schema:BusinessAudience",
        text="""A set of characteristics belonging to businesses, e.g. who compose an item\'s target audience.""",
    )

    SUB_ORGANIZATION = Semantic(
        id="subOrganization",
        ref="schema:subOrganization",
        text="""A relationship between two organizations where the first includes the second, e.g., as a subsidiary. See also: the more specific \'department\' property.""",
    )

    ARTICLE_SECTION = Semantic(
        id="articleSection",
        ref="schema:articleSection",
        text="""Articles may belong to one or more \'sections\' in a magazine or newspaper, such as Sports, Lifestyle, etc.""",
    )

    JOIN_ACTION = Semantic(
        id="JoinAction",
        ref="schema:JoinAction",
        text="""An agent joins an event/group with participants/friends at a location.\\n\\nRelated actions:\\n\\n* [[RegisterAction]]: Unlike RegisterAction, JoinAction refers to joining a group/team of people.\\n* [[SubscribeAction]]: Unlike SubscribeAction, JoinAction does not imply that you\'ll be receiving updates.\\n* [[FollowAction]]: Unlike FollowAction, JoinAction does not imply that you\'ll be polling for updates.""",
    )

    NUMBER_OF_BEDROOMS = Semantic(
        id="numberOfBedrooms",
        ref="schema:numberOfBedrooms",
        text="""The total integer number of bedrooms in a some [[Accommodation]], [[ApartmentComplex]] or [[FloorPlan]].""",
    )

    MEDICAL_TEST = Semantic(
        id="MedicalTest",
        ref="schema:MedicalTest",
        text="""Any medical test, typically performed for diagnostic purposes.""",
    )

    PERSON = Semantic(
        id="Person",
        ref="schema:Person",
        text="""A person (alive, dead, undead, or fictional).""",
    )

    CONTACT_POINT = Semantic(
        id="contactPoint",
        ref="schema:contactPoint",
        text="""A contact point for a person or organization.""",
    )

    BODY_MEASUREMENT_BUST = Semantic(
        id="BodyMeasurementBust",
        ref="schema:BodyMeasurementBust",
        text="""Maximum girth of bust. Used, for example, to fit women\'s suits.""",
    )

    WORST_RATING = Semantic(
        id="worstRating",
        ref="schema:worstRating",
        text="""The lowest value allowed in this rating system. If worstRating is omitted, 1 is assumed.""",
    )

    MEDICAL_CODE = Semantic(
        id="MedicalCode",
        ref="schema:MedicalCode",
        text="""A code for a medical entity.""",
    )

    ENUMERATION = Semantic(
        id="Enumeration",
        ref="schema:Enumeration",
        text="""Lists or enumerations—for example, a list of cuisines or music genres, etc.""",
    )

    PUBLIC_ACCESS = Semantic(
        id="publicAccess",
        ref="schema:publicAccess",
        text="""A flag to signal that the [[Place]] is open to public visitors.  If this property is omitted there is no assumed default boolean value""",
    )

    CUSTOMER_REMORSE_RETURN_FEES = Semantic(
        id="customerRemorseReturnFees",
        ref="schema:customerRemorseReturnFees",
        text="""The type of return fees if the product is returned due to customer remorse.""",
    )

    MUSCULOSKELETAL = Semantic(
        id="Musculoskeletal",
        ref="schema:Musculoskeletal",
        text="""A specific branch of medical science that pertains to diagnosis and treatment of disorders of muscles, ligaments and skeletal system.""",
    )

    EXPERIENCE_REQUIREMENTS = Semantic(
        id="experienceRequirements",
        ref="schema:experienceRequirements",
        text="""Description of skills and experience needed for the position or Occupation.""",
    )

    BROADCAST_RELEASE = Semantic(
        id="BroadcastRelease",
        ref="schema:BroadcastRelease",
        text="""BroadcastRelease.""",
    )

    ELECTRICIAN = Semantic(
        id="Electrician", ref="schema:Electrician", text="""An electrician."""
    )

    LEGISLATION_PASSED_BY = Semantic(
        id="legislationPassedBy",
        ref="schema:legislationPassedBy",
        text="""The person or organization that originally passed or made the law : typically parliament (for primary legislation) or government (for secondary legislation). This indicates the "legal author" of the law, as opposed to its physical author.""",
    )

    MAIN_ENTITY_OF_PAGE = Semantic(
        id="mainEntityOfPage",
        ref="schema:mainEntityOfPage",
        text="""Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See [background notes](/docs/datamodel.html#mainEntityBackground) for details.""",
    )

    ORDER_DATE = Semantic(
        id="orderDate", ref="schema:orderDate", text="""Date order was placed."""
    )

    BODY_MEASUREMENT_WAIST = Semantic(
        id="BodyMeasurementWaist",
        ref="schema:BodyMeasurementWaist",
        text="""Girth of natural waistline (between hip bones and lower ribs). Used, for example, to fit pants.""",
    )

    TRACKING_NUMBER = Semantic(
        id="trackingNumber",
        ref="schema:trackingNumber",
        text="""Shipper tracking number.""",
    )

    LEISURE_TIME_ACTIVITY = Semantic(
        id="LeisureTimeActivity",
        ref="schema:LeisureTimeActivity",
        text="""Any physical activity engaged in for recreational purposes. Examples may include ballroom dancing, roller skating, canoeing, fishing, etc.""",
    )

    PODIATRIC = Semantic(
        id="Podiatric",
        ref="schema:Podiatric",
        text="""Podiatry is the care of the human foot, especially the diagnosis and treatment of foot disorders.""",
    )

    CANCEL_ACTION = Semantic(
        id="CancelAction",
        ref="schema:CancelAction",
        text="""The act of asserting that a future event/action is no longer going to happen.\\n\\nRelated actions:\\n\\n* [[ConfirmAction]]: The antonym of CancelAction.""",
    )

    ISSUED_THROUGH = Semantic(
        id="issuedThrough",
        ref="schema:issuedThrough",
        text="""The service through with the permit was granted.""",
    )

    NOT_YET_RECRUITING = Semantic(
        id="NotYetRecruiting",
        ref="schema:NotYetRecruiting",
        text="""Not yet recruiting.""",
    )

    ASSIGN_ACTION = Semantic(
        id="AssignAction",
        ref="schema:AssignAction",
        text="""The act of allocating an action/event/task to some destination (someone or something).""",
    )

    HIRING_ORGANIZATION = Semantic(
        id="hiringOrganization",
        ref="schema:hiringOrganization",
        text="""Organization offering the job position.""",
    )

    MEDIA_REVIEW = Semantic(
        id="MediaReview",
        ref="schema:MediaReview",
        text="""A [[MediaReview]] is a more specialized form of Review dedicated to the evaluation of media content online, typically in the context of fact-checking and misinformation.
    For more general reviews of media in the broader sense, use [[UserReview]], [[CriticReview]] or other [[Review]] types. This definition is
    a work in progress. While the [[MediaManipulationRatingEnumeration]] list reflects significant community review amongst fact-checkers and others working
    to combat misinformation, the specific structures for representing media objects, their versions and publication context, is still evolving. Similarly, best practices for the relationship between [[MediaReview]] and [[ClaimReview]] markup has not yet been finalized.""",
    )

    AIRPORT = Semantic(id="Airport", ref="schema:Airport", text="""An airport.""")

    QUIZ = Semantic(
        id="Quiz",
        ref="schema:Quiz",
        text="""Quiz: A test of knowledge, skills and abilities.""",
    )

    RETAIL = Semantic(
        id="Retail",
        ref="schema:Retail",
        text="""The drug\'s cost represents the retail cost of the drug.""",
    )

    DIRECT_APPLY = Semantic(
        id="directApply",
        ref="schema:directApply",
        text="""Indicates whether an [[url]] that is associated with a [[JobPosting]] enables direct application for the job, via the posting website. A job posting is considered to have directApply of [[True]] if an application process for the specified job can be directly initiated via the url(s) given (noting that e.g. multiple internet domains might nevertheless be involved at an implementation level). A value of [[False]] is appropriate if there is no clear path to applying directly online for the specified job, navigating directly from the JobPosting url(s) supplied.""",
    )

    INCREASES_RISK_OF = Semantic(
        id="increasesRiskOf",
        ref="schema:increasesRiskOf",
        text="""The condition, complication, etc. influenced by this factor.""",
    )

    DENTIST = Semantic(id="Dentist", ref="schema:Dentist", text="""A dentist.""")

    INCLUDED_DATA_CATALOG = Semantic(
        id="includedDataCatalog",
        ref="schema:includedDataCatalog",
        text="""A data catalog which contains this dataset (this property was previously \'catalog\', preferred name is now \'includedInDataCatalog\').""",
    )

    SYNAGOGUE = Semantic(
        id="Synagogue", ref="schema:Synagogue", text="""A synagogue."""
    )

    ORDER = Semantic(
        id="Order",
        ref="schema:Order",
        text="""An order is a confirmation of a transaction (a receipt), which can contain multiple line items, each represented by an Offer that has been accepted by the customer.""",
    )

    BIKE_STORE = Semantic(
        id="BikeStore", ref="schema:BikeStore", text="""A bike store."""
    )

    EMBASSY = Semantic(id="Embassy", ref="schema:Embassy", text="""An embassy.""")

    OCCUPATIONAL_ACTIVITY = Semantic(
        id="OccupationalActivity",
        ref="schema:OccupationalActivity",
        text="""Any physical activity engaged in for job-related purposes. Examples may include waiting tables, maid service, carrying a mailbag, picking fruits or vegetables, construction work, etc.""",
    )

    CHOOSE_ACTION = Semantic(
        id="ChooseAction",
        ref="schema:ChooseAction",
        text="""The act of expressing a preference from a set of options or a large or unbounded set of choices/options.""",
    )

    SOME_PRODUCTS = Semantic(
        id="SomeProducts",
        ref="schema:SomeProducts",
        text="""A placeholder for multiple similar products of the same kind.""",
    )

    NONPROFIT501C5 = Semantic(
        id="Nonprofit501c5",
        ref="schema:Nonprofit501c5",
        text="""Nonprofit501c5: Non-profit type referring to Labor, Agricultural and Horticultural Organizations.""",
    )

    GAME_PLAY_MODE = Semantic(
        id="GamePlayMode",
        ref="schema:GamePlayMode",
        text="""Indicates whether this game is multi-player, co-op or single-player.""",
    )

    DISTANCE_FEE = Semantic(
        id="DistanceFee",
        ref="schema:DistanceFee",
        text="""Represents the distance fee (e.g., price per km or mile) part of the total price for an offered product, for example a car rental.""",
    )

    DUPLICATE_THERAPY = Semantic(
        id="duplicateTherapy",
        ref="schema:duplicateTherapy",
        text="""A therapy that duplicates or overlaps this one.""",
    )

    NUMBER_OF_BATHROOMS_TOTAL = Semantic(
        id="numberOfBathroomsTotal",
        ref="schema:numberOfBathroomsTotal",
        text="""The total integer number of bathrooms in a some [[Accommodation]], following real estate conventions as [documented in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsTotalInteger+Field): "The simple sum of the number of bathrooms. For example for a property with two Full Bathrooms and one Half Bathroom, the Bathrooms Total Integer will be 3.". See also [[numberOfRooms]].""",
    )

    MEDIA_REVIEW_ITEM = Semantic(
        id="MediaReviewItem",
        ref="schema:MediaReviewItem",
        text="""Represents an item or group of closely related items treated as a unit for the sake of evaluation in a [[MediaReview]]. Authorship etc. apply to the items rather than to the curation/grouping or reviewing party.""",
    )

    BENEFITS_HEALTH_ASPECT = Semantic(
        id="BenefitsHealthAspect",
        ref="schema:BenefitsHealthAspect",
        text="""Content about the benefits and advantages of usage or utilization of topic.""",
    )

    NEW_CONDITION = Semantic(
        id="NewCondition",
        ref="schema:NewCondition",
        text="""Indicates that the item is new.""",
    )

    NOSE = Semantic(
        id="Nose",
        ref="schema:Nose",
        text="""Nose function assessment with clinical examination.""",
    )

    HEAD = Semantic(
        id="Head",
        ref="schema:Head",
        text="""Head assessment with clinical examination.""",
    )

    DOMAIN_INCLUDES = Semantic(
        id="domainIncludes",
        ref="schema:domainIncludes",
        text="""Relates a property to a class that is (one of) the type(s) the property is expected to be used on.""",
    )

    BOOKMARK_ACTION = Semantic(
        id="BookmarkAction",
        ref="schema:BookmarkAction",
        text="""An agent bookmarks/flags/labels/tags/marks an object.""",
    )

    ANNUAL_PERCENTAGE_RATE = Semantic(
        id="annualPercentageRate",
        ref="schema:annualPercentageRate",
        text="""The annual rate that is charged for borrowing (or made by investing), expressed as a single percentage number that represents the actual yearly cost of funds over the term of a loan. This includes any fees or additional costs associated with the transaction.""",
    )

    RETURN_LABEL_DOWNLOAD_AND_PRINT = Semantic(
        id="ReturnLabelDownloadAndPrint",
        ref="schema:ReturnLabelDownloadAndPrint",
        text="""Indicated that a return label must be downloaded and printed by the customer.""",
    )

    LEGISLATION_CONSOLIDATES = Semantic(
        id="legislationConsolidates",
        ref="schema:legislationConsolidates",
        text="""Indicates another legislation taken into account in this consolidated legislation (which is usually the product of an editorial process that revises the legislation). This property should be used multiple times to refer to both the original version or the previous consolidated version, and to the legislations making the change.""",
    )

    TORQUE = Semantic(
        id="torque",
        ref="schema:torque",
        text="""The torque (turning force) of the vehicle\'s engine.\\n\\nTypical unit code(s): NU for newton metre (N m), F17 for pound-force per foot, or F48 for pound-force per inch\\n\\n* Note 1: You can link to information about how the given value has been determined (e.g. reference RPM) using the [[valueReference]] property.\\n* Note 2: You can use [[minValue]] and [[maxValue]] to indicate ranges.""",
    )

    SUB_EVENT = Semantic(
        id="subEvent",
        ref="schema:subEvent",
        text="""An Event that is part of this event. For example, a conference event includes many presentations, each of which is a subEvent of the conference.""",
    )

    SATURDAY = Semantic(
        id="Saturday",
        ref="schema:Saturday",
        text="""The day of the week between Friday and Sunday.""",
    )

    SENDER = Semantic(
        id="sender",
        ref="schema:sender",
        text="""A sub property of participant. The participant who is at the sending end of the action.""",
    )

    REPETITIONS = Semantic(
        id="repetitions",
        ref="schema:repetitions",
        text="""Number of times one should repeat the activity.""",
    )

    ABOUT = Semantic(
        id="about", ref="schema:about", text="""The subject matter of the content."""
    )

    TEXT = Semantic(
        id="text",
        ref="schema:text",
        text="""The textual content of this CreativeWork.""",
    )

    NONPROFIT501C18 = Semantic(
        id="Nonprofit501c18",
        ref="schema:Nonprofit501c18",
        text="""Nonprofit501c18: Non-profit type referring to Employee Funded Pension Trust (created before 25 June 1959).""",
    )

    HAS_MEASUREMENT = Semantic(
        id="hasMeasurement",
        ref="schema:hasMeasurement",
        text="""A product measurement, for example the inseam of pants, the wheel size of a bicycle, or the gauge of a screw. Usually an exact measurement, but can also be a range of measurements for adjustable products, for example belts and ski bindings.""",
    )

    CHOLESTEROL_CONTENT = Semantic(
        id="cholesterolContent",
        ref="schema:cholesterolContent",
        text="""The number of milligrams of cholesterol.""",
    )

    TIME_TO_COMPLETE = Semantic(
        id="timeToComplete",
        ref="schema:timeToComplete",
        text="""The expected length of time to complete the program if attending full-time.""",
    )

    OFFLINE_TEMPORARILY = Semantic(
        id="OfflineTemporarily",
        ref="schema:OfflineTemporarily",
        text="""Game server status: OfflineTemporarily. Server is offline now but it can be online soon.""",
    )

    ARRIVAL_STATION = Semantic(
        id="arrivalStation",
        ref="schema:arrivalStation",
        text="""The station where the train trip ends.""",
    )

    RISKS = Semantic(
        id="risks",
        ref="schema:risks",
        text="""Specific physiologic risks associated to the diet plan.""",
    )

    RECOMMENDED_INTAKE = Semantic(
        id="recommendedIntake",
        ref="schema:recommendedIntake",
        text="""Recommended intake of this supplement for a given population as defined by a specific recommending authority.""",
    )

    GEO_DISJOINT = Semantic(
        id="geoDisjoint",
        ref="schema:geoDisjoint",
        text="""Represents spatial relations in which two geometries (or the places they represent) are topologically disjoint: they have no point in common. They form a set of disconnected geometries." (a symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM))""",
    )

    EPIDEMIOLOGY = Semantic(
        id="epidemiology",
        ref="schema:epidemiology",
        text="""The characteristics of associated patients, such as age, gender, race etc.""",
    )

    ZOO = Semantic(id="Zoo", ref="schema:Zoo", text="""A zoo.""")

    PERMITTED_USAGE = Semantic(
        id="permittedUsage",
        ref="schema:permittedUsage",
        text="""Indications regarding the permitted usage of the accommodation.""",
    )

    DOMICILED_MORTGAGE = Semantic(
        id="domiciledMortgage",
        ref="schema:domiciledMortgage",
        text="""Whether borrower is a resident of the jurisdiction where the property is located.""",
    )

    OPTION = Semantic(
        id="option",
        ref="schema:option",
        text="""A sub property of object. The options subject to this action.""",
    )

    RESERVATION_ID = Semantic(
        id="reservationId",
        ref="schema:reservationId",
        text="""A unique identifier for the reservation.""",
    )

    LEGAL_VALUE_LEVEL = Semantic(
        id="LegalValueLevel",
        ref="schema:LegalValueLevel",
        text="""A list of possible levels for the legal validity of a legislation.""",
    )

    RECIPE_INSTRUCTIONS = Semantic(
        id="recipeInstructions",
        ref="schema:recipeInstructions",
        text="""A step in making the recipe, in the form of a single item (document, video, etc.) or an ordered list with HowToStep and/or HowToSection items.""",
    )

    BOOK_SERIES = Semantic(
        id="BookSeries",
        ref="schema:BookSeries",
        text="""A series of books. Included books can be indicated with the hasPart property.""",
    )

    BODY_MEASUREMENT_INSIDE_LEG = Semantic(
        id="BodyMeasurementInsideLeg",
        ref="schema:BodyMeasurementInsideLeg",
        text="""Inside leg (measured between crotch and soles of feet). Used, for example, to fit pants.""",
    )

    PARK = Semantic(id="Park", ref="schema:Park", text="""A park.""")

    DRUG_COST_CATEGORY = Semantic(
        id="DrugCostCategory",
        ref="schema:DrugCostCategory",
        text="""Enumerated categories of medical drug costs.""",
    )

    UNINCORPORATED_ASSOCIATION_CHARITY = Semantic(
        id="UnincorporatedAssociationCharity",
        ref="schema:UnincorporatedAssociationCharity",
        text="""UnincorporatedAssociationCharity: Non-profit type referring to a charitable company that is not incorporated (UK).""",
    )

    SEATING_MAP = Semantic(
        id="SeatingMap", ref="schema:SeatingMap", text="""A seating map."""
    )

    NONPROFIT501F = Semantic(
        id="Nonprofit501f",
        ref="schema:Nonprofit501f",
        text="""Nonprofit501f: Non-profit type referring to Cooperative Service Organizations.""",
    )

    FOOD_ESTABLISHMENT = Semantic(
        id="FoodEstablishment",
        ref="schema:FoodEstablishment",
        text="""A food-related business.""",
    )

    TYPICAL_TEST = Semantic(
        id="typicalTest",
        ref="schema:typicalTest",
        text="""A medical test typically performed given this condition.""",
    )

    DATE_DELETED = Semantic(
        id="dateDeleted",
        ref="schema:dateDeleted",
        text="""The datetime the item was removed from the DataFeed.""",
    )

    CHARACTER = Semantic(
        id="character",
        ref="schema:character",
        text="""Fictional person connected with a creative work.""",
    )

    COOK_TIME = Semantic(
        id="cookTime",
        ref="schema:cookTime",
        text="""The time it takes to actually cook the dish, in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).""",
    )

    SUGGESTED_GENDER = Semantic(
        id="suggestedGender",
        ref="schema:suggestedGender",
        text="""The suggested gender of the intended person or audience, for example "male", "female", or "unisex".""",
    )

    ACTORS = Semantic(
        id="actors",
        ref="schema:actors",
        text="""An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.""",
    )

    GEO_TOUCHES = Semantic(
        id="geoTouches",
        ref="schema:geoTouches",
        text="""Represents spatial relations in which two geometries (or the places they represent) touch: they have at least one boundary point in common, but no interior points." (a symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM) )""",
    )

    LEND_ACTION = Semantic(
        id="LendAction",
        ref="schema:LendAction",
        text="""The act of providing an object under an agreement that it will be returned at a later date. Reciprocal of BorrowAction.\\n\\nRelated actions:\\n\\n* [[BorrowAction]]: Reciprocal of LendAction.""",
    )

    LEGISLATION_CHANGES = Semantic(
        id="legislationChanges",
        ref="schema:legislationChanges",
        text="""Another legislation that this legislation changes. This encompasses the notions of amendment, replacement, correction, repeal, or other types of change. This may be a direct change (textual or non-textual amendment) or a consequential or indirect change. The property is to be used to express the existence of a change relationship between two acts rather than the existence of a consolidated version of the text that shows the result of the change. For consolidation relationships, use the <a href="/legislationConsolidates">legislationConsolidates</a> property.""",
    )

    SKILLS = Semantic(
        id="skills",
        ref="schema:skills",
        text="""A statement of knowledge, skill, ability, task or any other assertion expressing a competency that is desired or required to fulfill this role or to work in this occupation.""",
    )

    INCLUDES_OBJECT = Semantic(
        id="includesObject",
        ref="schema:includesObject",
        text="""This links to a node or nodes indicating the exact quantity of the products included in  an [[Offer]] or [[ProductCollection]].""",
    )

    DRUG_COST = Semantic(
        id="DrugCost",
        ref="schema:DrugCost",
        text="""The cost per unit of a medical drug. Note that this type is not meant to represent the price in an offer of a drug for sale; see the Offer type for that. This type will typically be used to tag wholesale or average retail cost of a drug, or maximum reimbursable cost. Costs of medical drugs vary widely depending on how and where they are paid for, so while this type captures some of the variables, costs should be used with caution by consumers of this schema\'s markup.""",
    )

    PRICE_RANGE = Semantic(
        id="priceRange",
        ref="schema:priceRange",
        text="""The price range of the business, for example ```$$$```.""",
    )

    ARTWORK_SURFACE = Semantic(
        id="artworkSurface",
        ref="schema:artworkSurface",
        text="""The supporting materials for the artwork, e.g. Canvas, Paper, Wood, Board, etc.""",
    )

    PROCESSOR_REQUIREMENTS = Semantic(
        id="processorRequirements",
        ref="schema:processorRequirements",
        text="""Processor architecture required to run the application (e.g. IA64).""",
    )

    DEMAND = Semantic(
        id="Demand",
        ref="schema:Demand",
        text="""A demand entity represents the public, not necessarily binding, not necessarily exclusive, announcement by an organization or person to seek a certain type of goods or services. For describing demand using this type, the very same properties used for Offer apply.""",
    )

    ISSUE_NUMBER = Semantic(
        id="issueNumber",
        ref="schema:issueNumber",
        text="""Identifies the issue of publication; for example, "iii" or "2".""",
    )

    OFFERS = Semantic(
        id="offers",
        ref="schema:offers",
        text="""An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
      """,
    )

    IN_STORE_ONLY = Semantic(
        id="InStoreOnly",
        ref="schema:InStoreOnly",
        text="""Indicates that the item is available only at physical locations.""",
    )

    SPORTS_ACTIVITY_LOCATION = Semantic(
        id="SportsActivityLocation",
        ref="schema:SportsActivityLocation",
        text="""A sports location, such as a playing field.""",
    )

    USER_REVIEW = Semantic(
        id="UserReview",
        ref="schema:UserReview",
        text="""A review created by an end-user (e.g. consumer, purchaser, attendee etc.), in contrast with [[CriticReview]].""",
    )

    BUSINESS_ENTITY_TYPE = Semantic(
        id="BusinessEntityType",
        ref="schema:BusinessEntityType",
        text="""A business entity type is a conceptual entity representing the legal form, the size, the main line of business, the position in the value chain, or any combination thereof, of an organization or business person.\\n\\nCommonly used values:\\n\\n* http://purl.org/goodrelations/v1#Business\\n* http://purl.org/goodrelations/v1#Enduser\\n* http://purl.org/goodrelations/v1#PublicInstitution\\n* http://purl.org/goodrelations/v1#Reseller
	  """,
    )

    LOCATION_FEATURE_SPECIFICATION = Semantic(
        id="LocationFeatureSpecification",
        ref="schema:LocationFeatureSpecification",
        text="""Specifies a location feature by providing a structured value representing a feature of an accommodation as a property-value pair of varying degrees of formality.""",
    )

    MEETS_EMISSION_STANDARD = Semantic(
        id="meetsEmissionStandard",
        ref="schema:meetsEmissionStandard",
        text="""Indicates that the vehicle meets the respective emission standard.""",
    )

    BOOK_STORE = Semantic(
        id="BookStore", ref="schema:BookStore", text="""A bookstore."""
    )

    STAGES_HEALTH_ASPECT = Semantic(
        id="StagesHealthAspect",
        ref="schema:StagesHealthAspect",
        text="""Stages that can be observed from a topic.""",
    )

    THERAPEUTIC_PROCEDURE = Semantic(
        id="TherapeuticProcedure",
        ref="schema:TherapeuticProcedure",
        text="""A medical procedure intended primarily for therapeutic purposes, aimed at improving a health condition.""",
    )

    CONTACTLESS_PAYMENT = Semantic(
        id="contactlessPayment",
        ref="schema:contactlessPayment",
        text="""A secure method for consumers to purchase products or services via debit, credit or smartcards by using RFID or NFC technology.""",
    )

    LEGISLATIVE_BUILDING = Semantic(
        id="LegislativeBuilding",
        ref="schema:LegislativeBuilding",
        text="""A legislative building&#x2014;for example, the state capitol.""",
    )

    ESTIMATED_SALARY = Semantic(
        id="estimatedSalary",
        ref="schema:estimatedSalary",
        text="""An estimated salary for a job posting or occupation, based on a variety of variables including, but not limited to industry, job title, and location. Estimated salaries  are often computed by outside organizations rather than the hiring organization, who may not have committed to the estimated value.""",
    )

    WEB_PAGE = Semantic(
        id="WebPage",
        ref="schema:WebPage",
        text="""A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as <code>breadcrumb</code> may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page.""",
    )

    SIZE_SYSTEM_METRIC = Semantic(
        id="SizeSystemMetric",
        ref="schema:SizeSystemMetric",
        text="""Metric size system.""",
    )

    LOW_LACTOSE_DIET = Semantic(
        id="LowLactoseDiet",
        ref="schema:LowLactoseDiet",
        text="""A diet appropriate for people with lactose intolerance.""",
    )

    STATEMENT = Semantic(
        id="Statement",
        ref="schema:Statement",
        text="""A statement about something, for example a fun or interesting fact. If known, the main entity this statement is about, can be indicated using mainEntity. For more formal claims (e.g. in Fact Checking), consider using [[Claim]] instead. Use the [[text]] property to capture the text of the statement.""",
    )

    X_RAY = Semantic(id="XRay", ref="schema:XRay", text="""X-ray imaging.""")

    PAYMENT_PAST_DUE = Semantic(
        id="PaymentPastDue",
        ref="schema:PaymentPastDue",
        text="""The payment is due and considered late.""",
    )

    SELF_CARE_HEALTH_ASPECT = Semantic(
        id="SelfCareHealthAspect",
        ref="schema:SelfCareHealthAspect",
        text="""Self care actions or measures that can be taken to sooth, health or avoid a topic. This may be carried at home and can be carried/managed by the person itself.""",
    )

    CLIP = Semantic(
        id="Clip",
        ref="schema:Clip",
        text="""A short TV or radio program or a segment/part of a program.""",
    )

    PRESCRIBING_INFO = Semantic(
        id="prescribingInfo",
        ref="schema:prescribingInfo",
        text="""Link to prescribing information for the drug.""",
    )

    TRIBUTARY = Semantic(
        id="tributary",
        ref="schema:tributary",
        text="""The anatomical or organ system that the vein flows into; a larger structure that the vein connects to.""",
    )

    CUSTOMER_REMORSE_RETURN_SHIPPING_FEES_AMOUNT = Semantic(
        id="customerRemorseReturnShippingFeesAmount",
        ref="schema:customerRemorseReturnShippingFeesAmount",
        text="""The amount of shipping costs if a product is returned due to customer remorse. Applicable when property [[customerRemorseReturnFees]] equals [[ReturnShippingFees]].""",
    )

    WEARABLE_SIZE_GROUP_PLUS = Semantic(
        id="WearableSizeGroupPlus",
        ref="schema:WearableSizeGroupPlus",
        text="""Size group "Plus" for wearables.""",
    )

    SIDE_EFFECTS_HEALTH_ASPECT = Semantic(
        id="SideEffectsHealthAspect",
        ref="schema:SideEffectsHealthAspect",
        text="""Side effects that can be observed from the usage of the topic.""",
    )

    LOCATION_CREATED = Semantic(
        id="locationCreated",
        ref="schema:locationCreated",
        text="""The location where the CreativeWork was created, which may not be the same as the location depicted in the CreativeWork.""",
    )

    ANNOUNCEMENT_LOCATION = Semantic(
        id="announcementLocation",
        ref="schema:announcementLocation",
        text="""Indicates a specific [[CivicStructure]] or [[LocalBusiness]] associated with the SpecialAnnouncement. For example, a specific testing facility or business with special opening hours. For a larger geographic region like a quarantine of an entire region, use [[spatialCoverage]].""",
    )

    DOOR_TIME = Semantic(
        id="doorTime",
        ref="schema:doorTime",
        text="""The time admission will commence.""",
    )

    COLLEAGUES = Semantic(
        id="colleagues", ref="schema:colleagues", text="""A colleague of the person."""
    )

    ROOM = Semantic(
        id="Room",
        ref="schema:Room",
        text="""A room is a distinguishable space within a structure, usually separated from other spaces by interior walls. (Source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Room">http://en.wikipedia.org/wiki/Room</a>).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
""",
    )

    EXCEPT_DATE = Semantic(
        id="exceptDate",
        ref="schema:exceptDate",
        text="""Defines a [[Date]] or [[DateTime]] during which a scheduled [[Event]] will not take place. The property allows exceptions to
      a [[Schedule]] to be specified. If an exception is specified as a [[DateTime]] then only the event that would have started at that specific date and time
      should be excluded from the schedule. If an exception is specified as a [[Date]] then any event that is scheduled for that 24 hour period should be
      excluded from the schedule. This allows a whole day to be excluded from the schedule without having to itemise every scheduled event.""",
    )

    VIDEO_GAME_SERIES = Semantic(
        id="VideoGameSeries",
        ref="schema:VideoGameSeries",
        text="""A video game series.""",
    )

    ADDITIONAL_TYPE = Semantic(
        id="additionalType",
        ref="schema:additionalType",
        text="""An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the \'typeof\' attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally.""",
    )

    STRENGTH_TRAINING = Semantic(
        id="StrengthTraining",
        ref="schema:StrengthTraining",
        text="""Physical activity that is engaged in to improve muscle and bone strength. Also referred to as resistance training.""",
    )

    RESULT = Semantic(
        id="result",
        ref="schema:result",
        text="""The result produced in the action. e.g. John wrote *a book*.""",
    )

    KNOWN_VEHICLE_DAMAGES = Semantic(
        id="knownVehicleDamages",
        ref="schema:knownVehicleDamages",
        text="""A textual description of known damages, both repaired and unrepaired.""",
    )

    THUMBNAIL = Semantic(
        id="thumbnail",
        ref="schema:thumbnail",
        text="""Thumbnail image for an image or video.""",
    )

    OCCUPATIONAL_EXPERIENCE_REQUIREMENTS = Semantic(
        id="OccupationalExperienceRequirements",
        ref="schema:OccupationalExperienceRequirements",
        text="""Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].""",
    )

    BROADCAST_FREQUENCY = Semantic(
        id="broadcastFrequency",
        ref="schema:broadcastFrequency",
        text="""The frequency used for over-the-air broadcasts. Numeric values or simple ranges e.g. 87-99. In addition a shortcut idiom is supported for frequences of AM and FM radio channels, e.g. "87 FM".""",
    )

    SPEECH_PATHOLOGY = Semantic(
        id="SpeechPathology",
        ref="schema:SpeechPathology",
        text="""The scientific study and treatment of defects, disorders, and malfunctions of speech and voice, as stuttering, lisping, or lalling, and of language disturbances, as aphasia or delayed language acquisition.""",
    )

    OBJECT = Semantic(
        id="object",
        ref="schema:object",
        text="""The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn\'t). e.g. John read *a book*.""",
    )

    MOLECULAR_ENTITY = Semantic(
        id="MolecularEntity",
        ref="schema:MolecularEntity",
        text="""Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity.""",
    )

    NUM_TRACKS = Semantic(
        id="numTracks",
        ref="schema:numTracks",
        text="""The number of tracks in this album or playlist.""",
    )

    IS_BASED_ON_URL = Semantic(
        id="isBasedOnUrl",
        ref="schema:isBasedOnUrl",
        text="""A resource that was used in the creation of this resource. This term can be repeated for multiple sources. For example, http://example.com/great-multiplication-intro.html.""",
    )

    GASTROENTEROLOGIC = Semantic(
        id="Gastroenterologic",
        ref="schema:Gastroenterologic",
        text="""A specific branch of medical science that pertains to diagnosis and treatment of disorders of digestive system.""",
    )

    WEARABLE_MEASUREMENT_BACK = Semantic(
        id="WearableMeasurementBack",
        ref="schema:WearableMeasurementBack",
        text="""Measurement of the back section, for example of a jacket""",
    )

    NUMBER_OF_DOORS = Semantic(
        id="numberOfDoors",
        ref="schema:numberOfDoors",
        text="""The number of doors.\\n\\nTypical unit code(s): C62""",
    )

    LOAN_MORTGAGE_MANDATE_AMOUNT = Semantic(
        id="loanMortgageMandateAmount",
        ref="schema:loanMortgageMandateAmount",
        text="""Amount of mortgage mandate that can be converted into a proper mortgage at a later stage.""",
    )

    MULTIPLE_VALUES = Semantic(
        id="multipleValues",
        ref="schema:multipleValues",
        text="""Whether multiple values are allowed for the property.  Default is false.""",
    )

    OPENING_HOURS = Semantic(
        id="openingHours",
        ref="schema:openingHours",
        text="""The general opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas \',\' separating each day. Day or time ranges are specified using a hyphen \'-\'.\\n\\n* Days are specified using the following two-letter combinations: ```Mo```, ```Tu```, ```We```, ```Th```, ```Fr```, ```Sa```, ```Su```.\\n* Times are specified using 24:00 format. For example, 3pm is specified as ```15:00```, 10am as ```10:00```. \\n* Here is an example: <code>&lt;time itemprop="openingHours" datetime=&quot;Tu,Th 16:00-20:00&quot;&gt;Tuesdays and Thursdays 4-8pm&lt;/time&gt;</code>.\\n* If a business is open 7 days a week, then it can be specified as <code>&lt;time itemprop=&quot;openingHours&quot; datetime=&quot;Mo-Su&quot;&gt;Monday through Sunday, all day&lt;/time&gt;</code>.""",
    )

    REIMBURSEMENT_CAP = Semantic(
        id="ReimbursementCap",
        ref="schema:ReimbursementCap",
        text="""The drug\'s cost represents the maximum reimbursement paid by an insurer for the drug.""",
    )

    BUSINESS_SUPPORT = Semantic(
        id="BusinessSupport",
        ref="schema:BusinessSupport",
        text="""BusinessSupport: this is a benefit for supporting businesses.""",
    )

    LESSER = Semantic(
        id="lesser",
        ref="schema:lesser",
        text="""This ordering relation for qualitative values indicates that the subject is lesser than the object.""",
    )

    JOB_TITLE = Semantic(
        id="jobTitle",
        ref="schema:jobTitle",
        text="""The job title of the person (for example, Financial Manager).""",
    )

    ACTIVATION_FEE = Semantic(
        id="ActivationFee",
        ref="schema:ActivationFee",
        text="""Represents the activation fee part of the total price for an offered product, for example a cellphone contract.""",
    )

    AREA_SERVED = Semantic(
        id="areaServed",
        ref="schema:areaServed",
        text="""The geographic area where a service or offered item is provided.""",
    )

    SPECIAL_OPENING_HOURS_SPECIFICATION = Semantic(
        id="specialOpeningHoursSpecification",
        ref="schema:specialOpeningHoursSpecification",
        text="""The special opening hours of a certain place.\\n\\nUse this to explicitly override general opening hours brought in scope by [[openingHoursSpecification]] or [[openingHours]].
      """,
    )

    PAYMENT_DUE = Semantic(
        id="paymentDue",
        ref="schema:paymentDue",
        text="""The date that payment is due.""",
    )

    SERVER_STATUS = Semantic(
        id="serverStatus",
        ref="schema:serverStatus",
        text="""Status of a game server.""",
    )

    COLOR = Semantic(
        id="color", ref="schema:color", text="""The color of the product."""
    )

    CORRECTION_COMMENT = Semantic(
        id="CorrectionComment",
        ref="schema:CorrectionComment",
        text="""A [[comment]] that corrects [[CreativeWork]].""",
    )

    RETURN_METHOD_ENUMERATION = Semantic(
        id="ReturnMethodEnumeration",
        ref="schema:ReturnMethodEnumeration",
        text="""Enumerates several types of product return methods.""",
    )

    RESIDENCE = Semantic(
        id="Residence",
        ref="schema:Residence",
        text="""The place where a person lives.""",
    )

    MEDICAL_SPECIALTY = Semantic(
        id="medicalSpecialty",
        ref="schema:medicalSpecialty",
        text="""A medical specialty of the provider.""",
    )

    MANUSCRIPT = Semantic(
        id="Manuscript",
        ref="schema:Manuscript",
        text="""A book, document, or piece of music written by hand rather than typed or printed.""",
    )

    SITE_NAVIGATION_ELEMENT = Semantic(
        id="SiteNavigationElement",
        ref="schema:SiteNavigationElement",
        text="""A navigation element of the page.""",
    )

    SHEET_MUSIC = Semantic(
        id="SheetMusic",
        ref="schema:SheetMusic",
        text="""Printed music, as opposed to performed or recorded music.""",
    )

    DIAGNOSIS = Semantic(
        id="diagnosis",
        ref="schema:diagnosis",
        text="""One or more alternative conditions considered in the differential diagnosis process as output of a diagnosis process.""",
    )

    CVD_NUM_VENT_USE = Semantic(
        id="cvdNumVentUse",
        ref="schema:cvdNumVentUse",
        text="""numventuse - MECHANICAL VENTILATORS IN USE: Total number of ventilators in use.""",
    )

    RSVP_RESPONSE_NO = Semantic(
        id="RsvpResponseNo",
        ref="schema:RsvpResponseNo",
        text="""The invitee will not attend.""",
    )

    RISK_FACTOR = Semantic(
        id="riskFactor",
        ref="schema:riskFactor",
        text="""A modifiable or non-modifiable factor that increases the risk of a patient contracting this condition, e.g. age,  coexisting condition.""",
    )

    DATA_TYPE = Semantic(
        id="DataType",
        ref="schema:DataType",
        text="""The basic data types such as Integers, Strings, etc.""",
    )

    AUTO_PARTS_STORE = Semantic(
        id="AutoPartsStore",
        ref="schema:AutoPartsStore",
        text="""An auto parts store.""",
    )

    RADIO_EPISODE = Semantic(
        id="RadioEpisode",
        ref="schema:RadioEpisode",
        text="""A radio episode which can be part of a series or season.""",
    )

    IS_PART_OF = Semantic(
        id="isPartOf",
        ref="schema:isPartOf",
        text="""Indicates an item or CreativeWork that this item, or CreativeWork (in some sense), is part of.""",
    )

    LOAN_REPAYMENT_FORM = Semantic(
        id="loanRepaymentForm",
        ref="schema:loanRepaymentForm",
        text="""A form of paying back money previously borrowed from a lender. Repayment usually takes the form of periodic payments that normally include part principal plus interest in each payment.""",
    )

    SEASON = Semantic(
        id="Season",
        ref="schema:Season",
        text="""A media season e.g. tv, radio, video game etc.""",
    )

    HALAL_DIET = Semantic(
        id="HalalDiet",
        ref="schema:HalalDiet",
        text="""A diet conforming to Islamic dietary practices.""",
    )

    INGREDIENTS = Semantic(
        id="ingredients",
        ref="schema:ingredients",
        text="""A single ingredient used in the recipe, e.g. sugar, flour or garlic.""",
    )

    CLINICAL_PHARMACOLOGY = Semantic(
        id="clinicalPharmacology",
        ref="schema:clinicalPharmacology",
        text="""Description of the absorption and elimination of drugs, including their concentration (pharmacokinetics, pK) and biological effects (pharmacodynamics, pD).""",
    )

    DAY_SPA = Semantic(id="DaySpa", ref="schema:DaySpa", text="""A day spa.""")

    PERCENTILE75 = Semantic(
        id="percentile75",
        ref="schema:percentile75",
        text="""The 75th percentile value.""",
    )

    ANALYSIS_NEWS_ARTICLE = Semantic(
        id="AnalysisNewsArticle",
        ref="schema:AnalysisNewsArticle",
        text="""An AnalysisNewsArticle is a [[NewsArticle]] that, while based on factual reporting, incorporates the expertise of the author/producer, offering interpretations and conclusions.""",
    )

    ENERGY_EFFICIENCY_SCALE_MAX = Semantic(
        id="energyEfficiencyScaleMax",
        ref="schema:energyEfficiencyScaleMax",
        text="""Specifies the most energy efficient class on the regulated EU energy consumption scale for the product category a product belongs to. For example, energy consumption for televisions placed on the market after January 1, 2020 is scaled from D to A+++.""",
    )

    HAS_MENU_SECTION = Semantic(
        id="hasMenuSection",
        ref="schema:hasMenuSection",
        text="""A subgrouping of the menu (by dishes, course, serving time period, etc.).""",
    )

    STUDIO_ALBUM = Semantic(
        id="StudioAlbum", ref="schema:StudioAlbum", text="""StudioAlbum."""
    )

    RETURN_SHIPPING_FEES = Semantic(
        id="ReturnShippingFees",
        ref="schema:ReturnShippingFees",
        text="""Specifies that the customer must pay the return shipping costs when returning a product""",
    )

    ACTIONABLE_FEEDBACK_POLICY = Semantic(
        id="actionableFeedbackPolicy",
        ref="schema:actionableFeedbackPolicy",
        text="""For a [[NewsMediaOrganization]] or other news-related [[Organization]], a statement about public engagement activities (for news media, the newsroom’s), including involving the public - digitally or otherwise -- in coverage decisions, reporting and activities after publication.""",
    )

    CONTAINS_SEASON = Semantic(
        id="containsSeason",
        ref="schema:containsSeason",
        text="""A season that is part of the media series.""",
    )

    POLYGON = Semantic(
        id="polygon",
        ref="schema:polygon",
        text="""A polygon is the area enclosed by a point-to-point path for which the starting and ending points are the same. A polygon is expressed as a series of four or more space delimited points where the first and final points are identical.""",
    )

    VALUE_MAX_LENGTH = Semantic(
        id="valueMaxLength",
        ref="schema:valueMaxLength",
        text="""Specifies the allowed range for number of characters in a literal value.""",
    )

    PARENT_ORGANIZATION = Semantic(
        id="parentOrganization",
        ref="schema:parentOrganization",
        text="""The larger organization that this organization is a [[subOrganization]] of, if any.""",
    )

    MATERIAL_EXTENT = Semantic(
        id="materialExtent",
        ref="schema:materialExtent",
        text="""The quantity of the materials being described or an expression of the physical space they occupy.""",
    )

    ENERGY = Semantic(
        id="Energy",
        ref="schema:Energy",
        text="""Properties that take Energy as values are of the form \'&lt;Number&gt; &lt;Energy unit of measure&gt;\'.""",
    )

    DEACTIVATE_ACTION = Semantic(
        id="DeactivateAction",
        ref="schema:DeactivateAction",
        text="""The act of stopping or deactivating a device or application (e.g. stopping a timer or turning off a flashlight).""",
    )

    DISCOUNT = Semantic(
        id="discount",
        ref="schema:discount",
        text="""Any discount applied (to an Order).""",
    )

    CONTENT_REFERENCE_TIME = Semantic(
        id="contentReferenceTime",
        ref="schema:contentReferenceTime",
        text="""The specific time described by a creative work, for works (e.g. articles, video objects etc.) that emphasise a particular moment within an Event.""",
    )

    MUSIC_ALBUM = Semantic(
        id="MusicAlbum",
        ref="schema:MusicAlbum",
        text="""A collection of music tracks.""",
    )

    IS_PART_OF_BIO_CHEM_ENTITY = Semantic(
        id="isPartOfBioChemEntity",
        ref="schema:isPartOfBioChemEntity",
        text="""Indicates a BioChemEntity that is (in some sense) a part of this BioChemEntity. """,
    )

    VEHICLE_SPECIAL_USAGE = Semantic(
        id="vehicleSpecialUsage",
        ref="schema:vehicleSpecialUsage",
        text="""Indicates whether the vehicle has been used for special purposes, like commercial rental, driving school, or as a taxi. The legislation in many countries requires this information to be revealed when offering a car for sale.""",
    )

    TRAVEL_ACTION = Semantic(
        id="TravelAction",
        ref="schema:TravelAction",
        text="""The act of traveling from an fromLocation to a destination by a specified mode of transport, optionally with participants.""",
    )

    INSTALL_URL = Semantic(
        id="installUrl",
        ref="schema:installUrl",
        text="""URL at which the app may be installed, if different from the URL of the item.""",
    )

    HEALTHCARE_REPORTING_DATA = Semantic(
        id="healthcareReportingData",
        ref="schema:healthcareReportingData",
        text="""Indicates data describing a hospital, e.g. a CDC [[CDCPMDRecord]] or as some kind of [[Dataset]].""",
    )

    PROGRAM_MEMBERSHIP_USED = Semantic(
        id="programMembershipUsed",
        ref="schema:programMembershipUsed",
        text="""Any membership in a frequent flyer, hotel loyalty program, etc. being applied to the reservation.""",
    )

    NATIONALITY = Semantic(
        id="nationality",
        ref="schema:nationality",
        text="""Nationality of the person.""",
    )

    AVAILABLE_DELIVERY_METHOD = Semantic(
        id="availableDeliveryMethod",
        ref="schema:availableDeliveryMethod",
        text="""The delivery method(s) available for this offer.""",
    )

    PERMIT = Semantic(
        id="Permit",
        ref="schema:Permit",
        text="""A permit issued by an organization, e.g. a parking pass.""",
    )

    HONORIFIC_PREFIX = Semantic(
        id="honorificPrefix",
        ref="schema:honorificPrefix",
        text="""An honorific prefix preceding a Person\'s name such as Dr/Mrs/Mr.""",
    )

    RECIPE_CUISINE = Semantic(
        id="recipeCuisine",
        ref="schema:recipeCuisine",
        text="""The cuisine of the recipe (for example, French or Ethiopian).""",
    )

    GYNECOLOGIC = Semantic(
        id="Gynecologic",
        ref="schema:Gynecologic",
        text="""A specific branch of medical science that pertains to the health care of women, particularly in the diagnosis and treatment of disorders affecting the female reproductive system.""",
    )

    ALBUM_PRODUCTION_TYPE = Semantic(
        id="albumProductionType",
        ref="schema:albumProductionType",
        text="""Classification of the album by it\'s type of content: soundtrack, live album, studio album, etc.""",
    )

    MAINTAINER = Semantic(
        id="maintainer",
        ref="schema:maintainer",
        text="""A maintainer of a [[Dataset]], software package ([[SoftwareApplication]]), or other [[Project]]. A maintainer is a [[Person]] or [[Organization]] that manages contributions to, and/or publication of, some (typically complex) artifact. It is common for distributions of software and data to be based on "upstream" sources. When [[maintainer]] is applied to a specific version of something e.g. a particular version or packaging of a [[Dataset]], it is always  possible that the upstream source has a different maintainer. The [[isBasedOn]] property can be used to indicate such relationships between datasets to make the different maintenance roles clear. Similarly in the case of software, a package may have dedicated maintainers working on integration into software distributions such as Ubuntu, as well as upstream maintainers of the underlying work.
      """,
    )

    ADDITIONAL_NUMBER_OF_GUESTS = Semantic(
        id="additionalNumberOfGuests",
        ref="schema:additionalNumberOfGuests",
        text="""If responding yes, the number of guests who will attend in addition to the invitee.""",
    )

    WORK_LOCATION = Semantic(
        id="workLocation",
        ref="schema:workLocation",
        text="""A contact location for a person\'s place of work.""",
    )

    NUMBERED_POSITION = Semantic(
        id="numberedPosition",
        ref="schema:numberedPosition",
        text="""A number associated with a role in an organization, for example, the number on an athlete\'s jersey.""",
    )

    EFFECTIVENESS_HEALTH_ASPECT = Semantic(
        id="EffectivenessHealthAspect",
        ref="schema:EffectivenessHealthAspect",
        text="""Content about the effectiveness-related aspects of a health topic.""",
    )

    WHOLESALE_STORE = Semantic(
        id="WholesaleStore", ref="schema:WholesaleStore", text="""A wholesale store."""
    )

    MEMBERSHIP_NUMBER = Semantic(
        id="membershipNumber",
        ref="schema:membershipNumber",
        text="""A unique identifier for the membership.""",
    )

    FUNDING_SCHEME = Semantic(
        id="FundingScheme",
        ref="schema:FundingScheme",
        text="""A FundingScheme combines organizational, project and policy aspects of grant-based funding
    that sets guidelines, principles and mechanisms to support other kinds of projects and activities.
    Funding is typically organized via [[Grant]] funding. Examples of funding schemes: Swiss Priority Programmes (SPPs); EU Framework 7 (FP7); Horizon 2020; the NIH-R01 Grant Program; Wellcome institutional strategic support fund. For large scale public sector funding, the management and administration of grant awards is often handled by other, dedicated, organizations - [[FundingAgency]]s such as ERC, REA, ...""",
    )

    RECOMMENDATION = Semantic(
        id="Recommendation",
        ref="schema:Recommendation",
        text="""[[Recommendation]] is a type of [[Review]] that suggests or proposes something as the best option or best course of action. Recommendations may be for products or services, or other concrete things, as in the case of a ranked list or product guide. A [[Guide]] may list multiple recommendations for different categories. For example, in a [[Guide]] about which TVs to buy, the author may have several [[Recommendation]]s.""",
    )

    CLINICIAN = Semantic(
        id="Clinician",
        ref="schema:Clinician",
        text="""Medical clinicians, including practicing physicians and other medical professionals involved in clinical practice.""",
    )

    MEDICINE_SYSTEM = Semantic(
        id="medicineSystem",
        ref="schema:medicineSystem",
        text="""The system of medicine that includes this MedicalEntity, for example \'evidence-based\', \'homeopathic\', \'chiropractic\', etc.""",
    )

    USES_DEVICE = Semantic(
        id="usesDevice",
        ref="schema:usesDevice",
        text="""Device used to perform the test.""",
    )

    TYPICAL_AGE_RANGE = Semantic(
        id="typicalAgeRange",
        ref="schema:typicalAgeRange",
        text="""The typical expected age range, e.g. \'7-9\', \'11-\'.""",
    )

    AUTHOR = Semantic(
        id="author",
        ref="schema:author",
        text="""The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.""",
    )

    IN_STORE_RETURNS_OFFERED = Semantic(
        id="inStoreReturnsOffered",
        ref="schema:inStoreReturnsOffered",
        text="""Are in-store returns offered? (for more advanced return methods use the [[returnMethod]] property)""",
    )

    COLLECTION_SIZE = Semantic(
        id="collectionSize",
        ref="schema:collectionSize",
        text="""The number of items in the [[Collection]].""",
    )

    MARRY_ACTION = Semantic(
        id="MarryAction",
        ref="schema:MarryAction",
        text="""The act of marrying a person.""",
    )

    IS_ACCESSORY_OR_SPARE_PART_FOR = Semantic(
        id="isAccessoryOrSparePartFor",
        ref="schema:isAccessoryOrSparePartFor",
        text="""A pointer to another product (or multiple products) for which this product is an accessory or spare part.""",
    )

    DATA_DOWNLOAD = Semantic(
        id="DataDownload",
        ref="schema:DataDownload",
        text="""A dataset in downloadable form.""",
    )

    ASSOCIATED_MEDIA_REVIEW = Semantic(
        id="associatedMediaReview",
        ref="schema:associatedMediaReview",
        text="""An associated [[MediaReview]], related by specific common content, topic or claim. The expectation is that this property would be most typically used in cases where a single activity is conducting both claim reviews and media reviews, in which case [[relatedMediaReview]] would commonly be used on a [[ClaimReview]], while [[relatedClaimReview]] would be used on [[MediaReview]].""",
    )

    BOAT_RESERVATION = Semantic(
        id="BoatReservation",
        ref="schema:BoatReservation",
        text="""A reservation for boat travel.

Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].""",
    )

    HINDU_TEMPLE = Semantic(
        id="HinduTemple", ref="schema:HinduTemple", text="""A Hindu temple."""
    )

    DIAGNOSTIC = Semantic(
        id="Diagnostic",
        ref="schema:Diagnostic",
        text="""A medical device used for diagnostic purposes.""",
    )

    SERVICE_OUTPUT = Semantic(
        id="serviceOutput",
        ref="schema:serviceOutput",
        text="""The tangible thing generated by the service, e.g. a passport, permit, etc.""",
    )

    NERVE = Semantic(
        id="Nerve",
        ref="schema:Nerve",
        text="""A common pathway for the electrochemical nerve impulses that are transmitted along each of the axons.""",
    )

    REQUIRED_MAX_AGE = Semantic(
        id="requiredMaxAge",
        ref="schema:requiredMaxAge",
        text="""Audiences defined by a person\'s maximum age.""",
    )

    DRIVING_SCHOOL_VEHICLE_USAGE = Semantic(
        id="DrivingSchoolVehicleUsage",
        ref="schema:DrivingSchoolVehicleUsage",
        text="""Indicates the usage of the vehicle for driving school.""",
    )

    TELEVISION_STATION = Semantic(
        id="TelevisionStation",
        ref="schema:TelevisionStation",
        text="""A television station.""",
    )

    SHIPPING_LABEL = Semantic(
        id="shippingLabel",
        ref="schema:shippingLabel",
        text="""Label to match an [[OfferShippingDetails]] with a [[ShippingRateSettings]] (within the context of a [[shippingSettingsLink]] cross-reference).""",
    )

    LANGUAGE = Semantic(
        id="language",
        ref="schema:language",
        text="""A sub property of instrument. The language used on this action.""",
    )

    OSTEOPATHIC = Semantic(
        id="Osteopathic",
        ref="schema:Osteopathic",
        text="""A system of medicine focused on promoting the body\'s innate ability to heal itself.""",
    )

    UNDER_NAME = Semantic(
        id="underName",
        ref="schema:underName",
        text="""The person or organization the reservation or ticket is for.""",
    )

    WEARABLE_SIZE_GROUP_MENS = Semantic(
        id="WearableSizeGroupMens",
        ref="schema:WearableSizeGroupMens",
        text="""Size group "Mens" for wearables.""",
    )

    COLLECTION_PAGE = Semantic(
        id="CollectionPage",
        ref="schema:CollectionPage",
        text="""Web page type: Collection page.""",
    )

    QUESTION = Semantic(
        id="Question",
        ref="schema:Question",
        text="""A specific question - e.g. from a user seeking answers online, or collected in a Frequently Asked Questions (FAQ) document.""",
    )

    SERIAL_NUMBER = Semantic(
        id="serialNumber",
        ref="schema:serialNumber",
        text="""The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.""",
    )

    SUBSTANCE = Semantic(
        id="Substance",
        ref="schema:Substance",
        text="""Any matter of defined composition that has discrete existence, whose origin may be biological, mineral or chemical.""",
    )

    DATELINE = Semantic(
        id="dateline",
        ref="schema:dateline",
        text="""A [dateline](https://en.wikipedia.org/wiki/Dateline) is a brief piece of text included in news articles that describes where and when the story was written or filed though the date is often omitted. Sometimes only a placename is provided.

Structured representations of dateline-related information can also be expressed more explicitly using [[locationCreated]] (which represents where a work was created e.g. where a news report was written).  For location depicted or described in the content, use [[contentLocation]].

Dateline summaries are oriented more towards human readers than towards automated processing, and can vary substantially. Some examples: "BEIRUT, Lebanon, June 2.", "Paris, France", "December 19, 2017 11:43AM Reporting from Washington", "Beijing/Moscow", "QUEZON CITY, Philippines".
      """,
    )

    ONLINE_ONLY = Semantic(
        id="OnlineOnly",
        ref="schema:OnlineOnly",
        text="""Indicates that the item is available only online.""",
    )

    TRANSIT_TIME = Semantic(
        id="transitTime",
        ref="schema:transitTime",
        text="""The typical delay the order has been sent for delivery and the goods reach the final customer. Typical properties: minValue, maxValue, unitCode (d for DAY).""",
    )

    ALUMNI_OF = Semantic(
        id="alumniOf",
        ref="schema:alumniOf",
        text="""An organization that the person is an alumni of.""",
    )

    CONTENT_TYPE = Semantic(
        id="contentType",
        ref="schema:contentType",
        text="""The supported content type(s) for an EntryPoint response.""",
    )

    BENEFITS = Semantic(
        id="benefits",
        ref="schema:benefits",
        text="""Description of benefits associated with the job.""",
    )

    CHILD_MIN_AGE = Semantic(
        id="childMinAge", ref="schema:childMinAge", text="""Minimal age of the child."""
    )

    FUNDER = Semantic(
        id="funder",
        ref="schema:funder",
        text="""A person or organization that supports (sponsors) something through some kind of financial contribution.""",
    )

    ACCOMMODATION = Semantic(
        id="Accommodation",
        ref="schema:Accommodation",
        text="""An accommodation is a place that can accommodate human beings, e.g. a hotel room, a camping pitch, or a meeting room. Many accommodations are for overnight stays, but this is not a mandatory requirement.
For more specific types of accommodations not defined in schema.org, one can use additionalType with external vocabularies.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
""",
    )

    CVD_NUM_TOT_BEDS = Semantic(
        id="cvdNumTotBeds",
        ref="schema:cvdNumTotBeds",
        text="""numtotbeds - ALL HOSPITAL BEDS: Total number of all Inpatient and outpatient beds, including all staffed,ICU, licensed, and overflow (surge) beds used for inpatients or outpatients.""",
    )

    GLOBAL_LOCATION_NUMBER = Semantic(
        id="globalLocationNumber",
        ref="schema:globalLocationNumber",
        text="""The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.""",
    )

    GAS_STATION = Semantic(
        id="GasStation", ref="schema:GasStation", text="""A gas station."""
    )

    ARCHIVE_HELD = Semantic(
        id="archiveHeld",
        ref="schema:archiveHeld",
        text="""Collection, [fonds](https://en.wikipedia.org/wiki/Fonds), or item held, kept or maintained by an [[ArchiveOrganization]].""",
    )

    PEDIATRIC = Semantic(
        id="Pediatric",
        ref="schema:Pediatric",
        text="""A specific branch of medical science that specializes in the care of infants, children and adolescents.""",
    )

    EVIDENCE_LEVEL_C = Semantic(
        id="EvidenceLevelC",
        ref="schema:EvidenceLevelC",
        text="""Only consensus opinion of experts, case studies, or standard-of-care.""",
    )

    MULTI_PLAYER = Semantic(
        id="MultiPlayer",
        ref="schema:MultiPlayer",
        text="""Play mode: MultiPlayer. Requiring or allowing multiple human players to play simultaneously.""",
    )

    ITEM_LIST_UNORDERED = Semantic(
        id="ItemListUnordered",
        ref="schema:ItemListUnordered",
        text="""An ItemList ordered with no explicit order.""",
    )

    NUMBER_OF_PARTIAL_BATHROOMS = Semantic(
        id="numberOfPartialBathrooms",
        ref="schema:numberOfPartialBathrooms",
        text="""Number of partial bathrooms - The total number of half and ¼ bathrooms in an [[Accommodation]]. This corresponds to the [BathroomsPartial field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsPartial+Field). """,
    )

    MESSAGE = Semantic(
        id="Message",
        ref="schema:Message",
        text="""A single message from a sender to one or more organizations or people.""",
    )

    TENNIS_COMPLEX = Semantic(
        id="TennisComplex", ref="schema:TennisComplex", text="""A tennis complex."""
    )

    DOES_NOT_SHIP = Semantic(
        id="doesNotShip",
        ref="schema:doesNotShip",
        text="""Indicates when shipping to a particular [[shippingDestination]] is not available.""",
    )

    MEDICAL_CONTRAINDICATION = Semantic(
        id="MedicalContraindication",
        ref="schema:MedicalContraindication",
        text="""A condition or factor that serves as a reason to withhold a certain medical therapy. Contraindications can be absolute (there are no reasonable circumstances for undertaking a course of action) or relative (the patient is at higher risk of complications, but that these risks may be outweighed by other considerations or mitigated by other measures).""",
    )

    CVD_NUM_C19_DIED = Semantic(
        id="cvdNumC19Died",
        ref="schema:cvdNumC19Died",
        text="""numc19died - DEATHS: Patients with suspected or confirmed COVID-19 who died in the hospital, ED, or any overflow location.""",
    )

    LEGISLATION_DATE = Semantic(
        id="legislationDate",
        ref="schema:legislationDate",
        text="""The date of adoption or signature of the legislation. This is the date at which the text is officially aknowledged to be a legislation, even though it might not even be published or in force.""",
    )

    MEDIA_GALLERY = Semantic(
        id="MediaGallery",
        ref="schema:MediaGallery",
        text="""Web page type: Media gallery page. A mixed-media page that can contains media such as images, videos, and other multimedia.""",
    )

    REGISTER_ACTION = Semantic(
        id="RegisterAction",
        ref="schema:RegisterAction",
        text="""The act of registering to be a user of a service, product or web page.\\n\\nRelated actions:\\n\\n* [[JoinAction]]: Unlike JoinAction, RegisterAction implies you are registering to be a user of a service, *not* a group/team of people.\\n* [FollowAction]]: Unlike FollowAction, RegisterAction doesn\'t imply that the agent is expecting to poll for updates from the object.\\n* [[SubscribeAction]]: Unlike SubscribeAction, RegisterAction doesn\'t imply that the agent is expecting updates from the object.""",
    )

    AMP_STORY = Semantic(
        id="AmpStory",
        ref="schema:AmpStory",
        text="""A creative work with a visual storytelling format intended to be viewed online, particularly on mobile devices.""",
    )

    TYPICAL_CREDITS_PER_TERM = Semantic(
        id="typicalCreditsPerTerm",
        ref="schema:typicalCreditsPerTerm",
        text="""The number of credits or units a full-time student would be expected to take in 1 term however \'term\' is defined by the institution.""",
    )

    ILLUSTRATOR = Semantic(
        id="illustrator",
        ref="schema:illustrator",
        text="""The illustrator of the book.""",
    )

    EXERCISE_PLAN = Semantic(
        id="ExercisePlan",
        ref="schema:ExercisePlan",
        text="""Fitness-related activity designed for a specific health-related purpose, including defined exercise routines as well as activity prescribed by a clinician.""",
    )

    CHILD_CARE = Semantic(
        id="ChildCare", ref="schema:ChildCare", text="""A Childcare center."""
    )

    MEDIA_MANIPULATION_RATING_ENUMERATION = Semantic(
        id="MediaManipulationRatingEnumeration",
        ref="schema:MediaManipulationRatingEnumeration",
        text=""" Codes for use with the [[mediaAuthenticityCategory]] property, indicating the authenticity of a media object (in the context of how it was published or shared). In general these codes are not mutually exclusive, although some combinations (such as \'original\' versus \'transformed\', \'edited\' and \'staged\') would be contradictory if applied in the same [[MediaReview]]. Note that the application of these codes is with regard to a piece of media shared or published in a particular context.""",
    )

    STAGE = Semantic(
        id="stage",
        ref="schema:stage",
        text="""The stage of the condition, if applicable.""",
    )

    PRODUCT_I_D = Semantic(
        id="productID",
        ref="schema:productID",
        text="""The product identifier, such as ISBN. For example: ``` meta itemprop="productID" content="isbn:123-456-789" ```.""",
    )

    COMEDY_CLUB = Semantic(
        id="ComedyClub", ref="schema:ComedyClub", text="""A comedy club."""
    )

    SPEAKABLE = Semantic(
        id="speakable",
        ref="schema:speakable",
        text="""Indicates sections of a Web page that are particularly \'speakable\' in the sense of being highlighted as being especially appropriate for text-to-speech conversion. Other sections of a page may also be usefully spoken in particular circumstances; the \'speakable\' property serves to indicate the parts most likely to be generally useful for speech.

The *speakable* property can be repeated an arbitrary number of times, with three kinds of possible \'content-locator\' values:

1.) *id-value* URL references - uses *id-value* of an element in the page being annotated. The simplest use of *speakable* has (potentially relative) URL values, referencing identified sections of the document concerned.

2.) CSS Selectors - addresses content in the annotated page, eg. via class attribute. Use the [[cssSelector]] property.

3.)  XPaths - addresses content via XPaths (assuming an XML view of the content). Use the [[xpath]] property.


For more sophisticated markup of speakable sections beyond simple ID references, either CSS selectors or XPath expressions to pick out document section(s) as speakable. For this
we define a supporting type, [[SpeakableSpecification]]  which is defined to be a possible value of the *speakable* property.
         """,
    )

    SEND_ACTION = Semantic(
        id="SendAction",
        ref="schema:SendAction",
        text="""The act of physically/electronically dispatching an object for transfer from an origin to a destination.Related actions:\\n\\n* [[ReceiveAction]]: The reciprocal of SendAction.\\n* [[GiveAction]]: Unlike GiveAction, SendAction does not imply the transfer of ownership (e.g. I can send you my laptop, but I\'m not necessarily giving it to you).""",
    )

    YEAR_BUILT = Semantic(
        id="yearBuilt",
        ref="schema:yearBuilt",
        text="""The year an [[Accommodation]] was constructed. This corresponds to the [YearBuilt field in RESO](https://ddwiki.reso.org/display/DDW17/YearBuilt+Field). """,
    )

    PRE_OP = Semantic(
        id="preOp",
        ref="schema:preOp",
        text="""A description of the workup, testing, and other preparations required before implanting this device.""",
    )

    THESIS = Semantic(
        id="Thesis",
        ref="schema:Thesis",
        text="""A thesis or dissertation document submitted in support of candidature for an academic degree or professional qualification.""",
    )

    SHORT_STORY = Semantic(
        id="ShortStory",
        ref="schema:ShortStory",
        text="""Short story or tale. A brief work of literature, usually written in narrative prose.""",
    )

    SCHEDULE_ACTION = Semantic(
        id="ScheduleAction",
        ref="schema:ScheduleAction",
        text="""Scheduling future actions, events, or tasks.\\n\\nRelated actions:\\n\\n* [[ReserveAction]]: Unlike ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task, etc) towards a time slot / spatial allocation.""",
    )

    MODEL = Semantic(
        id="model",
        ref="schema:model",
        text="""The model of the product. Use with the URL of a ProductModel or a textual representation of the model identifier. The URL of the ProductModel can be from an external source. It is recommended to additionally provide strong product identifiers via the gtin8/gtin13/gtin14 and mpn properties.""",
    )

    AYURVEDIC = Semantic(
        id="Ayurvedic",
        ref="schema:Ayurvedic",
        text="""A system of medicine that originated in India over thousands of years and that focuses on integrating and balancing the body, mind, and spirit.""",
    )

    DEPTH = Semantic(id="depth", ref="schema:depth", text="""The depth of the item.""")

    NONPROFIT501C26 = Semantic(
        id="Nonprofit501c26",
        ref="schema:Nonprofit501c26",
        text="""Nonprofit501c26: Non-profit type referring to State-Sponsored Organizations Providing Health Coverage for High-Risk Individuals.""",
    )

    WORK_PRESENTED = Semantic(
        id="workPresented",
        ref="schema:workPresented",
        text="""The movie presented during this event.""",
    )

    HAS_DRIVE_THROUGH_SERVICE = Semantic(
        id="hasDriveThroughService",
        ref="schema:hasDriveThroughService",
        text="""Indicates whether some facility (e.g. [[FoodEstablishment]], [[CovidTestingFacility]]) offers a service that can be used by driving through in a car. In the case of [[CovidTestingFacility]] such facilities could potentially help with social distancing from other potentially-infected users.""",
    )

    EXCHANGE_RATE_SPREAD = Semantic(
        id="exchangeRateSpread",
        ref="schema:exchangeRateSpread",
        text="""The difference between the price at which a broker or other intermediary buys and sells foreign currency.""",
    )

    MAXIMUM_ATTENDEE_CAPACITY = Semantic(
        id="maximumAttendeeCapacity",
        ref="schema:maximumAttendeeCapacity",
        text="""The total number of individuals that may attend an event or venue.""",
    )

    IN_PLAYLIST = Semantic(
        id="inPlaylist",
        ref="schema:inPlaylist",
        text="""The playlist to which this recording belongs.""",
    )

    RADIATION_THERAPY = Semantic(
        id="RadiationTherapy",
        ref="schema:RadiationTherapy",
        text="""A process of care using radiation aimed at improving a health condition.""",
    )

    NATURAL_PROGRESSION = Semantic(
        id="naturalProgression",
        ref="schema:naturalProgression",
        text="""The expected progression of the condition if it is not treated and allowed to progress naturally.""",
    )

    NUMBER_OF_SEASONS = Semantic(
        id="numberOfSeasons",
        ref="schema:numberOfSeasons",
        text="""The number of seasons in this series.""",
    )

    EMPLOYEES = Semantic(
        id="employees",
        ref="schema:employees",
        text="""People working for this organization.""",
    )

    E_U_ENERGY_EFFICIENCY_ENUMERATION = Semantic(
        id="EUEnergyEfficiencyEnumeration",
        ref="schema:EUEnergyEfficiencyEnumeration",
        text="""Enumerates the EU energy efficiency classes A-G as well as A+, A++, and A+++ as defined in EU directive 2017/1369.""",
    )

    PREDECESSOR_OF = Semantic(
        id="predecessorOf",
        ref="schema:predecessorOf",
        text="""A pointer from a previous, often discontinued variant of the product to its newer variant.""",
    )

    DEPARTURE_PLATFORM = Semantic(
        id="departurePlatform",
        ref="schema:departurePlatform",
        text="""The platform from which the train departs.""",
    )

    EXPIRES = Semantic(
        id="expires",
        ref="schema:expires",
        text="""Date the content expires and is no longer useful or available. For example a [[VideoObject]] or [[NewsArticle]] whose availability or relevance is time-limited, or a [[ClaimReview]] fact check whose publisher wants to indicate that it may no longer be relevant (or helpful to highlight) after some date.""",
    )

    SEAT_NUMBER = Semantic(
        id="seatNumber",
        ref="schema:seatNumber",
        text="""The location of the reserved seat (e.g., 27).""",
    )

    DISCOVER_ACTION = Semantic(
        id="DiscoverAction",
        ref="schema:DiscoverAction",
        text="""The act of discovering/finding an object.""",
    )

    MONDAY = Semantic(
        id="Monday",
        ref="schema:Monday",
        text="""The day of the week between Sunday and Tuesday.""",
    )

    ESTIMATES_RISK_OF = Semantic(
        id="estimatesRiskOf",
        ref="schema:estimatesRiskOf",
        text="""The condition, complication, or symptom whose risk is being estimated.""",
    )

    RECOMMENDED_DOSE_SCHEDULE = Semantic(
        id="RecommendedDoseSchedule",
        ref="schema:RecommendedDoseSchedule",
        text="""A recommended dosing schedule for a drug or supplement as prescribed or recommended by an authority or by the drug/supplement\'s manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.""",
    )

    CUTOFF_TIME = Semantic(
        id="cutoffTime",
        ref="schema:cutoffTime",
        text="""Order cutoff time allows merchants to describe the time after which they will no longer process orders received on that day. For orders processed after cutoff time, one day gets added to the delivery time estimate. This property is expected to be most typically used via the [[ShippingRateSettings]] publication pattern. The time is indicated using the ISO-8601 Time format, e.g. "23:30:00-05:00" would represent 6:30 pm Eastern Standard Time (EST) which is 5 hours behind Coordinated Universal Time (UTC).""",
    )

    REQUIRED_COLLATERAL = Semantic(
        id="requiredCollateral",
        ref="schema:requiredCollateral",
        text="""Assets required to secure loan or credit repayments. It may take form of third party pledge, goods, financial instruments (cash, securities, etc.)""",
    )

    WEIGHT = Semantic(
        id="weight",
        ref="schema:weight",
        text="""The weight of the product or person.""",
    )

    GTIN13 = Semantic(
        id="gtin13",
        ref="schema:gtin13",
        text="""The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.""",
    )

    PARTIALLY_IN_FORCE = Semantic(
        id="PartiallyInForce",
        ref="schema:PartiallyInForce",
        text="""Indicates that parts of the legislation are in force, and parts are not.""",
    )

    ENERGY_EFFICIENCY_SCALE_MIN = Semantic(
        id="energyEfficiencyScaleMin",
        ref="schema:energyEfficiencyScaleMin",
        text="""Specifies the least energy efficient class on the regulated EU energy consumption scale for the product category a product belongs to. For example, energy consumption for televisions placed on the market after January 1, 2020 is scaled from D to A+++.""",
    )

    PROVIDER_MOBILITY = Semantic(
        id="providerMobility",
        ref="schema:providerMobility",
        text="""Indicates the mobility of a provided service (e.g. \'static\', \'dynamic\').""",
    )

    SIZE_GROUP = Semantic(
        id="sizeGroup",
        ref="schema:sizeGroup",
        text='''The size group (also known as "size type") for a product\'s size. Size groups are common in the fashion industry to define size segments and suggested audiences for wearable products. Multiple values can be combined, for example "men\'s big and tall", "petite maternity" or "regular"''',
    )

    BANK_OR_CREDIT_UNION = Semantic(
        id="BankOrCreditUnion",
        ref="schema:BankOrCreditUnion",
        text="""Bank or credit union.""",
    )

    MEDICAL_SYMPTOM = Semantic(
        id="MedicalSymptom",
        ref="schema:MedicalSymptom",
        text="""Any complaint sensed and expressed by the patient (therefore defined as subjective)  like stomachache, lower-back pain, or fatigue.""",
    )

    HEALTH_ASPECT_ENUMERATION = Semantic(
        id="HealthAspectEnumeration",
        ref="schema:HealthAspectEnumeration",
        text="""HealthAspectEnumeration enumerates several aspects of health content online, each of which might be described using [[hasHealthAspect]] and [[HealthTopicContent]].""",
    )

    ITEM_SHIPPED = Semantic(
        id="itemShipped", ref="schema:itemShipped", text="""Item(s) being shipped."""
    )

    ABRIDGED = Semantic(
        id="abridged",
        ref="schema:abridged",
        text="""Indicates whether the book is an abridged edition.""",
    )

    DIVERSITY_POLICY = Semantic(
        id="diversityPolicy",
        ref="schema:diversityPolicy",
        text="""Statement on diversity policy by an [[Organization]] e.g. a [[NewsMediaOrganization]]. For a [[NewsMediaOrganization]], a statement describing the newsroom’s diversity policy on both staffing and sources, typically providing staffing data.""",
    )

    SCHEDULE_TIMEZONE = Semantic(
        id="scheduleTimezone",
        ref="schema:scheduleTimezone",
        text="""Indicates the timezone for which the time(s) indicated in the [[Schedule]] are given. The value provided should be among those listed in the IANA Time Zone Database.""",
    )

    MATH_SOLVER = Semantic(
        id="MathSolver",
        ref="schema:MathSolver",
        text="""A math solver which is capable of solving a subset of mathematical problems.""",
    )

    CANDIDATE = Semantic(
        id="candidate",
        ref="schema:candidate",
        text="""A sub property of object. The candidate subject of this action.""",
    )

    FUNCTIONAL_CLASS = Semantic(
        id="functionalClass",
        ref="schema:functionalClass",
        text="""The degree of mobility the joint allows.""",
    )

    RETURN_FEES_CUSTOMER_RESPONSIBILITY = Semantic(
        id="ReturnFeesCustomerResponsibility",
        ref="schema:ReturnFeesCustomerResponsibility",
        text="""Specifies that product returns must be paid for, and are the responsibility of, the customer.""",
    )

    VINYL_FORMAT = Semantic(
        id="VinylFormat", ref="schema:VinylFormat", text="""VinylFormat."""
    )

    PRICE_VALID_UNTIL = Semantic(
        id="priceValidUntil",
        ref="schema:priceValidUntil",
        text="""The date after which the price is no longer available.""",
    )

    DIGITAL_AUDIO_TAPE_FORMAT = Semantic(
        id="DigitalAudioTapeFormat",
        ref="schema:DigitalAudioTapeFormat",
        text="""DigitalAudioTapeFormat.""",
    )

    MEDICAL_SIGN = Semantic(
        id="MedicalSign",
        ref="schema:MedicalSign",
        text="""Any physical manifestation of a person\'s medical condition discoverable by objective diagnostic tests or physical examination.""",
    )

    DISCOUNT_CODE = Semantic(
        id="discountCode",
        ref="schema:discountCode",
        text="""Code used to redeem a discount.""",
    )

    BODY_MEASUREMENT_WEIGHT = Semantic(
        id="BodyMeasurementWeight",
        ref="schema:BodyMeasurementWeight",
        text="""Body weight. Used, for example, to measure pantyhose.""",
    )

    USER_INTERACTION_COUNT = Semantic(
        id="userInteractionCount",
        ref="schema:userInteractionCount",
        text="""The number of interactions for the CreativeWork using the WebSite or SoftwareApplication.""",
    )

    GENRE = Semantic(
        id="genre",
        ref="schema:genre",
        text="""Genre of the creative work, broadcast channel or group.""",
    )

    CONTACT_TYPE = Semantic(
        id="contactType",
        ref="schema:contactType",
        text="""A person or organization can have different contact points, for different purposes. For example, a sales contact point, a PR contact point and so on. This property is used to specify the kind of contact point.""",
    )

    WORK_TRANSLATION = Semantic(
        id="workTranslation",
        ref="schema:workTranslation",
        text="""A work that is a translation of the content of this work. e.g. 西遊記 has an English workTranslation “Journey to the West”,a German workTranslation “Monkeys Pilgerfahrt” and a Vietnamese  translation Tây du ký bình khảo.""",
    )

    NERVE = Semantic(
        id="nerve",
        ref="schema:nerve",
        text="""The underlying innervation associated with the muscle.""",
    )

    MASS = Semantic(
        id="Mass",
        ref="schema:Mass",
        text="""Properties that take Mass as values are of the form \'&lt;Number&gt; &lt;Mass unit of measure&gt;\'. E.g., \'7 kg\'.""",
    )

    DURING_MEDIA = Semantic(
        id="duringMedia",
        ref="schema:duringMedia",
        text="""A media object representing the circumstances while performing this direction.""",
    )

    FINANCIAL_PRODUCT = Semantic(
        id="FinancialProduct",
        ref="schema:FinancialProduct",
        text="""A product provided to consumers and businesses by financial institutions such as banks, insurance companies, brokerage firms, consumer finance companies, and investment companies which comprise the financial services industry.""",
    )

    SOFTWARE_APPLICATION = Semantic(
        id="SoftwareApplication",
        ref="schema:SoftwareApplication",
        text="""A software application.""",
    )

    WEARABLE_SIZE_SYSTEM_ENUMERATION = Semantic(
        id="WearableSizeSystemEnumeration",
        ref="schema:WearableSizeSystemEnumeration",
        text="""Enumerates common size systems specific for wearable products""",
    )

    FLEXIBILITY = Semantic(
        id="Flexibility",
        ref="schema:Flexibility",
        text="""Physical activity that is engaged in to improve joint and muscle flexibility.""",
    )

    PALLIATIVE_PROCEDURE = Semantic(
        id="PalliativeProcedure",
        ref="schema:PalliativeProcedure",
        text="""A medical procedure intended primarily for palliative purposes, aimed at relieving the symptoms of an underlying health condition.""",
    )

    REVIEW_COUNT = Semantic(
        id="reviewCount",
        ref="schema:reviewCount",
        text="""The count of total number of reviews.""",
    )

    TRAVEL_AGENCY = Semantic(
        id="TravelAgency", ref="schema:TravelAgency", text="""A travel agency."""
    )

    RECYCLING_CENTER = Semantic(
        id="RecyclingCenter",
        ref="schema:RecyclingCenter",
        text="""A recycling center.""",
    )

    READONLY_VALUE = Semantic(
        id="readonlyValue",
        ref="schema:readonlyValue",
        text="""Whether or not a property is mutable.  Default is false. Specifying this for a property that also has a value makes it act similar to a "hidden" input in an HTML form.""",
    )

    PHOTO = Semantic(
        id="photo", ref="schema:photo", text="""A photograph of this place."""
    )

    TAXI_RESERVATION = Semantic(
        id="TaxiReservation",
        ref="schema:TaxiReservation",
        text="""A reservation for a taxi.\\n\\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].""",
    )

    SPORT = Semantic(
        id="sport", ref="schema:sport", text="""A type of sport (e.g. Baseball)."""
    )

    COMIC_COVER_ART = Semantic(
        id="ComicCoverArt",
        ref="schema:ComicCoverArt",
        text="""The artwork on the cover of a comic.""",
    )

    DEPARTURE_BUS_STOP = Semantic(
        id="departureBusStop",
        ref="schema:departureBusStop",
        text="""The stop or station from which the bus departs.""",
    )

    VALUE_MIN_LENGTH = Semantic(
        id="valueMinLength",
        ref="schema:valueMinLength",
        text="""Specifies the minimum allowed range for number of characters in a literal value.""",
    )

    PRODUCT_MODEL = Semantic(
        id="ProductModel",
        ref="schema:ProductModel",
        text="""A datasheet or vendor specification of a product (in the sense of a prototypical description).""",
    )

    RECIPE = Semantic(
        id="recipe",
        ref="schema:recipe",
        text="""A sub property of instrument. The recipe/instructions used to perform the action.""",
    )

    HEALTH_PLAN_COINSURANCE_OPTION = Semantic(
        id="healthPlanCoinsuranceOption",
        ref="schema:healthPlanCoinsuranceOption",
        text="""Whether the coinsurance applies before or after deductible, etc. TODO: Is this a closed set?""",
    )

    ORIGINATES_FROM = Semantic(
        id="originatesFrom",
        ref="schema:originatesFrom",
        text="""The vasculature the lymphatic structure originates, or afferents, from.""",
    )

    CVD_NUM_C19_H_O_PATS = Semantic(
        id="cvdNumC19HOPats",
        ref="schema:cvdNumC19HOPats",
        text="""numc19hopats - HOSPITAL ONSET: Patients hospitalized in an NHSN inpatient care location with onset of suspected or confirmed COVID-19 14 or more days after hospitalization.""",
    )

    PRODUCTION_DATE = Semantic(
        id="productionDate",
        ref="schema:productionDate",
        text="""The date of production of the item, e.g. vehicle.""",
    )

    WEARABLE_SIZE_SYSTEM_CONTINENTAL = Semantic(
        id="WearableSizeSystemContinental",
        ref="schema:WearableSizeSystemContinental",
        text="""Continental size system for wearables.""",
    )

    AGGREGATE_RATING = Semantic(
        id="aggregateRating",
        ref="schema:aggregateRating",
        text="""The overall rating, based on a collection of reviews or ratings, of the item.""",
    )

    BOARDING_POLICY = Semantic(
        id="boardingPolicy",
        ref="schema:boardingPolicy",
        text="""The type of boarding policy used by the airline (e.g. zone-based or group-based).""",
    )

    DIET_NUTRITION = Semantic(
        id="DietNutrition",
        ref="schema:DietNutrition",
        text="""Dietetic and nutrition as a medical specialty.""",
    )

    ADMINISTRATION_ROUTE = Semantic(
        id="administrationRoute",
        ref="schema:administrationRoute",
        text="""A route by which this drug may be administered, e.g. \'oral\'.""",
    )

    MILEAGE_FROM_ODOMETER = Semantic(
        id="mileageFromOdometer",
        ref="schema:mileageFromOdometer",
        text="""The total distance travelled by the particular vehicle since its initial production, as read from its odometer.\\n\\nTypical unit code(s): KMT for kilometers, SMI for statute miles""",
    )

    ELIGIBLE_CUSTOMER_TYPE = Semantic(
        id="eligibleCustomerType",
        ref="schema:eligibleCustomerType",
        text="""The type(s) of customers for which the given offer is valid.""",
    )

    DELIVERY_METHOD = Semantic(
        id="DeliveryMethod",
        ref="schema:DeliveryMethod",
        text="""A delivery method is a standardized procedure for transferring the product or service to the destination of fulfillment chosen by the customer. Delivery methods are characterized by the means of transportation used, and by the organization or group that is the contracting party for the sending organization or person.\\n\\nCommonly used values:\\n\\n* http://purl.org/goodrelations/v1#DeliveryModeDirectDownload\\n* http://purl.org/goodrelations/v1#DeliveryModeFreight\\n* http://purl.org/goodrelations/v1#DeliveryModeMail\\n* http://purl.org/goodrelations/v1#DeliveryModeOwnFleet\\n* http://purl.org/goodrelations/v1#DeliveryModePickUp\\n* http://purl.org/goodrelations/v1#DHL\\n* http://purl.org/goodrelations/v1#FederalExpress\\n* http://purl.org/goodrelations/v1#UPS
        """,
    )

    CONTAINED_IN = Semantic(
        id="containedIn",
        ref="schema:containedIn",
        text="""The basic containment relation between a place and one that contains it.""",
    )

    TARGET_POPULATION = Semantic(
        id="targetPopulation",
        ref="schema:targetPopulation",
        text="""Characteristics of the population for which this is intended, or which typically uses it, e.g. \'adults\'.""",
    )

    AUDIENCE_TYPE = Semantic(
        id="audienceType",
        ref="schema:audienceType",
        text="""The target group associated with a given audience (e.g. veterans, car owners, musicians, etc.).""",
    )

    MERCHANT_RETURN_POLICY = Semantic(
        id="MerchantReturnPolicy",
        ref="schema:MerchantReturnPolicy",
        text="""A MerchantReturnPolicy provides information about product return policies associated with an [[Organization]], [[Product]], or [[Offer]].""",
    )

    PROPERTY_VALUE = Semantic(
        id="PropertyValue",
        ref="schema:PropertyValue",
        text="""A property-value pair, e.g. representing a feature of a product or place. Use the \'name\' property for the name of the property. If there is an additional human-readable version of the value, put that into the \'description\' property.\\n\\n Always use specific schema.org properties when a) they exist and b) you can populate them. Using PropertyValue as a substitute will typically not trigger the same effect as using the original, specific property.
    """,
    )

    POSTAL_CODE = Semantic(
        id="postalCode",
        ref="schema:postalCode",
        text="""The postal code. For example, 94043.""",
    )

    QUARANTINE_GUIDELINES = Semantic(
        id="quarantineGuidelines",
        ref="schema:quarantineGuidelines",
        text="""Guidelines about quarantine rules, e.g. in the context of a pandemic.""",
    )

    WRITE_PERMISSION = Semantic(
        id="WritePermission",
        ref="schema:WritePermission",
        text="""Permission to write or edit the document.""",
    )

    KNOWS_LANGUAGE = Semantic(
        id="knowsLanguage",
        ref="schema:knowsLanguage",
        text="""Of a [[Person]], and less typically of an [[Organization]], to indicate a known language. We do not distinguish skill levels or reading/writing/speaking/signing here. Use language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47).""",
    )

    EPISODE_NUMBER = Semantic(
        id="episodeNumber",
        ref="schema:episodeNumber",
        text="""Position of the episode within an ordered group of episodes.""",
    )

    EMBEDDED_TEXT_CAPTION = Semantic(
        id="embeddedTextCaption",
        ref="schema:embeddedTextCaption",
        text="""Represents textual captioning from a [[MediaObject]], e.g. text of a \'meme\'.""",
    )

    APARTMENT = Semantic(
        id="Apartment",
        ref="schema:Apartment",
        text="""An apartment (in American English) or flat (in British English) is a self-contained housing unit (a type of residential real estate) that occupies only part of a building (Source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Apartment">http://en.wikipedia.org/wiki/Apartment</a>).""",
    )

    MEDICAL_OBSERVATIONAL_STUDY = Semantic(
        id="MedicalObservationalStudy",
        ref="schema:MedicalObservationalStudy",
        text="""An observational study is a type of medical study that attempts to infer the possible effect of a treatment through observation of a cohort of subjects over a period of time. In an observational study, the assignment of subjects into treatment groups versus control groups is outside the control of the investigator. This is in contrast with controlled studies, such as the randomized controlled trials represented by MedicalTrial, where each subject is randomly assigned to a treatment group or a control group before the start of the treatment.""",
    )

    COURSE_WORKLOAD = Semantic(
        id="courseWorkload",
        ref="schema:courseWorkload",
        text="""The amount of work expected of students taking the course, often provided as a figure per week or per month, and may be broken down by type. For example, "2 hours of lectures, 1 hour of lab work and 3 hours of independent study per week".""",
    )

    TRANSMISSION_METHOD = Semantic(
        id="transmissionMethod",
        ref="schema:transmissionMethod",
        text="""How the disease spreads, either as a route or vector, for example \'direct contact\', \'Aedes aegypti\', etc.""",
    )

    BOWLING_ALLEY = Semantic(
        id="BowlingAlley", ref="schema:BowlingAlley", text="""A bowling alley."""
    )

    ALBUM = Semantic(id="album", ref="schema:album", text="""A music album.""")

    PRICE_SPECIFICATION = Semantic(
        id="PriceSpecification",
        ref="schema:PriceSpecification",
        text="""A structured value representing a price or price range. Typically, only the subclasses of this type are used for markup. It is recommended to use [[MonetaryAmount]] to describe independent amounts of money such as a salary, credit card limits, etc.""",
    )

    BITRATE = Semantic(
        id="bitrate", ref="schema:bitrate", text="""The bitrate of the media object."""
    )

    MAY_TREAT_HEALTH_ASPECT = Semantic(
        id="MayTreatHealthAspect",
        ref="schema:MayTreatHealthAspect",
        text="""Related topics may be treated by a Topic.""",
    )

    ENERGY_EFFICIENCY_ENUMERATION = Semantic(
        id="EnergyEfficiencyEnumeration",
        ref="schema:EnergyEfficiencyEnumeration",
        text="""Enumerates energy efficiency levels (also known as "classes" or "ratings") and certifications that are part of several international energy efficiency standards.""",
    )

    ACRISS_CODE = Semantic(
        id="acrissCode",
        ref="schema:acrissCode",
        text="""The ACRISS Car Classification Code is a code used by many car rental companies, for classifying vehicles. ACRISS stands for Association of Car Rental Industry Systems and Standards.""",
    )

    NET_WORTH = Semantic(
        id="netWorth",
        ref="schema:netWorth",
        text="""The total financial value of the person as calculated by subtracting assets from liabilities.""",
    )

    SPOKEN_BY_CHARACTER = Semantic(
        id="spokenByCharacter",
        ref="schema:spokenByCharacter",
        text="""The (e.g. fictional) character, Person or Organization to whom the quotation is attributed within the containing CreativeWork.""",
    )

    PAY_ACTION = Semantic(
        id="PayAction",
        ref="schema:PayAction",
        text="""An agent pays a price to a participant.""",
    )

    PAYMENT_METHOD_ID = Semantic(
        id="paymentMethodId",
        ref="schema:paymentMethodId",
        text="""An identifier for the method of payment used (e.g. the last 4 digits of the credit card).""",
    )

    F_D_ACATEGORY_X = Semantic(
        id="FDAcategoryX",
        ref="schema:FDAcategoryX",
        text="""A designation by the US FDA signifying that studies in animals or humans have demonstrated fetal abnormalities and/or there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience, and the risks involved in use of the drug in pregnant women clearly outweigh potential benefits.""",
    )

    VEHICLE_IDENTIFICATION_NUMBER = Semantic(
        id="vehicleIdentificationNumber",
        ref="schema:vehicleIdentificationNumber",
        text="""The Vehicle Identification Number (VIN) is a unique serial number used by the automotive industry to identify individual motor vehicles.""",
    )

    CLINCAL_PHARMACOLOGY = Semantic(
        id="clincalPharmacology",
        ref="schema:clincalPharmacology",
        text="""Description of the absorption and elimination of drugs, including their concentration (pharmacokinetics, pK) and biological effects (pharmacodynamics, pD).""",
    )

    STUDY_LOCATION = Semantic(
        id="studyLocation",
        ref="schema:studyLocation",
        text="""The location in which the study is taking/took place.""",
    )

    DIABETIC_DIET = Semantic(
        id="DiabeticDiet",
        ref="schema:DiabeticDiet",
        text="""A diet appropriate for people with diabetes.""",
    )

    HINDU_DIET = Semantic(
        id="HinduDiet",
        ref="schema:HinduDiet",
        text="""A diet conforming to Hindu dietary practices, in particular, beef-free.""",
    )

    SCREENSHOT = Semantic(
        id="screenshot",
        ref="schema:screenshot",
        text="""A link to a screenshot image of the app.""",
    )

    CONFIRM_ACTION = Semantic(
        id="ConfirmAction",
        ref="schema:ConfirmAction",
        text="""The act of notifying someone that a future event/action is going to happen as expected.\\n\\nRelated actions:\\n\\n* [[CancelAction]]: The antonym of ConfirmAction.""",
    )

    SUB_TEST = Semantic(
        id="subTest", ref="schema:subTest", text="""A component test of the panel."""
    )

    AWARD = Semantic(
        id="award", ref="schema:award", text="""An award won by or for this item."""
    )

    FAT_CONTENT = Semantic(
        id="fatContent", ref="schema:fatContent", text="""The number of grams of fat."""
    )

    ATTENDEES = Semantic(
        id="attendees", ref="schema:attendees", text="""A person attending the event."""
    )

    HEALTH_PLAN_DRUG_OPTION = Semantic(
        id="healthPlanDrugOption", ref="schema:healthPlanDrugOption", text="""TODO."""
    )

    CVD_FACILITY_COUNTY = Semantic(
        id="cvdFacilityCounty",
        ref="schema:cvdFacilityCounty",
        text="""Name of the County of the NHSN facility that this data record applies to. Use [[cvdFacilityId]] to identify the facility. To provide other details, [[healthcareReportingData]] can be used on a [[Hospital]] entry.""",
    )

    SERIOUS_ADVERSE_OUTCOME = Semantic(
        id="seriousAdverseOutcome",
        ref="schema:seriousAdverseOutcome",
        text="""A possible serious complication and/or serious side effect of this therapy. Serious adverse outcomes include those that are life-threatening; result in death, disability, or permanent damage; require hospitalization or prolong existing hospitalization; cause congenital anomalies or birth defects; or jeopardize the patient and may require medical or surgical intervention to prevent one of the outcomes in this definition.""",
    )

    DEFINED_REGION = Semantic(
        id="DefinedRegion",
        ref="schema:DefinedRegion",
        text="""A DefinedRegion is a geographic area defined by potentially arbitrary (rather than political, administrative or natural geographical) criteria. Properties are provided for defining a region by reference to sets of postal codes.

Examples: a delivery destination when shopping. Region where regional pricing is configured.

Requirement 1:
Country: US
States: "NY", "CA"

Requirement 2:
Country: US
PostalCode Set: { [94000-94585], [97000, 97999], [13000, 13599]}
{ [12345, 12345], [78945, 78945], }
Region = state, canton, prefecture, autonomous community...
""",
    )

    ENERGY_STAR_ENERGY_EFFICIENCY_ENUMERATION = Semantic(
        id="EnergyStarEnergyEfficiencyEnumeration",
        ref="schema:EnergyStarEnergyEfficiencyEnumeration",
        text="""Used to indicate whether a product is EnergyStar certified.""",
    )

    PERFORMING_ARTS_THEATER = Semantic(
        id="PerformingArtsTheater",
        ref="schema:PerformingArtsTheater",
        text="""A theater or other performing art center.""",
    )

    GOVERNMENT_BENEFITS_INFO = Semantic(
        id="governmentBenefitsInfo",
        ref="schema:governmentBenefitsInfo",
        text="""governmentBenefitsInfo provides information about government benefits associated with a SpecialAnnouncement.""",
    )

    NUMBER = Semantic(
        id="Number",
        ref="schema:Number",
        text="""Data type: Number.\\n\\nUsage guidelines:\\n\\n* Use values from 0123456789 (Unicode \'DIGIT ZERO\' (U+0030) to \'DIGIT NINE\' (U+0039)) rather than superficially similiar Unicode symbols.\\n* Use \'.\' (Unicode \'FULL STOP\' (U+002E)) rather than \',\' to indicate a decimal point. Avoid using these symbols as a readability separator.""",
    )

    EVIDENCE_ORIGIN = Semantic(
        id="evidenceOrigin",
        ref="schema:evidenceOrigin",
        text="""Source of the data used to formulate the guidance, e.g. RCT, consensus opinion, etc.""",
    )

    HAS_MOLECULAR_FUNCTION = Semantic(
        id="hasMolecularFunction",
        ref="schema:hasMolecularFunction",
        text="""Molecular function performed by this BioChemEntity; please use PropertyValue if you want to include any evidence.""",
    )

    BLOG = Semantic(
        id="Blog",
        ref="schema:Blog",
        text="""A [blog](https://en.wikipedia.org/wiki/Blog), sometimes known as a "weblog". Note that the individual posts ([[BlogPosting]]s) in a [[Blog]] are often colloqually referred to by the same term.""",
    )

    ASSEMBLY_VERSION = Semantic(
        id="assemblyVersion",
        ref="schema:assemblyVersion",
        text="""Associated product/technology version. e.g., .NET Framework 4.5.""",
    )

    PROCESSING_TIME = Semantic(
        id="processingTime",
        ref="schema:processingTime",
        text="""Estimated processing time for the service using this channel.""",
    )

    SHARE_ACTION = Semantic(
        id="ShareAction",
        ref="schema:ShareAction",
        text="""The act of distributing content to people for their amusement or edification.""",
    )

    AEROBIC_ACTIVITY = Semantic(
        id="AerobicActivity",
        ref="schema:AerobicActivity",
        text="""Physical activity of relatively low intensity that depends primarily on the aerobic energy-generating process; during activity, the aerobic metabolism uses oxygen to adequately meet energy demands during exercise.""",
    )

    WORKERS_UNION = Semantic(
        id="WorkersUnion",
        ref="schema:WorkersUnion",
        text="""A Workers Union (also known as a Labor Union, Labour Union, or Trade Union) is an organization that promotes the interests of its worker members by collectively bargaining with management, organizing, and political lobbying.""",
    )

    IUPAC_NAME = Semantic(
        id="iupacName",
        ref="schema:iupacName",
        text="""Systematic method of naming chemical compounds as recommended by the International Union of Pure and Applied Chemistry (IUPAC).""",
    )

    FINANCIAL_SERVICE = Semantic(
        id="FinancialService",
        ref="schema:FinancialService",
        text="""Financial services business.""",
    )

    TEMPORAL_COVERAGE = Semantic(
        id="temporalCoverage",
        ref="schema:temporalCoverage",
        text="""The temporalCoverage of a CreativeWork indicates the period that the content applies to, i.e. that it describes, either as a DateTime or as a textual string indicating a time period in [ISO 8601 time interval format](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals). In
      the case of a Dataset it will typically indicate the relevant time period in a precise notation (e.g. for a 2011 census dataset, the year 2011 would be written "2011/2012"). Other forms of content e.g. ScholarlyArticle, Book, TVSeries or TVEpisode may indicate their temporalCoverage in broader terms - textually or via well-known URL.
      Written works such as books may sometimes have precise temporal coverage too, e.g. a work set in 1939 - 1945 can be indicated in ISO 8601 interval format format via "1939/1945".

Open-ended date ranges can be written with ".." in place of the end date. For example, "2015-11/.." indicates a range beginning in November 2015 and with no specified final date. This is tentative and might be updated in future when ISO 8601 is officially updated.""",
    )

    DEVICE = Semantic(
        id="device",
        ref="schema:device",
        text="""Device required to run the application. Used in cases where a specific make/model is required to run the application.""",
    )

    GAME_LOCATION = Semantic(
        id="gameLocation",
        ref="schema:gameLocation",
        text="""Real or fictional location of the game (or part of game).""",
    )

    REAL_ESTATE_AGENT = Semantic(
        id="RealEstateAgent",
        ref="schema:RealEstateAgent",
        text="""A real-estate agent.""",
    )

    MENU_SECTION = Semantic(
        id="MenuSection",
        ref="schema:MenuSection",
        text="""A sub-grouping of food or drink items in a menu. E.g. courses (such as \'Dinner\', \'Breakfast\', etc.), specific type of dishes (such as \'Meat\', \'Vegan\', \'Drinks\', etc.), or some other classification made by the menu provider.""",
    )

    MUSIC_RECORDING = Semantic(
        id="MusicRecording",
        ref="schema:MusicRecording",
        text="""A music recording (track), usually a single song.""",
    )

    WEARABLE_SIZE_GROUP_BOYS = Semantic(
        id="WearableSizeGroupBoys",
        ref="schema:WearableSizeGroupBoys",
        text="""Size group "Boys" for wearables.""",
    )

    DANCE_EVENT = Semantic(
        id="DanceEvent", ref="schema:DanceEvent", text="""Event type: A social dance."""
    )

    RESEARCH_PROJECT = Semantic(
        id="ResearchProject",
        ref="schema:ResearchProject",
        text="""A Research project.""",
    )

    RELATED_TO = Semantic(
        id="relatedTo",
        ref="schema:relatedTo",
        text="""The most generic familial relation.""",
    )

    COMIC_STORY = Semantic(
        id="ComicStory",
        ref="schema:ComicStory",
        text="""The term "story" is any indivisible, re-printable
    	unit of a comic, including the interior stories, covers, and backmatter. Most
    	comics have at least two stories: a cover (ComicCoverArt) and an interior story.""",
    )

    WEARABLE_SIZE_GROUP_INFANTS = Semantic(
        id="WearableSizeGroupInfants",
        ref="schema:WearableSizeGroupInfants",
        text="""Size group "Infants" for wearables.""",
    )

    COMMUNICATE_ACTION = Semantic(
        id="CommunicateAction",
        ref="schema:CommunicateAction",
        text="""The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.""",
    )

    SHIPPING_DESTINATION = Semantic(
        id="shippingDestination",
        ref="schema:shippingDestination",
        text="""indicates (possibly multiple) shipping destinations. These can be defined in several ways e.g. postalCode ranges.""",
    )

    SCREENING_EVENT = Semantic(
        id="ScreeningEvent",
        ref="schema:ScreeningEvent",
        text="""A screening of a movie or other video.""",
    )

    MAP_CATEGORY_TYPE = Semantic(
        id="MapCategoryType",
        ref="schema:MapCategoryType",
        text="""An enumeration of several kinds of Map.""",
    )

    RESULT_REVIEW = Semantic(
        id="resultReview",
        ref="schema:resultReview",
        text="""A sub property of result. The review that resulted in the performing of the action.""",
    )

    BLOG_POSTING = Semantic(
        id="BlogPosting", ref="schema:BlogPosting", text="""A blog post."""
    )

    COVERAGE_END_TIME = Semantic(
        id="coverageEndTime",
        ref="schema:coverageEndTime",
        text="""The time when the live blog will stop covering the Event. Note that coverage may continue after the Event concludes.""",
    )

    ANAEROBIC_ACTIVITY = Semantic(
        id="AnaerobicActivity",
        ref="schema:AnaerobicActivity",
        text="""Physical activity that is of high-intensity which utilizes the anaerobic metabolism of the body.""",
    )

    MEDICAL_SPECIALTY = Semantic(
        id="MedicalSpecialty",
        ref="schema:MedicalSpecialty",
        text="""Any specific branch of medical science or practice. Medical specialities include clinical specialties that pertain to particular organ systems and their respective disease states, as well as allied health specialties. Enumerated type.""",
    )

    HEALTH_PLAN_MARKETING_URL = Semantic(
        id="healthPlanMarketingUrl",
        ref="schema:healthPlanMarketingUrl",
        text="""The URL that goes directly to the plan brochure for the specific standard plan or plan variation.""",
    )

    MEDICAL_CAUSE = Semantic(
        id="MedicalCause",
        ref="schema:MedicalCause",
        text="""The causative agent(s) that are responsible for the pathophysiologic process that eventually results in a medical condition, symptom or sign. In this schema, unless otherwise specified this is meant to be the proximate cause of the medical condition, symptom or sign. The proximate cause is defined as the causative agent that most directly results in the medical condition, symptom or sign. For example, the HIV virus could be considered a cause of AIDS. Or in a diagnostic context, if a patient fell and sustained a hip fracture and two days later sustained a pulmonary embolism which eventuated in a cardiac arrest, the cause of the cardiac arrest (the proximate cause) would be the pulmonary embolism and not the fall. Medical causes can include cardiovascular, chemical, dermatologic, endocrine, environmental, gastroenterologic, genetic, hematologic, gynecologic, iatrogenic, infectious, musculoskeletal, neurologic, nutritional, obstetric, oncologic, otolaryngologic, pharmacologic, psychiatric, pulmonary, renal, rheumatologic, toxic, traumatic, or urologic causes; medical conditions can be causes as well.""",
    )

    BY_DAY = Semantic(
        id="byDay",
        ref="schema:byDay",
        text="""Defines the day(s) of the week on which a recurring [[Event]] takes place. May be specified using either [[DayOfWeek]], or alternatively [[Text]] conforming to iCal\'s syntax for byDay recurrence rules.""",
    )

    AUTO_REPAIR = Semantic(
        id="AutoRepair", ref="schema:AutoRepair", text="""Car repair business."""
    )

    MOBILE_APPLICATION = Semantic(
        id="MobileApplication",
        ref="schema:MobileApplication",
        text="""A software application designed specifically to work well on a mobile device such as a telephone.""",
    )

    HAS_PART = Semantic(
        id="hasPart",
        ref="schema:hasPart",
        text="""Indicates an item or CreativeWork that is part of this item, or CreativeWork (in some sense).""",
    )

    CAMPGROUND = Semantic(
        id="Campground",
        ref="schema:Campground",
        text="""A camping site, campsite, or [[Campground]] is a place used for overnight stay in the outdoors, typically containing individual [[CampingPitch]] locations. \\n\\n
In British English a campsite is an area, usually divided into a number of pitches, where people can camp overnight using tents or camper vans or caravans; this British English use of the word is synonymous with the American English expression campground. In American English the term campsite generally means an area where an individual, family, group, or military unit can pitch a tent or park a camper; a campground may contain many campsites (Source: Wikipedia see [https://en.wikipedia.org/wiki/Campsite](https://en.wikipedia.org/wiki/Campsite)).\\n\\n

See also the dedicated [document on the use of schema.org for marking up hotels and other forms of accommodations](/docs/hotels.html).
""",
    )

    FOUNDING_LOCATION = Semantic(
        id="foundingLocation",
        ref="schema:foundingLocation",
        text="""The place where the Organization was founded.""",
    )

    NONPROFIT501C4 = Semantic(
        id="Nonprofit501c4",
        ref="schema:Nonprofit501c4",
        text="""Nonprofit501c4: Non-profit type referring to Civic Leagues, Social Welfare Organizations, and Local Associations of Employees.""",
    )

    REQUIRED_QUANTITY = Semantic(
        id="requiredQuantity",
        ref="schema:requiredQuantity",
        text="""The required quantity of the item(s).""",
    )

    DIGITAL_DOCUMENT_PERMISSION_TYPE = Semantic(
        id="DigitalDocumentPermissionType",
        ref="schema:DigitalDocumentPermissionType",
        text="""A type of permission which can be granted for accessing a digital document.""",
    )

    AVAILABLE_STRENGTH = Semantic(
        id="availableStrength",
        ref="schema:availableStrength",
        text="""An available dosage strength for the drug.""",
    )

    TRACKING_URL = Semantic(
        id="trackingUrl",
        ref="schema:trackingUrl",
        text="""Tracking url for the parcel delivery.""",
    )

    ONLINE = Semantic(
        id="Online",
        ref="schema:Online",
        text="""Game server status: Online. Server is available.""",
    )

    POSITIVE_NOTES = Semantic(
        id="positiveNotes",
        ref="schema:positiveNotes",
        text="""Indicates, in the context of a [[Review]] (e.g. framed as \'pro\' vs \'con\' considerations), positive considerations - either as unstructured text, or a list.""",
    )

    SUGGESTED_AGE = Semantic(
        id="suggestedAge",
        ref="schema:suggestedAge",
        text="""The age or age range for the intended audience or person, for example 3-12 months for infants, 1-5 years for toddlers.""",
    )

    DRY_CLEANING_OR_LAUNDRY = Semantic(
        id="DryCleaningOrLaundry",
        ref="schema:DryCleaningOrLaundry",
        text="""A dry-cleaning business.""",
    )

    TRAILER = Semantic(
        id="trailer",
        ref="schema:trailer",
        text="""The trailer of a movie or tv/radio series, season, episode, etc.""",
    )

    LIQUOR_STORE = Semantic(
        id="LiquorStore",
        ref="schema:LiquorStore",
        text="""A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits.""",
    )

    SIZE_SYSTEM_IMPERIAL = Semantic(
        id="SizeSystemImperial",
        ref="schema:SizeSystemImperial",
        text="""Imperial size system.""",
    )

    BRANCH_OF = Semantic(
        id="branchOf",
        ref="schema:branchOf",
        text="""The larger organization that this local business is a branch of, if any. Not to be confused with (anatomical)[[branch]].""",
    )

    RANGE_INCLUDES = Semantic(
        id="rangeIncludes",
        ref="schema:rangeIncludes",
        text="""Relates a property to a class that constitutes (one of) the expected type(s) for values of the property.""",
    )

    NONPROFIT_TYPE = Semantic(
        id="NonprofitType",
        ref="schema:NonprofitType",
        text="""NonprofitType enumerates several kinds of official non-profit types of which a non-profit organization can be.""",
    )

    INTERACTION_TYPE = Semantic(
        id="interactionType",
        ref="schema:interactionType",
        text="""The Action representing the type of interaction. For up votes, +1s, etc. use [[LikeAction]]. For down votes use [[DislikeAction]]. Otherwise, use the most specific Action.""",
    )

    ACTIVE_INGREDIENT = Semantic(
        id="activeIngredient",
        ref="schema:activeIngredient",
        text="""An active ingredient, typically chemical compounds and/or biologic substances.""",
    )

    SERVICE_LOCATION = Semantic(
        id="serviceLocation",
        ref="schema:serviceLocation",
        text="""The location (e.g. civic structure, local business, etc.) where a person can go to access the service.""",
    )

    HEALTH_PLAN_NETWORK = Semantic(
        id="HealthPlanNetwork",
        ref="schema:HealthPlanNetwork",
        text="""A US-style health insurance plan network. """,
    )

    MEDICAL_SCHOLARLY_ARTICLE = Semantic(
        id="MedicalScholarlyArticle",
        ref="schema:MedicalScholarlyArticle",
        text="""A scholarly article in the medical domain.""",
    )

    SELF_STORAGE = Semantic(
        id="SelfStorage", ref="schema:SelfStorage", text="""A self-storage facility."""
    )

    STAGE_AS_NUMBER = Semantic(
        id="stageAsNumber",
        ref="schema:stageAsNumber",
        text="""The stage represented as a number, e.g. 3.""",
    )

    SOFTWARE_SOURCE_CODE = Semantic(
        id="SoftwareSourceCode",
        ref="schema:SoftwareSourceCode",
        text="""Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates.""",
    )

    EPISODES = Semantic(
        id="episodes",
        ref="schema:episodes",
        text="""An episode of a TV/radio series or season.""",
    )

    ACCESSIBILITY_SUMMARY = Semantic(
        id="accessibilitySummary",
        ref="schema:accessibilitySummary",
        text='''A human-readable summary of specific accessibility features or deficiencies, consistent with the other accessibility metadata but expressing subtleties such as "short descriptions are present but long descriptions will be needed for non-visual users" or "short descriptions are present and no long descriptions are needed."''',
    )

    RESEARCHER = Semantic(
        id="Researcher", ref="schema:Researcher", text="""Researchers."""
    )

    NONPROFIT501C8 = Semantic(
        id="Nonprofit501c8",
        ref="schema:Nonprofit501c8",
        text="""Nonprofit501c8: Non-profit type referring to Fraternal Beneficiary Societies and Associations.""",
    )

    NUMBER_OF_AXLES = Semantic(
        id="numberOfAxles",
        ref="schema:numberOfAxles",
        text="""The number of axles.\\n\\nTypical unit code(s): C62""",
    )

    WEARABLE_SIZE_SYSTEM_B_R = Semantic(
        id="WearableSizeSystemBR",
        ref="schema:WearableSizeSystemBR",
        text="""Brazilian size system for wearables.""",
    )

    PRICE_TYPE_ENUMERATION = Semantic(
        id="PriceTypeEnumeration",
        ref="schema:PriceTypeEnumeration",
        text="""Enumerates different price types, for example list price, invoice price, and sale price.""",
    )

    CC_RECIPIENT = Semantic(
        id="ccRecipient",
        ref="schema:ccRecipient",
        text="""A sub property of recipient. The recipient copied on a message.""",
    )

    DEFENCE_ESTABLISHMENT = Semantic(
        id="DefenceEstablishment",
        ref="schema:DefenceEstablishment",
        text="""A defence establishment, such as an army or navy base.""",
    )

    NONPROFIT501Q = Semantic(
        id="Nonprofit501q",
        ref="schema:Nonprofit501q",
        text="""Nonprofit501q: Non-profit type referring to Credit Counseling Organizations.""",
    )

    ORIGINAL_MEDIA_LINK = Semantic(
        id="originalMediaLink",
        ref="schema:originalMediaLink",
        text="""Link to the page containing an original version of the content, or directly to an online copy of the original [[MediaObject]] content, e.g. video file.""",
    )

    BODY_MEASUREMENT_HIPS = Semantic(
        id="BodyMeasurementHips",
        ref="schema:BodyMeasurementHips",
        text="""Girth of hips (measured around the buttocks). Used, for example, to fit skirts.""",
    )

    LOCAL_BUSINESS = Semantic(
        id="LocalBusiness",
        ref="schema:LocalBusiness",
        text="""A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.""",
    )

    AVAILABILITY = Semantic(
        id="availability",
        ref="schema:availability",
        text="""The availability of this item&#x2014;for example In stock, Out of stock, Pre-order, etc.""",
    )

    CVD_NUM_C19_OVERFLOW_PATS = Semantic(
        id="cvdNumC19OverflowPats",
        ref="schema:cvdNumC19OverflowPats",
        text="""numc19overflowpats - ED/OVERFLOW: Patients with suspected or confirmed COVID-19 who are in the ED or any overflow location awaiting an inpatient bed.""",
    )

    BLOG_POSTS = Semantic(
        id="blogPosts",
        ref="schema:blogPosts",
        text="""Indicates a post that is part of a [[Blog]]. Note that historically, what we term a "Blog" was once known as a "weblog", and that what we term a "BlogPosting" is now often colloquially referred to as a "blog".""",
    )

    BIO_CHEM_ENTITY = Semantic(
        id="BioChemEntity",
        ref="schema:BioChemEntity",
        text="""Any biological, chemical, or biochemical thing. For example: a protein; a gene; a chemical; a synthetic chemical.""",
    )

    TIRE_SHOP = Semantic(id="TireShop", ref="schema:TireShop", text="""A tire shop.""")

    HOSTEL = Semantic(
        id="Hostel",
        ref="schema:Hostel",
        text="""A hostel - cheap accommodation, often in shared dormitories.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
""",
    )

    SENSORY_REQUIREMENT = Semantic(
        id="sensoryRequirement",
        ref="schema:sensoryRequirement",
        text="""A description of any sensory requirements and levels necessary to function on the job, including hearing and vision. Defined terms such as those in O*net may be used, but note that there is no way to specify the level of ability as well as its nature when using a defined term.""",
    )

    NUTRITION_INFORMATION = Semantic(
        id="NutritionInformation",
        ref="schema:NutritionInformation",
        text="""Nutritional information about the recipe.""",
    )

    EDUCATIONAL_OCCUPATIONAL_PROGRAM = Semantic(
        id="EducationalOccupationalProgram",
        ref="schema:EducationalOccupationalProgram",
        text="""A program offered by an institution which determines the learning progress to achieve an outcome, usually a credential like a degree or certificate. This would define a discrete set of opportunities (e.g., job, courses) that together constitute a program with a clear start, end, set of requirements, and transition to a new occupational opportunity (e.g., a job), or sometimes a higher educational opportunity (e.g., an advanced degree).""",
    )

    RELEASE_OF = Semantic(
        id="releaseOf",
        ref="schema:releaseOf",
        text="""The album this is a release of.""",
    )

    RADIO_CLIP = Semantic(
        id="RadioClip",
        ref="schema:RadioClip",
        text="""A short radio program or a segment/part of a radio program.""",
    )

    NONPROFIT501C25 = Semantic(
        id="Nonprofit501c25",
        ref="schema:Nonprofit501c25",
        text="""Nonprofit501c25: Non-profit type referring to Real Property Title-Holding Corporations or Trusts with Multiple Parents.""",
    )

    REVIEW_ASPECT = Semantic(
        id="reviewAspect",
        ref="schema:reviewAspect",
        text="""This Review or Rating is relevant to this part or facet of the itemReviewed.""",
    )

    TEXT_VALUE = Semantic(
        id="textValue", ref="schema:textValue", text="""Text value being annotated."""
    )

    NONPROFIT501C1 = Semantic(
        id="Nonprofit501c1",
        ref="schema:Nonprofit501c1",
        text="""Nonprofit501c1: Non-profit type referring to Corporations Organized Under Act of Congress, including Federal Credit Unions and National Farm Loan Associations.""",
    )

    RENEGOTIABLE_LOAN = Semantic(
        id="renegotiableLoan",
        ref="schema:renegotiableLoan",
        text="""Whether the terms for payment of interest can be renegotiated during the life of the loan.""",
    )

    TRANSFER_ACTION = Semantic(
        id="TransferAction",
        ref="schema:TransferAction",
        text="""The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.""",
    )

    DATA_FEED_ITEM = Semantic(
        id="DataFeedItem",
        ref="schema:DataFeedItem",
        text="""A single item within a larger data feed.""",
    )

    ALBUM_RELEASE_TYPE = Semantic(
        id="albumReleaseType",
        ref="schema:albumReleaseType",
        text="""The kind of release which this album is: single, EP or album.""",
    )

    FAST_FOOD_RESTAURANT = Semantic(
        id="FastFoodRestaurant",
        ref="schema:FastFoodRestaurant",
        text="""A fast-food restaurant.""",
    )

    TICKET_NUMBER = Semantic(
        id="ticketNumber",
        ref="schema:ticketNumber",
        text="""The unique identifier for the ticket.""",
    )

    APPROVED_INDICATION = Semantic(
        id="ApprovedIndication",
        ref="schema:ApprovedIndication",
        text="""An indication for a medical therapy that has been formally specified or approved by a regulatory body that regulates use of the therapy; for example, the US FDA approves indications for most drugs in the US.""",
    )

    ACCESS_MODE_SUFFICIENT = Semantic(
        id="accessModeSufficient",
        ref="schema:accessModeSufficient",
        text="""A list of single or combined accessModes that are sufficient to understand all the intellectual content of a resource. Expected values include:  auditory, tactile, textual, visual.
      """,
    )

    EXHIBITION_EVENT = Semantic(
        id="ExhibitionEvent",
        ref="schema:ExhibitionEvent",
        text="""Event type: Exhibition event, e.g. at a museum, library, archive, tradeshow, ...""",
    )

    E_U_ENERGY_EFFICIENCY_CATEGORY_E = Semantic(
        id="EUEnergyEfficiencyCategoryE",
        ref="schema:EUEnergyEfficiencyCategoryE",
        text="""Represents EU Energy Efficiency Class E as defined in EU energy labeling regulations.""",
    )

    D_V_D_FORMAT = Semantic(
        id="DVDFormat", ref="schema:DVDFormat", text="""DVDFormat."""
    )

    READ_PERMISSION = Semantic(
        id="ReadPermission",
        ref="schema:ReadPermission",
        text="""Permission to read or view the document.""",
    )

    WEARABLE_SIZE_SYSTEM_E_N13402 = Semantic(
        id="WearableSizeSystemEN13402",
        ref="schema:WearableSizeSystemEN13402",
        text="""EN 13402 (joint European standard for size labelling of clothes).""",
    )

    GTIN8 = Semantic(
        id="gtin8",
        ref="schema:gtin8",
        text="""The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.""",
    )

    VALUE_ADDED_TAX_INCLUDED = Semantic(
        id="valueAddedTaxIncluded",
        ref="schema:valueAddedTaxIncluded",
        text="""Specifies whether the applicable value-added tax (VAT) is included in the price specification or not.""",
    )

    PAYMENT_DECLINED = Semantic(
        id="PaymentDeclined",
        ref="schema:PaymentDeclined",
        text="""The payee received the payment, but it was declined for some reason.""",
    )

    ARRIVAL_BUS_STOP = Semantic(
        id="arrivalBusStop",
        ref="schema:arrivalBusStop",
        text="""The stop or station from which the bus arrives.""",
    )

    NECK = Semantic(
        id="Neck",
        ref="schema:Neck",
        text="""Neck assessment with clinical examination.""",
    )

    NONPROFIT501C28 = Semantic(
        id="Nonprofit501c28",
        ref="schema:Nonprofit501c28",
        text="""Nonprofit501c28: Non-profit type referring to National Railroad Retirement Investment Trusts.""",
    )

    DERMATOLOGIC = Semantic(
        id="Dermatologic",
        ref="schema:Dermatologic",
        text="""Something relating to or practicing dermatology.""",
    )

    WEARABLE_SIZE_GROUP_JUNIORS = Semantic(
        id="WearableSizeGroupJuniors",
        ref="schema:WearableSizeGroupJuniors",
        text="""Size group "Juniors" for wearables.""",
    )

    ULTRASOUND = Semantic(
        id="Ultrasound", ref="schema:Ultrasound", text="""Ultrasound imaging."""
    )

    VALID_FOR = Semantic(
        id="validFor",
        ref="schema:validFor",
        text="""The duration of validity of a permit or similar thing.""",
    )

    BY_MONTH_DAY = Semantic(
        id="byMonthDay",
        ref="schema:byMonthDay",
        text="""Defines the day(s) of the month on which a recurring [[Event]] takes place. Specified as an [[Integer]] between 1-31.""",
    )

    PREGNANCY_WARNING = Semantic(
        id="pregnancyWarning",
        ref="schema:pregnancyWarning",
        text="""Any precaution, guidance, contraindication, etc. related to this drug\'s use during pregnancy.""",
    )

    NSN = Semantic(
        id="nsn",
        ref="schema:nsn",
        text="""Indicates the [NATO stock number](https://en.wikipedia.org/wiki/NATO_Stock_Number) (nsn) of a [[Product]]. """,
    )

    SUSPEND_ACTION = Semantic(
        id="SuspendAction",
        ref="schema:SuspendAction",
        text="""The act of momentarily pausing a device or application (e.g. pause music playback or pause a timer).""",
    )

    DENTISTRY = Semantic(
        id="Dentistry",
        ref="schema:Dentistry",
        text="""A branch of medicine that is involved in the dental care.""",
    )

    HEADLINE = Semantic(
        id="headline", ref="schema:headline", text="""Headline of the article."""
    )

    CONTENT_URL = Semantic(
        id="contentUrl",
        ref="schema:contentUrl",
        text="""Actual bytes of the media object, for example the image file or video file.""",
    )

    PROCEDURE = Semantic(
        id="procedure",
        ref="schema:procedure",
        text="""A description of the procedure involved in setting up, using, and/or installing the device.""",
    )

    EDUCATIONAL_ALIGNMENT = Semantic(
        id="educationalAlignment",
        ref="schema:educationalAlignment",
        text="""An alignment to an established educational framework.

This property should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [[teaches]] or [[assesses]] a competency.""",
    )

    ITEM_DEFECT_RETURN_SHIPPING_FEES_AMOUNT = Semantic(
        id="itemDefectReturnShippingFeesAmount",
        ref="schema:itemDefectReturnShippingFeesAmount",
        text="""Amount of shipping costs for defect product returns. Applicable when property [[itemDefectReturnFees]] equals [[ReturnShippingFees]].""",
    )

    BLOG_POST = Semantic(
        id="blogPost",
        ref="schema:blogPost",
        text="""A posting that is part of this blog.""",
    )

    TAKE_ACTION = Semantic(
        id="TakeAction",
        ref="schema:TakeAction",
        text="""The act of gaining ownership of an object from an origin. Reciprocal of GiveAction.\\n\\nRelated actions:\\n\\n* [[GiveAction]]: The reciprocal of TakeAction.\\n* [[ReceiveAction]]: Unlike ReceiveAction, TakeAction implies that ownership has been transfered.""",
    )

    DEPARTURE_TIME = Semantic(
        id="departureTime",
        ref="schema:departureTime",
        text="""The expected departure time.""",
    )

    BREADCRUMB_LIST = Semantic(
        id="BreadcrumbList",
        ref="schema:BreadcrumbList",
        text="""A BreadcrumbList is an ItemList consisting of a chain of linked Web pages, typically described using at least their URL and their name, and typically ending with the current page.\\n\\nThe [[position]] property is used to reconstruct the order of the items in a BreadcrumbList The convention is that a breadcrumb list has an [[itemListOrder]] of [[ItemListOrderAscending]] (lower values listed first), and that the first items in this list correspond to the "top" or beginning of the breadcrumb trail, e.g. with a site or section homepage. The specific values of \'position\' are not assigned meaning for a BreadcrumbList, but they should be integers, e.g. beginning with \'1\' for the first item in the list.
      """,
    )

    TRACKS = Semantic(
        id="tracks",
        ref="schema:tracks",
        text="""A music recording (track)&#x2014;usually a single song.""",
    )

    WEARABLE_MEASUREMENT_TYPE_ENUMERATION = Semantic(
        id="WearableMeasurementTypeEnumeration",
        ref="schema:WearableMeasurementTypeEnumeration",
        text="""Enumerates common types of measurement for wearables products.""",
    )

    ACCESS_CODE = Semantic(
        id="accessCode",
        ref="schema:accessCode",
        text="""Password, PIN, or access code needed for delivery (e.g. from a locker).""",
    )

    TERMS_OF_SERVICE = Semantic(
        id="termsOfService",
        ref="schema:termsOfService",
        text="""Human-readable terms of service documentation.""",
    )

    TRIPLE_BLINDED_TRIAL = Semantic(
        id="TripleBlindedTrial",
        ref="schema:TripleBlindedTrial",
        text="""A trial design in which neither the researcher, the person administering the therapy nor the patient knows the details of the treatment the patient was randomly assigned to.""",
    )

    ASK_PUBLIC_NEWS_ARTICLE = Semantic(
        id="AskPublicNewsArticle",
        ref="schema:AskPublicNewsArticle",
        text="""A [[NewsArticle]] expressing an open call by a [[NewsMediaOrganization]] asking the public for input, insights, clarifications, anecdotes, documentation, etc., on an issue, for reporting purposes.""",
    )

    PROCEDURE_TYPE = Semantic(
        id="procedureType",
        ref="schema:procedureType",
        text="""The type of procedure, for example Surgical, Noninvasive, or Percutaneous.""",
    )

    ORDER_DELIVERY = Semantic(
        id="orderDelivery",
        ref="schema:orderDelivery",
        text="""The delivery of the parcel related to this order or order item.""",
    )

    LEASE_LENGTH = Semantic(
        id="leaseLength",
        ref="schema:leaseLength",
        text="""Length of the lease for some [[Accommodation]], either particular to some [[Offer]] or in some cases intrinsic to the property.""",
    )

    PARTICIPANT = Semantic(
        id="participant",
        ref="schema:participant",
        text="""Other co-agents that participated in the action indirectly. e.g. John wrote a book with *Steve*.""",
    )

    USE_ACTION = Semantic(
        id="UseAction",
        ref="schema:UseAction",
        text="""The act of applying an object to its intended purpose.""",
    )

    GUIDELINE = Semantic(
        id="guideline",
        ref="schema:guideline",
        text="""A medical guideline related to this entity.""",
    )

    PRINT_SECTION = Semantic(
        id="printSection",
        ref="schema:printSection",
        text="""If this NewsArticle appears in print, this field indicates the print section in which the article appeared.""",
    )

    SCHOOL_DISTRICT = Semantic(
        id="SchoolDistrict",
        ref="schema:SchoolDistrict",
        text="""A School District is an administrative area for the administration of schools.""",
    )

    WEARABLE_SIZE_GROUP_MATERNITY = Semantic(
        id="WearableSizeGroupMaternity",
        ref="schema:WearableSizeGroupMaternity",
        text="""Size group "Maternity" for wearables.""",
    )

    LOAN_TYPE = Semantic(
        id="loanType", ref="schema:loanType", text="""The type of a loan or credit."""
    )

    COMIC_ISSUE = Semantic(
        id="ComicIssue",
        ref="schema:ComicIssue",
        text="""Individual comic issues are serially published as
    	part of a larger series. For the sake of consistency, even one-shot issues
    	belong to a series comprised of a single issue. All comic issues can be
    	uniquely identified by: the combination of the name and volume number of the
    	series to which the issue belongs; the issue number; and the variant
    	description of the issue (if any).""",
    )

    BEFORE_MEDIA = Semantic(
        id="beforeMedia",
        ref="schema:beforeMedia",
        text="""A media object representing the circumstances before performing this direction.""",
    )

    FLIGHT_DISTANCE = Semantic(
        id="flightDistance",
        ref="schema:flightDistance",
        text="""The distance of the flight.""",
    )

    JOB_IMMEDIATE_START = Semantic(
        id="jobImmediateStart",
        ref="schema:jobImmediateStart",
        text="""An indicator as to whether a position is available for an immediate start.""",
    )

    WITHDRAWN = Semantic(id="Withdrawn", ref="schema:Withdrawn", text="""Withdrawn.""")

    MEDICAL_ENUMERATION = Semantic(
        id="MedicalEnumeration",
        ref="schema:MedicalEnumeration",
        text="""Enumerations related to health and the practice of medicine: A concept that is used to attribute a quality to another concept, as a qualifier, a collection of items or a listing of all of the elements of a set in medicine practice.""",
    )

    HEALTH_PLAN_PHARMACY_CATEGORY = Semantic(
        id="healthPlanPharmacyCategory",
        ref="schema:healthPlanPharmacyCategory",
        text="""The category or type of pharmacy associated with this cost sharing.""",
    )

    ACTION_ACCESS_SPECIFICATION = Semantic(
        id="ActionAccessSpecification",
        ref="schema:ActionAccessSpecification",
        text="""A set of requirements that a must be fulfilled in order to perform an Action.""",
    )

    ACCOUNT_ID = Semantic(
        id="accountId",
        ref="schema:accountId",
        text="""The identifier for the account the payment will be applied to.""",
    )

    WEB_PAGE_ELEMENT = Semantic(
        id="WebPageElement",
        ref="schema:WebPageElement",
        text="""A web page element, like a table or an image.""",
    )

    HEALTH_PLAN_NETWORK_TIER = Semantic(
        id="healthPlanNetworkTier",
        ref="schema:healthPlanNetworkTier",
        text="""The tier(s) for this network.""",
    )

    NONPROFIT501C16 = Semantic(
        id="Nonprofit501c16",
        ref="schema:Nonprofit501c16",
        text="""Nonprofit501c16: Non-profit type referring to Cooperative Organizations to Finance Crop Operations.""",
    )

    QUANTITATIVE_VALUE_DISTRIBUTION = Semantic(
        id="QuantitativeValueDistribution",
        ref="schema:QuantitativeValueDistribution",
        text="""A statistical distribution of values.""",
    )

    BREASTFEEDING_WARNING = Semantic(
        id="breastfeedingWarning",
        ref="schema:breastfeedingWarning",
        text="""Any precaution, guidance, contraindication, etc. related to this drug\'s use by breastfeeding mothers.""",
    )

    NONPROFIT501C11 = Semantic(
        id="Nonprofit501c11",
        ref="schema:Nonprofit501c11",
        text="""Nonprofit501c11: Non-profit type referring to Teachers\' Retirement Fund Associations.""",
    )

    PHYSICAL_REQUIREMENT = Semantic(
        id="physicalRequirement",
        ref="schema:physicalRequirement",
        text="""A description of the types of physical activity associated with the job. Defined terms such as those in O*net may be used, but note that there is no way to specify the level of ability as well as its nature when using a defined term.""",
    )

    USES_HEALTH_PLAN_ID_STANDARD = Semantic(
        id="usesHealthPlanIdStandard",
        ref="schema:usesHealthPlanIdStandard",
        text="""The standard for interpreting thePlan ID. The preferred is "HIOS". See the Centers for Medicare & Medicaid Services for more details.""",
    )

    COMPUTER_STORE = Semantic(
        id="ComputerStore", ref="schema:ComputerStore", text="""A computer store."""
    )

    HOSPITAL_AFFILIATION = Semantic(
        id="hospitalAffiliation",
        ref="schema:hospitalAffiliation",
        text="""A hospital with which the physician or office is affiliated.""",
    )

    AMOUNT = Semantic(id="amount", ref="schema:amount", text="""The amount of money.""")

    ACQUIRED_FROM = Semantic(
        id="acquiredFrom",
        ref="schema:acquiredFrom",
        text="""The organization or person from which the product was acquired.""",
    )

    BROADCAST_SIGNAL_MODULATION = Semantic(
        id="broadcastSignalModulation",
        ref="schema:broadcastSignalModulation",
        text="""The modulation (e.g. FM, AM, etc) used by a particular broadcast service.""",
    )

    FUEL_CONSUMPTION = Semantic(
        id="fuelConsumption",
        ref="schema:fuelConsumption",
        text="""The amount of fuel consumed for traveling a particular distance or temporal duration with the given vehicle (e.g. liters per 100 km).\\n\\n* Note 1: There are unfortunately no standard unit codes for liters per 100 km.  Use [[unitText]] to indicate the unit of measurement, e.g. L/100 km.\\n* Note 2: There are two ways of indicating the fuel consumption, [[fuelConsumption]] (e.g. 8 liters per 100 km) and [[fuelEfficiency]] (e.g. 30 miles per gallon). They are reciprocal.\\n* Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use [[valueReference]] to link the value for the fuel consumption to another value.""",
    )

    COMPOSER = Semantic(
        id="composer",
        ref="schema:composer",
        text="""The person or organization who wrote a composition, or who is the composer of a work performed at some event.""",
    )

    MEDICAL_WEB_PAGE = Semantic(
        id="MedicalWebPage",
        ref="schema:MedicalWebPage",
        text="""A web page that provides medical information.""",
    )

    DISEASE_SPREAD_STATISTICS = Semantic(
        id="diseaseSpreadStatistics",
        ref="schema:diseaseSpreadStatistics",
        text="""Statistical information about the spread of a disease, either as [[WebContent]], or
  described directly as a [[Dataset]], or the specific [[Observation]]s in the dataset. When a [[WebContent]] URL is
  provided, the page indicated might also contain more such markup.""",
    )

    OPERATING_SYSTEM = Semantic(
        id="operatingSystem",
        ref="schema:operatingSystem",
        text="""Operating systems supported (Windows 7, OSX 10.6, Android 1.6).""",
    )

    JOB_LOCATION = Semantic(
        id="jobLocation",
        ref="schema:jobLocation",
        text="""A (typically single) geographic location associated with the job position.""",
    )

    HAS_DEFINED_TERM = Semantic(
        id="hasDefinedTerm",
        ref="schema:hasDefinedTerm",
        text="""A Defined Term contained in this term set.""",
    )

    GAME_SERVER_STATUS = Semantic(
        id="GameServerStatus",
        ref="schema:GameServerStatus",
        text="""Status of a game server.""",
    )

    NUMBER_OF_EPISODES = Semantic(
        id="numberOfEpisodes",
        ref="schema:numberOfEpisodes",
        text="""The number of episodes in this season or series.""",
    )

    HEALTH_CLUB = Semantic(
        id="HealthClub", ref="schema:HealthClub", text="""A health club."""
    )

    OPEN_TRIAL = Semantic(
        id="OpenTrial",
        ref="schema:OpenTrial",
        text="""A trial design in which the researcher knows the full details of the treatment, and so does the patient.""",
    )

    RESERVATION_CANCELLED = Semantic(
        id="ReservationCancelled",
        ref="schema:ReservationCancelled",
        text="""The status for a previously confirmed reservation that is now cancelled.""",
    )

    PHYSIOTHERAPY = Semantic(
        id="Physiotherapy",
        ref="schema:Physiotherapy",
        text="""The practice of treatment of disease, injury, or deformity by physical methods such as massage, heat treatment, and exercise rather than by drugs or surgery..""",
    )

    HONORIFIC_SUFFIX = Semantic(
        id="honorificSuffix",
        ref="schema:honorificSuffix",
        text="""An honorific suffix following a Person\'s name such as M.D. /PhD/MSCSW.""",
    )

    TRANS_FAT_CONTENT = Semantic(
        id="transFatContent",
        ref="schema:transFatContent",
        text="""The number of grams of trans fat.""",
    )

    REJECT_ACTION = Semantic(
        id="RejectAction",
        ref="schema:RejectAction",
        text="""The act of rejecting to/adopting an object.\\n\\nRelated actions:\\n\\n* [[AcceptAction]]: The antonym of RejectAction.""",
    )

    PUBLISHING_PRINCIPLES = Semantic(
        id="publishingPrinciples",
        ref="schema:publishingPrinciples",
        text="""The publishingPrinciples property indicates (typically via [[URL]]) a document describing the editorial principles of an [[Organization]] (or individual e.g. a [[Person]] writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity policies. When applied to a [[CreativeWork]] (e.g. [[NewsArticle]]) the principles are those of the party primarily responsible for the creation of the [[CreativeWork]].

While such policies are most typically expressed in natural language, sometimes related information (e.g. indicating a [[funder]]) can be expressed using schema.org terminology.
""",
    )

    VIDEO_QUALITY = Semantic(
        id="videoQuality",
        ref="schema:videoQuality",
        text="""The quality of the video.""",
    )

    HAS_MENU_ITEM = Semantic(
        id="hasMenuItem",
        ref="schema:hasMenuItem",
        text="""A food or drink item contained in a menu or menu section.""",
    )

    BUS_NUMBER = Semantic(
        id="busNumber",
        ref="schema:busNumber",
        text="""The unique identifier for the bus.""",
    )

    TRAIN_RESERVATION = Semantic(
        id="TrainReservation",
        ref="schema:TrainReservation",
        text="""A reservation for train travel.\\n\\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].""",
    )

    GOVERNMENT_BUILDING = Semantic(
        id="GovernmentBuilding",
        ref="schema:GovernmentBuilding",
        text="""A government building.""",
    )

    X_PATH_TYPE = Semantic(
        id="XPathType",
        ref="schema:XPathType",
        text="""Text representing an XPath (typically but not necessarily version 1.0).""",
    )

    DISCOUNT_CURRENCY = Semantic(
        id="discountCurrency",
        ref="schema:discountCurrency",
        text="""The currency of the discount.\\n\\nUse standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217) e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies e.g. "BTC"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types e.g. "Ithaca HOUR".""",
    )

    IS_LIVE_BROADCAST = Semantic(
        id="isLiveBroadcast",
        ref="schema:isLiveBroadcast",
        text="""True if the broadcast is of a live event.""",
    )

    MODIFIED_TIME = Semantic(
        id="modifiedTime",
        ref="schema:modifiedTime",
        text="""The date and time the reservation was modified.""",
    )

    MEDICAL_RISK_ESTIMATOR = Semantic(
        id="MedicalRiskEstimator",
        ref="schema:MedicalRiskEstimator",
        text="""Any rule set or interactive tool for estimating the risk of developing a complication or condition.""",
    )

    LAYOUT_IMAGE = Semantic(
        id="layoutImage",
        ref="schema:layoutImage",
        text="""A schematic image showing the floorplan layout.""",
    )

    EVENT_ATTENDANCE_MODE_ENUMERATION = Semantic(
        id="EventAttendanceModeEnumeration",
        ref="schema:EventAttendanceModeEnumeration",
        text="""An EventAttendanceModeEnumeration value is one of potentially several modes of organising an event, relating to whether it is online or offline.""",
    )

    SMILES = Semantic(
        id="smiles",
        ref="schema:smiles",
        text="""A specification in form of a line notation for describing the structure of chemical species using short ASCII strings.  Double bond stereochemistry \\ indicators may need to be escaped in the string in formats where the backslash is an escape character.""",
    )

    CVD_NUM_BEDS = Semantic(
        id="cvdNumBeds",
        ref="schema:cvdNumBeds",
        text="""numbeds - HOSPITAL INPATIENT BEDS: Inpatient beds, including all staffed, licensed, and overflow (surge) beds used for inpatients.""",
    )

    ACTION = Semantic(
        id="Action",
        ref="schema:Action",
        text="""An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.\\n\\nSee also [blog post](http://blog.schema.org/2014/04/announcing-schemaorg-actions.html) and [Actions overview document](https://schema.org/docs/actions.html).""",
    )

    A_M_RADIO_CHANNEL = Semantic(
        id="AMRadioChannel",
        ref="schema:AMRadioChannel",
        text="""A radio channel that uses AM.""",
    )

    ISIC_V4 = Semantic(
        id="isicV4",
        ref="schema:isicV4",
        text="""The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.""",
    )

    NONPROFIT501C12 = Semantic(
        id="Nonprofit501c12",
        ref="schema:Nonprofit501c12",
        text="""Nonprofit501c12: Non-profit type referring to Benevolent Life Insurance Associations, Mutual Ditch or Irrigation Companies, Mutual or Cooperative Telephone Companies.""",
    )

    VEIN = Semantic(
        id="Vein",
        ref="schema:Vein",
        text="""A type of blood vessel that specifically carries blood to the heart.""",
    )

    TICKET_TOKEN = Semantic(
        id="ticketToken",
        ref="schema:ticketToken",
        text="""Reference to an asset (e.g., Barcode, QR code image or PDF) usable for entrance.""",
    )

    PAID_LEAVE = Semantic(
        id="PaidLeave",
        ref="schema:PaidLeave",
        text="""PaidLeave: this is a benefit for paid leave.""",
    )

    LIVE_BLOG_POSTING = Semantic(
        id="LiveBlogPosting",
        ref="schema:LiveBlogPosting",
        text="""A [[LiveBlogPosting]] is a [[BlogPosting]] intended to provide a rolling textual coverage of an ongoing event through continuous updates.""",
    )

    SALE_PRICE = Semantic(
        id="SalePrice",
        ref="schema:SalePrice",
        text="""Represents a sale price (usually active for a limited period) of an offered product.""",
    )

    ENGINE_TYPE = Semantic(
        id="engineType",
        ref="schema:engineType",
        text="""The type of engine or engines powering the vehicle.""",
    )

    LIKE_ACTION = Semantic(
        id="LikeAction",
        ref="schema:LikeAction",
        text="""The act of expressing a positive sentiment about the object. An agent likes an object (a proposition, topic or theme) with participants.""",
    )

    LEGAL_SERVICE = Semantic(
        id="LegalService",
        ref="schema:LegalService",
        text="""A LegalService is a business that provides legally-oriented services, advice and representation, e.g. law firms.\\n\\nAs a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]\\(s).""",
    )

    BRANCH = Semantic(
        id="branch",
        ref="schema:branch",
        text="""The branches that delineate from the nerve bundle. Not to be confused with [[branchOf]].""",
    )

    LONGITUDE = Semantic(
        id="longitude",
        ref="schema:longitude",
        text="""The longitude of a location. For example ```-122.08585``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).""",
    )

    COMMENT = Semantic(
        id="comment", ref="schema:comment", text="""Comments, typically from users."""
    )

    MUSIC_EVENT = Semantic(
        id="MusicEvent", ref="schema:MusicEvent", text="""Event type: Music event."""
    )

    SMOKING_ALLOWED = Semantic(
        id="smokingAllowed",
        ref="schema:smokingAllowed",
        text="""Indicates whether it is allowed to smoke in the place, e.g. in the restaurant, hotel or hotel room.""",
    )

    URL = Semantic(id="url", ref="schema:url", text="""URL of the item.""")

    ELIGIBLE_TRANSACTION_VOLUME = Semantic(
        id="eligibleTransactionVolume",
        ref="schema:eligibleTransactionVolume",
        text="""The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.""",
    )

    STUDY = Semantic(
        id="study",
        ref="schema:study",
        text="""A medical study or trial related to this entity.""",
    )

    ISBN = Semantic(id="isbn", ref="schema:isbn", text="""The ISBN of the book.""")

    BIRTH_PLACE = Semantic(
        id="birthPlace",
        ref="schema:birthPlace",
        text="""The place where the person was born.""",
    )

    SOFTWARE_ADD_ON = Semantic(
        id="softwareAddOn",
        ref="schema:softwareAddOn",
        text="""Additional content for a software application.""",
    )

    ART_EDITION = Semantic(
        id="artEdition",
        ref="schema:artEdition",
        text="""The number of copies when multiple copies of a piece of artwork are produced - e.g. for a limited edition of 20 prints, \'artEdition\' refers to the total number of copies (in this example "20").""",
    )

    CODE_VALUE = Semantic(
        id="codeValue",
        ref="schema:codeValue",
        text="""A short textual code that uniquely identifies the value.""",
    )

    PARENT = Semantic(
        id="parent", ref="schema:parent", text="""A parent of this person."""
    )

    RETURN_LABEL_SOURCE_ENUMERATION = Semantic(
        id="ReturnLabelSourceEnumeration",
        ref="schema:ReturnLabelSourceEnumeration",
        text="""Enumerates several types of return labels for product returns.""",
    )

    SKI_RESORT = Semantic(
        id="SkiResort", ref="schema:SkiResort", text="""A ski resort."""
    )

    EXPECTED_PROGNOSIS = Semantic(
        id="expectedPrognosis",
        ref="schema:expectedPrognosis",
        text="""The likely outcome in either the short term or long term of the medical condition.""",
    )

    ITINERARY = Semantic(
        id="itinerary",
        ref="schema:itinerary",
        text="""Destination(s) ( [[Place]] ) that make up a trip. For a trip where destination order is important use [[ItemList]] to specify that order (see examples).""",
    )

    AUDIO = Semantic(
        id="audio", ref="schema:audio", text="""An embedded audio object."""
    )

    DRINK_ACTION = Semantic(
        id="DrinkAction",
        ref="schema:DrinkAction",
        text="""The act of swallowing liquids.""",
    )

    LOAN_PAYMENT_AMOUNT = Semantic(
        id="loanPaymentAmount",
        ref="schema:loanPaymentAmount",
        text="""The amount of money to pay in a single payment.""",
    )

    MEDICAL_INTANGIBLE = Semantic(
        id="MedicalIntangible",
        ref="schema:MedicalIntangible",
        text="""A utility class that serves as the umbrella for a number of \'intangible\' things in the medical space.""",
    )

    VEHICLE_INTERIOR_COLOR = Semantic(
        id="vehicleInteriorColor",
        ref="schema:vehicleInteriorColor",
        text="""The color or color combination of the interior of the vehicle.""",
    )

    NURSING = Semantic(
        id="Nursing",
        ref="schema:Nursing",
        text="""A health profession of a person formally educated and trained in the care of the sick or infirm person.""",
    )

    PAYMENT_CARD = Semantic(
        id="PaymentCard",
        ref="schema:PaymentCard",
        text="""A payment method using a credit, debit, store or other card to associate the payment with an account.""",
    )

    PROFILE_PAGE = Semantic(
        id="ProfilePage",
        ref="schema:ProfilePage",
        text="""Web page type: Profile page.""",
    )

    DAY_OF_WEEK = Semantic(
        id="DayOfWeek",
        ref="schema:DayOfWeek",
        text="""The day of the week, e.g. used to specify to which day the opening hours of an OpeningHoursSpecification refer.

Originally, URLs from [GoodRelations](http://purl.org/goodrelations/v1) were used (for [[Monday]], [[Tuesday]], [[Wednesday]], [[Thursday]], [[Friday]], [[Saturday]], [[Sunday]] plus a special entry for [[PublicHolidays]]); these have now been integrated directly into schema.org.
      """,
    )

    DURATION = Semantic(
        id="duration",
        ref="schema:duration",
        text="""The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).""",
    )

    ORGANIZATION = Semantic(
        id="Organization",
        ref="schema:Organization",
        text="""An organization such as a school, NGO, corporation, club, etc.""",
    )

    MUSIC_RELEASE = Semantic(
        id="MusicRelease",
        ref="schema:MusicRelease",
        text="""A MusicRelease is a specific release of a music album.""",
    )

    MEMBERSHIP_POINTS_EARNED = Semantic(
        id="membershipPointsEarned",
        ref="schema:membershipPointsEarned",
        text="""The number of membership points earned by the member. If necessary, the unitText can be used to express the units the points are issued in. (e.g. stars, miles, etc.)""",
    )

    PAINTING = Semantic(id="Painting", ref="schema:Painting", text="""A painting.""")

    E_U_ENERGY_EFFICIENCY_CATEGORY_A2_PLUS = Semantic(
        id="EUEnergyEfficiencyCategoryA2Plus",
        ref="schema:EUEnergyEfficiencyCategoryA2Plus",
        text="""Represents EU Energy Efficiency Class A++ as defined in EU energy labeling regulations.""",
    )

    MIXED_EVENT_ATTENDANCE_MODE = Semantic(
        id="MixedEventAttendanceMode",
        ref="schema:MixedEventAttendanceMode",
        text="""MixedEventAttendanceMode - an event that is conducted as a combination of both offline and online modes.""",
    )

    VIDEO = Semantic(
        id="video", ref="schema:video", text="""An embedded video object."""
    )

    BACK_ORDER = Semantic(
        id="BackOrder",
        ref="schema:BackOrder",
        text="""Indicates that the item is available on back order.""",
    )

    ARRIVE_ACTION = Semantic(
        id="ArriveAction",
        ref="schema:ArriveAction",
        text="""The act of arriving at a place. An agent arrives at a destination from a fromLocation, optionally with participants.""",
    )

    ITEM_LIST_ELEMENT = Semantic(
        id="itemListElement",
        ref="schema:itemListElement",
        text="""For itemListElement values, you can use simple strings (e.g. "Peter", "Paul", "Mary"), existing entities, or use ListItem.\\n\\nText values are best if the elements in the list are plain strings. Existing entities are best for a simple, unordered list of existing things in your data. ListItem is used with ordered lists when you want to provide additional context about the element in that list or when the same item might be in different places in different lists.\\n\\nNote: The order of elements in your mark-up is not sufficient for indicating the order or elements.  Use ListItem with a \'position\' property in such cases.""",
    )

    BILLING_PERIOD = Semantic(
        id="billingPeriod",
        ref="schema:billingPeriod",
        text="""The time interval used to compute the invoice.""",
    )

    CLEANING_FEE = Semantic(
        id="CleaningFee",
        ref="schema:CleaningFee",
        text="""Represents the cleaning fee part of the total price for an offered product, for example a vacation rental.""",
    )

    PHARMACY = Semantic(
        id="Pharmacy", ref="schema:Pharmacy", text="""A pharmacy or drugstore."""
    )

    SOURCE_ORGANIZATION = Semantic(
        id="sourceOrganization",
        ref="schema:sourceOrganization",
        text="""The Organization on whose behalf the creator was working.""",
    )

    NIGHT_CLUB = Semantic(
        id="NightClub", ref="schema:NightClub", text="""A nightclub or discotheque."""
    )

    NONPROFIT501K = Semantic(
        id="Nonprofit501k",
        ref="schema:Nonprofit501k",
        text="""Nonprofit501k: Non-profit type referring to Child Care Organizations.""",
    )

    NONPROFIT501C17 = Semantic(
        id="Nonprofit501c17",
        ref="schema:Nonprofit501c17",
        text="""Nonprofit501c17: Non-profit type referring to Supplemental Unemployment Benefit Trusts.""",
    )

    TRAVEL_BANS = Semantic(
        id="travelBans",
        ref="schema:travelBans",
        text="""Information about travel bans, e.g. in the context of a pandemic.""",
    )

    OWNERSHIP_INFO = Semantic(
        id="OwnershipInfo",
        ref="schema:OwnershipInfo",
        text="""A structured value providing information about when a certain organization or person owned a certain product.""",
    )

    STUDY_DESIGN = Semantic(
        id="studyDesign",
        ref="schema:studyDesign",
        text="""Specifics about the observational study design (enumerated).""",
    )

    DISTANCE = Semantic(
        id="distance",
        ref="schema:distance",
        text="""The distance travelled, e.g. exercising or travelling.""",
    )

    MONETARY_GRANT = Semantic(
        id="MonetaryGrant", ref="schema:MonetaryGrant", text="""A monetary grant."""
    )

    COMIC_SERIES = Semantic(
        id="ComicSeries",
        ref="schema:ComicSeries",
        text="""A sequential publication of comic stories under a
    	unifying title, for example "The Amazing Spider-Man" or "Groo the
    	Wanderer".""",
    )

    MEDIA_OBJECT = Semantic(
        id="MediaObject",
        ref="schema:MediaObject",
        text="""A media object, such as an image, video, or audio object embedded in a web page or a downloadable dataset i.e. DataDownload. Note that a creative work may have many media objects associated with it on the same web page. For example, a page about a single song (MusicRecording) may have a music video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject\'s).""",
    )

    IS_GIFT = Semantic(
        id="isGift",
        ref="schema:isGift",
        text="""Was the offer accepted as a gift for someone other than the buyer.""",
    )

    STREET_ADDRESS = Semantic(
        id="streetAddress",
        ref="schema:streetAddress",
        text="""The street address. For example, 1600 Amphitheatre Pkwy.""",
    )

    COST_CATEGORY = Semantic(
        id="costCategory",
        ref="schema:costCategory",
        text="""The category of cost, such as wholesale, retail, reimbursement cap, etc.""",
    )

    IMAGE_OBJECT = Semantic(
        id="ImageObject", ref="schema:ImageObject", text="""An image file."""
    )

    PAYMENT_DUE = Semantic(
        id="PaymentDue",
        ref="schema:PaymentDue",
        text="""The payment is due, but still within an acceptable time to be received.""",
    )

    TAXI_VEHICLE_USAGE = Semantic(
        id="TaxiVehicleUsage",
        ref="schema:TaxiVehicleUsage",
        text="""Indicates the usage of the car as a taxi.""",
    )

    OFFERS_PRESCRIPTION_BY_MAIL = Semantic(
        id="offersPrescriptionByMail",
        ref="schema:offersPrescriptionByMail",
        text="""Whether prescriptions can be delivered by mail.""",
    )

    COLORIST = Semantic(
        id="colorist",
        ref="schema:colorist",
        text="""The individual who adds color to inked drawings.""",
    )

    MEMBER = Semantic(
        id="member",
        ref="schema:member",
        text="""A member of an Organization or a ProgramMembership. Organizations can be members of organizations; ProgramMembership is typically for individuals.""",
    )

    PREGNANCY_CATEGORY = Semantic(
        id="pregnancyCategory",
        ref="schema:pregnancyCategory",
        text="""Pregnancy category of this drug.""",
    )

    CARDIOVASCULAR_EXAM = Semantic(
        id="CardiovascularExam",
        ref="schema:CardiovascularExam",
        text="""Cardiovascular system assessment withclinical examination.""",
    )

    LEFT_HAND_DRIVING = Semantic(
        id="LeftHandDriving",
        ref="schema:LeftHandDriving",
        text="""The steering position is on the left side of the vehicle (viewed from the main direction of driving).""",
    )

    ORDER_IN_TRANSIT = Semantic(
        id="OrderInTransit",
        ref="schema:OrderInTransit",
        text="""OrderStatus representing that an order is in transit.""",
    )

    IN_CODE_SET = Semantic(
        id="inCodeSet",
        ref="schema:inCodeSet",
        text="""A [[CategoryCodeSet]] that contains this category code.""",
    )

    DISCUSSES = Semantic(
        id="discusses",
        ref="schema:discusses",
        text="""Specifies the CreativeWork associated with the UserComment.""",
    )

    MEDICAL_TEST_PANEL = Semantic(
        id="MedicalTestPanel",
        ref="schema:MedicalTestPanel",
        text="""Any collection of tests commonly ordered together.""",
    )

    APPLICATION_SUITE = Semantic(
        id="applicationSuite",
        ref="schema:applicationSuite",
        text="""The name of the application suite to which the application belongs (e.g. Excel belongs to Office).""",
    )

    WEARABLE_SIZE_SYSTEM_U_S = Semantic(
        id="WearableSizeSystemUS",
        ref="schema:WearableSizeSystemUS",
        text="""United States size system for wearables.""",
    )

    OPENS = Semantic(
        id="opens",
        ref="schema:opens",
        text="""The opening hour of the place or service on the given day(s) of the week.""",
    )

    DEFINED_TERM_SET = Semantic(
        id="DefinedTermSet",
        ref="schema:DefinedTermSet",
        text="""A set of defined terms for example a set of categories or a classification scheme, a glossary, dictionary or enumeration.""",
    )

    HYPER_TOC_ENTRY = Semantic(
        id="HyperTocEntry",
        ref="schema:HyperTocEntry",
        text="""A HyperToEntry is an item within a [[HyperToc]], which represents a hypertext table of contents for complex media objects, such as [[VideoObject]], [[AudioObject]]. The media object itself is indicated using [[associatedMedia]]. Each section of interest within that content can be described with a [[HyperTocEntry]], with associated [[startOffset]] and [[endOffset]]. When several entries are all from the same file, [[associatedMedia]] is used on the overarching [[HyperTocEntry]]; if the content has been split into multiple files, they can be referenced using [[associatedMedia]] on each [[HyperTocEntry]].""",
    )

    AVAILABLE_TEST = Semantic(
        id="availableTest",
        ref="schema:availableTest",
        text="""A diagnostic test or procedure offered by this lab.""",
    )

    HEALTH_PLAN_COPAY = Semantic(
        id="healthPlanCopay",
        ref="schema:healthPlanCopay",
        text="""Whether The copay amount.""",
    )

    TO_RECIPIENT = Semantic(
        id="toRecipient",
        ref="schema:toRecipient",
        text="""A sub property of recipient. The recipient who was directly sent the message.""",
    )

    GENDER = Semantic(
        id="gender",
        ref="schema:gender",
        text="""Gender of something, typically a [[Person]], but possibly also fictional characters, animals, etc. While https://schema.org/Male and https://schema.org/Female may be used, text strings are also acceptable for people who do not identify as a binary gender. The [[gender]] property can also be used in an extended sense to cover e.g. the gender of sports teams. As with the gender of individuals, we do not try to enumerate all possibilities. A mixed-gender [[SportsTeam]] can be indicated with a text value of "Mixed".""",
    )

    RATING_COUNT = Semantic(
        id="ratingCount",
        ref="schema:ratingCount",
        text="""The count of total number of ratings.""",
    )

    WATCH_ACTION = Semantic(
        id="WatchAction",
        ref="schema:WatchAction",
        text="""The act of consuming dynamic/moving visual content.""",
    )

    DEPARTURE_GATE = Semantic(
        id="departureGate",
        ref="schema:departureGate",
        text="""Identifier of the flight\'s departure gate.""",
    )

    REPORT = Semantic(
        id="Report",
        ref="schema:Report",
        text="""A Report generated by governmental or non-governmental organization.""",
    )

    NOTARY = Semantic(id="Notary", ref="schema:Notary", text="""A notary.""")

    MEDICAL_INDICATION = Semantic(
        id="MedicalIndication",
        ref="schema:MedicalIndication",
        text="""A condition or factor that indicates use of a medical therapy, including signs, symptoms, risk factors, anatomical states, etc.""",
    )

    SPECIALTY = Semantic(
        id="Specialty",
        ref="schema:Specialty",
        text="""Any branch of a field in which people typically develop specific expertise, usually after significant study, time, and effort.""",
    )

    DISTILLERY = Semantic(
        id="Distillery", ref="schema:Distillery", text="""A distillery."""
    )

    YEARS_IN_OPERATION = Semantic(
        id="yearsInOperation",
        ref="schema:yearsInOperation",
        text="""The age of the business.""",
    )

    QUANTITATIVE_VALUE = Semantic(
        id="QuantitativeValue",
        ref="schema:QuantitativeValue",
        text=""" A point value or interval for product characteristics and other purposes.""",
    )

    DEPARTMENT_STORE = Semantic(
        id="DepartmentStore",
        ref="schema:DepartmentStore",
        text="""A department store.""",
    )

    T_V_SERIES = Semantic(
        id="TVSeries",
        ref="schema:TVSeries",
        text="""CreativeWorkSeries dedicated to TV broadcast and associated online delivery.""",
    )

    INFORM_ACTION = Semantic(
        id="InformAction",
        ref="schema:InformAction",
        text="""The act of notifying someone of information pertinent to them, with no expectation of a response.""",
    )

    ANATOMICAL_STRUCTURE = Semantic(
        id="AnatomicalStructure",
        ref="schema:AnatomicalStructure",
        text="""Any part of the human body, typically a component of an anatomical system. Organs, tissues, and cells are all anatomical structures.""",
    )

    SIGNIFICANT_LINKS = Semantic(
        id="significantLinks",
        ref="schema:significantLinks",
        text="""The most significant URLs on the page. Typically, these are the non-navigation links that are clicked on the most.""",
    )

    SCREENING_HEALTH_ASPECT = Semantic(
        id="ScreeningHealthAspect",
        ref="schema:ScreeningHealthAspect",
        text="""Content about how to screen or further filter a topic.""",
    )

    OUT_OF_STOCK = Semantic(
        id="OutOfStock",
        ref="schema:OutOfStock",
        text="""Indicates that the item is out of stock.""",
    )

    AMENITY_FEATURE = Semantic(
        id="amenityFeature",
        ref="schema:amenityFeature",
        text="""An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic property does not make a statement about whether the feature is included in an offer for the main accommodation or available at extra costs.""",
    )

    EXPECTED_ARRIVAL_FROM = Semantic(
        id="expectedArrivalFrom",
        ref="schema:expectedArrivalFrom",
        text="""The earliest date the package may arrive.""",
    )

    Q_A_PAGE = Semantic(
        id="QAPage",
        ref="schema:QAPage",
        text="""A QAPage is a WebPage focussed on a specific Question and its Answer(s), e.g. in a question answering site or documenting Frequently Asked Questions (FAQs).""",
    )

    SEATING_CAPACITY = Semantic(
        id="seatingCapacity",
        ref="schema:seatingCapacity",
        text="""The number of persons that can be seated (e.g. in a vehicle), both in terms of the physical space available, and in terms of limitations set by law.\\n\\nTypical unit code(s): C62 for persons """,
    )

    HOW_PERFORMED = Semantic(
        id="howPerformed",
        ref="schema:howPerformed",
        text="""How the procedure is performed.""",
    )

    RENTAL_CAR_RESERVATION = Semantic(
        id="RentalCarReservation",
        ref="schema:RentalCarReservation",
        text="""A reservation for a rental car.\\n\\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.""",
    )

    LOCKER_DELIVERY = Semantic(
        id="LockerDelivery",
        ref="schema:LockerDelivery",
        text="""A DeliveryMethod in which an item is made available via locker.""",
    )

    RECIPIENT = Semantic(
        id="recipient",
        ref="schema:recipient",
        text="""A sub property of participant. The participant who is at the receiving end of the action.""",
    )

    MEDICAL_SIGN_OR_SYMPTOM = Semantic(
        id="MedicalSignOrSymptom",
        ref="schema:MedicalSignOrSymptom",
        text="""Any feature associated or not with a medical condition. In medicine a symptom is generally subjective while a sign is objective.""",
    )

    EMPLOYER_REVIEW = Semantic(
        id="EmployerReview",
        ref="schema:EmployerReview",
        text="""An [[EmployerReview]] is a review of an [[Organization]] regarding its role as an employer, written by a current or former employee of that organization.""",
    )

    DATA_CATALOG = Semantic(
        id="DataCatalog", ref="schema:DataCatalog", text="""A collection of datasets."""
    )

    AVAILABLE_THROUGH = Semantic(
        id="availableThrough",
        ref="schema:availableThrough",
        text="""After this date, the item will no longer be available for pickup.""",
    )

    BENEFITS_SUMMARY_URL = Semantic(
        id="benefitsSummaryUrl",
        ref="schema:benefitsSummaryUrl",
        text="""The URL that goes directly to the summary of benefits and coverage for the specific standard plan or plan variation.""",
    )

    NEWS_ARTICLE = Semantic(
        id="NewsArticle",
        ref="schema:NewsArticle",
        text="""A NewsArticle is an article whose content reports news, or provides background context and supporting materials for understanding the news.

A more detailed overview of [schema.org News markup](/docs/news.html) is also available.
""",
    )

    PARENTAL_SUPPORT = Semantic(
        id="ParentalSupport",
        ref="schema:ParentalSupport",
        text="""ParentalSupport: this is a benefit for parental support.""",
    )

    REFUND_TYPE_ENUMERATION = Semantic(
        id="RefundTypeEnumeration",
        ref="schema:RefundTypeEnumeration",
        text="""Enumerates several kinds of product return refund types.""",
    )

    MERCHANT_RETURN_NOT_PERMITTED = Semantic(
        id="MerchantReturnNotPermitted",
        ref="schema:MerchantReturnNotPermitted",
        text="""Specifies that product returns are not permitted.""",
    )

    APPLICATION_START_DATE = Semantic(
        id="applicationStartDate",
        ref="schema:applicationStartDate",
        text="""The date at which the program begins collecting applications for the next enrollment cycle.""",
    )

    ACCEPTED_PAYMENT_METHOD = Semantic(
        id="acceptedPaymentMethod",
        ref="schema:acceptedPaymentMethod",
        text="""The payment method(s) accepted by seller for this offer.""",
    )

    E_U_ENERGY_EFFICIENCY_CATEGORY_B = Semantic(
        id="EUEnergyEfficiencyCategoryB",
        ref="schema:EUEnergyEfficiencyCategoryB",
        text="""Represents EU Energy Efficiency Class B as defined in EU energy labeling regulations.""",
    )

    CLOTHING_STORE = Semantic(
        id="ClothingStore", ref="schema:ClothingStore", text="""A clothing store."""
    )

    IDENTIFYING_EXAM = Semantic(
        id="identifyingExam",
        ref="schema:identifyingExam",
        text="""A physical examination that can identify this sign.""",
    )

    AUTO_RENTAL = Semantic(
        id="AutoRental", ref="schema:AutoRental", text="""A car rental business."""
    )

    ROOFING_CONTRACTOR = Semantic(
        id="RoofingContractor",
        ref="schema:RoofingContractor",
        text="""A roofing contractor.""",
    )

    HAS_REPRESENTATION = Semantic(
        id="hasRepresentation",
        ref="schema:hasRepresentation",
        text="""A common representation such as a protein sequence or chemical structure for this entity. For images use schema.org/image.""",
    )

    FAMILY_NAME = Semantic(
        id="familyName",
        ref="schema:familyName",
        text="""Family name. In the U.S., the last name of a Person.""",
    )

    LIMITED_AVAILABILITY = Semantic(
        id="LimitedAvailability",
        ref="schema:LimitedAvailability",
        text="""Indicates that the item has limited availability.""",
    )

    NONPROFIT501C20 = Semantic(
        id="Nonprofit501c20",
        ref="schema:Nonprofit501c20",
        text="""Nonprofit501c20: Non-profit type referring to Group Legal Services Plan Organizations.""",
    )

    SPORTS_ORGANIZATION = Semantic(
        id="SportsOrganization",
        ref="schema:SportsOrganization",
        text="""Represents the collection of all sports organizations, including sports teams, governing bodies, and sports associations.""",
    )

    TAXI_SERVICE = Semantic(
        id="TaxiService",
        ref="schema:TaxiService",
        text="""A service for a vehicle for hire with a driver for local travel. Fares are usually calculated based on distance traveled.""",
    )

    WHOLESALE = Semantic(
        id="Wholesale",
        ref="schema:Wholesale",
        text="""The drug\'s cost represents the wholesale acquisition cost of the drug.""",
    )

    INCLUDED_COMPOSITION = Semantic(
        id="includedComposition",
        ref="schema:includedComposition",
        text="""Smaller compositions included in this work (e.g. a movement in a symphony).""",
    )

    BUSINESS_FUNCTION = Semantic(
        id="businessFunction",
        ref="schema:businessFunction",
        text="""The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.""",
    )

    HOW_TO_SECTION = Semantic(
        id="HowToSection",
        ref="schema:HowToSection",
        text="""A sub-grouping of steps in the instructions for how to achieve a result (e.g. steps for making a pie crust within a pie recipe).""",
    )

    ENDOCRINE = Semantic(
        id="Endocrine",
        ref="schema:Endocrine",
        text="""A specific branch of medical science that pertains to diagnosis and treatment of disorders of endocrine glands and their secretions.""",
    )

    TERMINATED = Semantic(
        id="Terminated", ref="schema:Terminated", text="""Terminated."""
    )

    SCHOOL = Semantic(id="School", ref="schema:School", text="""A school.""")

    MUSIC_STORE = Semantic(
        id="MusicStore", ref="schema:MusicStore", text="""A music store."""
    )

    INCENTIVES = Semantic(
        id="incentives",
        ref="schema:incentives",
        text="""Description of bonus and commission compensation aspects of the job.""",
    )

    WEARABLE_MEASUREMENT_COLLAR = Semantic(
        id="WearableMeasurementCollar",
        ref="schema:WearableMeasurementCollar",
        text="""Measurement of the collar, for example of a shirt""",
    )

    EXERCISE_GYM = Semantic(
        id="ExerciseGym", ref="schema:ExerciseGym", text="""A gym."""
    )

    ENGINE_SPECIFICATION = Semantic(
        id="EngineSpecification",
        ref="schema:EngineSpecification",
        text="""Information about the engine of the vehicle. A vehicle can have multiple engines represented by multiple engine specification entities.""",
    )

    SHIPPING_RATE = Semantic(
        id="shippingRate",
        ref="schema:shippingRate",
        text="""The shipping rate is the cost of shipping to the specified destination. Typically, the maxValue and currency values (of the [[MonetaryAmount]]) are most appropriate.""",
    )

    FUNDED_ITEM = Semantic(
        id="fundedItem",
        ref="schema:fundedItem",
        text="""Indicates an item funded or sponsored through a [[Grant]].""",
    )

    MIXTAPE_ALBUM = Semantic(
        id="MixtapeAlbum", ref="schema:MixtapeAlbum", text="""MixtapeAlbum."""
    )

    BY_ARTIST = Semantic(
        id="byArtist",
        ref="schema:byArtist",
        text="""The artist that performed this album or recording.""",
    )

    PRODUCT = Semantic(
        id="Product",
        ref="schema:Product",
        text="""Any offered product or service. For example: a pair of shoes; a concert ticket; the rental of a car; a haircut; or an episode of a TV show streamed online.""",
    )

    NAICS = Semantic(
        id="naics",
        ref="schema:naics",
        text="""The North American Industry Classification System (NAICS) code for a particular organization or business person.""",
    )

    VENDOR = Semantic(
        id="vendor",
        ref="schema:vendor",
        text="""\'vendor\' is an earlier term for \'seller\'.""",
    )

    RELATED_LINK = Semantic(
        id="relatedLink",
        ref="schema:relatedLink",
        text="""A link related to this web page, for example to other related web pages.""",
    )

    ALTERNATE_NAME = Semantic(
        id="alternateName",
        ref="schema:alternateName",
        text="""An alias for the item.""",
    )

    SAFETY_HEALTH_ASPECT = Semantic(
        id="SafetyHealthAspect",
        ref="schema:SafetyHealthAspect",
        text="""Content about the safety-related aspects of a health topic.""",
    )

    SAME_AS = Semantic(
        id="sameAs",
        ref="schema:sameAs",
        text="""URL of a reference Web page that unambiguously indicates the item\'s identity. E.g. the URL of the item\'s Wikipedia page, Wikidata entry, or official website.""",
    )

    TRANSLATOR = Semantic(
        id="translator",
        ref="schema:translator",
        text="""Organization or person who adapts a creative work to different languages, regional differences and technical requirements of a target market, or that translates during some event.""",
    )

    ITEM_LIST = Semantic(
        id="ItemList",
        ref="schema:ItemList",
        text="""A list of items of any sort&#x2014;for example, Top 10 Movies About Weathermen, or Top 100 Party Songs. Not to be confused with HTML lists, which are often used only for formatting.""",
    )

    RESORT = Semantic(
        id="Resort",
        ref="schema:Resort",
        text="""A resort is a place used for relaxation or recreation, attracting visitors for holidays or vacations. Resorts are places, towns or sometimes commercial establishment operated by a single company (Source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Resort">http://en.wikipedia.org/wiki/Resort</a>).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
    """,
    )

    CONTROL_ACTION = Semantic(
        id="ControlAction",
        ref="schema:ControlAction",
        text="""An agent controls a device or application.""",
    )

    INFECTIOUS_DISEASE = Semantic(
        id="InfectiousDisease",
        ref="schema:InfectiousDisease",
        text="""An infectious disease is a clinically evident human disease resulting from the presence of pathogenic microbial agents, like pathogenic viruses, pathogenic bacteria, fungi, protozoa, multicellular parasites, and prions. To be considered an infectious disease, such pathogens are known to be able to cause this disease.""",
    )

    RUNTIME_PLATFORM = Semantic(
        id="runtimePlatform",
        ref="schema:runtimePlatform",
        text="""Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3, .Net Framework 3.0).""",
    )

    MUSCLE_ACTION = Semantic(
        id="muscleAction",
        ref="schema:muscleAction",
        text="""The movement the muscle generates.""",
    )

    EVIDENCE_LEVEL_B = Semantic(
        id="EvidenceLevelB",
        ref="schema:EvidenceLevelB",
        text="""Data derived from a single randomized trial, or nonrandomized studies.""",
    )

    PRODUCES = Semantic(
        id="produces",
        ref="schema:produces",
        text="""The tangible thing generated by the service, e.g. a passport, permit, etc.""",
    )

    SCHEDULED_TIME = Semantic(
        id="scheduledTime",
        ref="schema:scheduledTime",
        text="""The time the object is scheduled to.""",
    )

    LASER_DISC_FORMAT = Semantic(
        id="LaserDiscFormat", ref="schema:LaserDiscFormat", text="""LaserDiscFormat."""
    )

    NON_EQUAL = Semantic(
        id="nonEqual",
        ref="schema:nonEqual",
        text="""This ordering relation for qualitative values indicates that the subject is not equal to the object.""",
    )

    DATE_TIME = Semantic(
        id="DateTime",
        ref="schema:DateTime",
        text="""A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] (see Chapter 5.4 of ISO 8601).""",
    )

    RATING = Semantic(
        id="Rating",
        ref="schema:Rating",
        text="""A rating is an evaluation on a numeric scale, such as 1 to 5 stars.""",
    )

    PUBLICATION_EVENT = Semantic(
        id="PublicationEvent",
        ref="schema:PublicationEvent",
        text="""A PublicationEvent corresponds indifferently to the event of publication for a CreativeWork of any type e.g. a broadcast event, an on-demand event, a book/journal publication via a variety of delivery media.""",
    )

    LODGING_UNIT_DESCRIPTION = Semantic(
        id="lodgingUnitDescription",
        ref="schema:lodgingUnitDescription",
        text="""A full description of the lodging unit.""",
    )

    POSITION = Semantic(
        id="position",
        ref="schema:position",
        text="""The position of an item in a series or sequence of items.""",
    )

    PROTOZOA = Semantic(
        id="Protozoa",
        ref="schema:Protozoa",
        text="""Single-celled organism that causes an infection.""",
    )

    BODY_MEASUREMENT_CHEST = Semantic(
        id="BodyMeasurementChest",
        ref="schema:BodyMeasurementChest",
        text="""Maximum girth of chest. Used, for example, to fit men\'s suits.""",
    )

    BRAND = Semantic(
        id="Brand",
        ref="schema:Brand",
        text="""A brand is a name used by an organization or business person for labeling a product, product group, or similar.""",
    )

    STRUCTURED_VALUE = Semantic(
        id="StructuredValue",
        ref="schema:StructuredValue",
        text="""Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.""",
    )

    BUS_RESERVATION = Semantic(
        id="BusReservation",
        ref="schema:BusReservation",
        text="""A reservation for bus travel. \\n\\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].""",
    )

    SEAT_SECTION = Semantic(
        id="seatSection",
        ref="schema:seatSection",
        text="""The section location of the reserved seat (e.g. Orchestra).""",
    )

    SUBTITLE_LANGUAGE = Semantic(
        id="subtitleLanguage",
        ref="schema:subtitleLanguage",
        text="""Languages in which subtitles/captions are available, in [IETF BCP 47 standard format](http://tools.ietf.org/html/bcp47).""",
    )

    E_P_RELEASE = Semantic(
        id="EPRelease", ref="schema:EPRelease", text="""EPRelease."""
    )

    XPATH = Semantic(
        id="xpath",
        ref="schema:xpath",
        text="""An XPath, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".""",
    )

    CURRENCY_CONVERSION_SERVICE = Semantic(
        id="CurrencyConversionService",
        ref="schema:CurrencyConversionService",
        text="""A service to convert funds from one currency to another currency.""",
    )

    DISAGREE_ACTION = Semantic(
        id="DisagreeAction",
        ref="schema:DisagreeAction",
        text="""The act of expressing a difference of opinion with the object. An agent disagrees to/about an object (a proposition, topic or theme) with participants.""",
    )

    RESERVATION_HOLD = Semantic(
        id="ReservationHold",
        ref="schema:ReservationHold",
        text="""The status of a reservation on hold pending an update like credit card number or flight changes.""",
    )

    PRE_SALE = Semantic(
        id="PreSale",
        ref="schema:PreSale",
        text="""Indicates that the item is available for ordering and delivery before general availability.""",
    )

    TRANSLATION_OF_WORK = Semantic(
        id="translationOfWork",
        ref="schema:translationOfWork",
        text="""The work that this work has been translated from. e.g. 物种起源 is a translationOf “On the Origin of Species”""",
    )

    IS_BASED_ON = Semantic(
        id="isBasedOn",
        ref="schema:isBasedOn",
        text="""A resource from which this work is derived or from which it is a modification or adaption.""",
    )

    ADDRESS_LOCALITY = Semantic(
        id="addressLocality",
        ref="schema:addressLocality",
        text="""The locality in which the street address is, and which is in the region. For example, Mountain View.""",
    )

    EMPLOYEE = Semantic(
        id="employee",
        ref="schema:employee",
        text="""Someone working for this organization.""",
    )

    ORDER_PROCESSING = Semantic(
        id="OrderProcessing",
        ref="schema:OrderProcessing",
        text="""OrderStatus representing that an order is being processed.""",
    )

    COUNTRY = Semantic(id="Country", ref="schema:Country", text="""A country.""")

    DELIVERY_TIME_SETTINGS = Semantic(
        id="DeliveryTimeSettings",
        ref="schema:DeliveryTimeSettings",
        text="""A DeliveryTimeSettings represents re-usable pieces of shipping information, relating to timing. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of a [[OfferShippingDetails]]. Several occurrences can be published, distinguished (and identified/referenced) by their different values for [[transitTimeLabel]].""",
    )

    ELIGIBLE_DURATION = Semantic(
        id="eligibleDuration",
        ref="schema:eligibleDuration",
        text="""The duration for which the given offer is valid.""",
    )

    WORK_BASED_PROGRAM = Semantic(
        id="WorkBasedProgram",
        ref="schema:WorkBasedProgram",
        text="""A program with both an educational and employment component. Typically based at a workplace and structured around work-based learning, with the aim of instilling competencies related to an occupation. WorkBasedProgram is used to distinguish programs such as apprenticeships from school, college or other classroom based educational programs.""",
    )

    GEO_COVERS = Semantic(
        id="geoCovers",
        ref="schema:geoCovers",
        text="""Represents a relationship between two geometries (or the places they represent), relating a covering geometry to a covered geometry. "Every point of b is a point of (the interior or boundary of) a". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).""",
    )

    HAS_BIO_POLYMER_SEQUENCE = Semantic(
        id="hasBioPolymerSequence",
        ref="schema:hasBioPolymerSequence",
        text="""A symbolic representation of a BioChemEnity. For example, a nucleotide sequence of a Gene or an amino acid sequence of a Protein.""",
    )

    SIBLING = Semantic(
        id="sibling", ref="schema:sibling", text="""A sibling of the person."""
    )

    E_U_ENERGY_EFFICIENCY_CATEGORY_A1_PLUS = Semantic(
        id="EUEnergyEfficiencyCategoryA1Plus",
        ref="schema:EUEnergyEfficiencyCategoryA1Plus",
        text="""Represents EU Energy Efficiency Class A+ as defined in EU energy labeling regulations.""",
    )

    NONPROFIT501C13 = Semantic(
        id="Nonprofit501c13",
        ref="schema:Nonprofit501c13",
        text="""Nonprofit501c13: Non-profit type referring to Cemetery Companies.""",
    )

    INFECTIOUS_AGENT_CLASS = Semantic(
        id="InfectiousAgentClass",
        ref="schema:InfectiousAgentClass",
        text="""Classes of agents or pathogens that transmit infectious diseases. Enumerated type.""",
    )

    NAME = Semantic(id="name", ref="schema:name", text="""The name of the item.""")

    YIELD = Semantic(
        id="yield",
        ref="schema:yield",
        text="""The quantity that results by performing instructions. For example, a paper airplane, 10 personalized candles.""",
    )

    VENUE_MAP = Semantic(
        id="VenueMap",
        ref="schema:VenueMap",
        text="""A venue map (e.g. for malls, auditoriums, museums, etc.).""",
    )

    EXERCISE_ACTION = Semantic(
        id="ExerciseAction",
        ref="schema:ExerciseAction",
        text="""The act of participating in exertive activity for the purposes of improving health and fitness.""",
    )

    CASH_BACK = Semantic(
        id="cashBack",
        ref="schema:cashBack",
        text="""A cardholder benefit that pays the cardholder a small percentage of their net expenditures.""",
    )

    SCHEMA_VERSION = Semantic(
        id="schemaVersion",
        ref="schema:schemaVersion",
        text="""Indicates (by URL or string) a particular version of a schema used in some CreativeWork. This property was created primarily to
    indicate the use of a specific schema.org release, e.g. ```10.0``` as a simple string, or more explicitly via URL, ```https://schema.org/docs/releases.html#v10.0```. There may be situations in which other schemas might usefully be referenced this way, e.g. ```http://dublincore.org/specifications/dublin-core/dces/1999-07-02/``` but this has not been carefully explored in the community.""",
    )

    PHYSICAL_THERAPY = Semantic(
        id="PhysicalTherapy",
        ref="schema:PhysicalTherapy",
        text="""A process of progressive physical care and rehabilitation aimed at improving a health condition.""",
    )

    EVENT_RESCHEDULED = Semantic(
        id="EventRescheduled",
        ref="schema:EventRescheduled",
        text="""The event has been rescheduled. The event\'s previousStartDate should be set to the old date and the startDate should be set to the event\'s new date. (If the event has been rescheduled multiple times, the previousStartDate property may be repeated).""",
    )

    ADMINISTRATIVE_AREA = Semantic(
        id="AdministrativeArea",
        ref="schema:AdministrativeArea",
        text="""A geographical region, typically under the jurisdiction of a particular government.""",
    )

    PREPEND_ACTION = Semantic(
        id="PrependAction",
        ref="schema:PrependAction",
        text="""The act of inserting at the beginning if an ordered collection.""",
    )

    MULTI_CENTER_TRIAL = Semantic(
        id="MultiCenterTrial",
        ref="schema:MultiCenterTrial",
        text="""A trial that takes place at multiple centers.""",
    )

    BREWERY = Semantic(id="Brewery", ref="schema:Brewery", text="""Brewery.""")

    CREATE_ACTION = Semantic(
        id="CreateAction",
        ref="schema:CreateAction",
        text="""The act of deliberately creating/producing/generating/building a result out of the agent.""",
    )

    SINGLE_FAMILY_RESIDENCE = Semantic(
        id="SingleFamilyResidence",
        ref="schema:SingleFamilyResidence",
        text="""Residence type: Single-family home.""",
    )

    VEHICLE = Semantic(
        id="Vehicle",
        ref="schema:Vehicle",
        text="""A vehicle is a device that is designed or used to transport people or cargo over land, water, air, or through space.""",
    )

    WEARABLE_SIZE_GROUP_ENUMERATION = Semantic(
        id="WearableSizeGroupEnumeration",
        ref="schema:WearableSizeGroupEnumeration",
        text="""Enumerates common size groups (also known as "size types") for wearable products.""",
    )

    CARGO_VOLUME = Semantic(
        id="cargoVolume",
        ref="schema:cargoVolume",
        text="""The available volume for cargo or luggage. For automobiles, this is usually the trunk volume.\\n\\nTypical unit code(s): LTR for liters, FTQ for cubic foot/feet\\n\\nNote: You can use [[minValue]] and [[maxValue]] to indicate ranges.""",
    )

    CHILD_TAXON = Semantic(
        id="childTaxon",
        ref="schema:childTaxon",
        text="""Closest child taxa of the taxon in question.""",
    )

    DEMO_ALBUM = Semantic(id="DemoAlbum", ref="schema:DemoAlbum", text="""DemoAlbum.""")

    MATH_EXPRESSION = Semantic(
        id="mathExpression",
        ref="schema:mathExpression",
        text="""A mathematical expression (e.g. \'x^2-3x=0\') that may be solved for a specific variable, simplified, or transformed. This can take many formats, e.g. LaTeX, Ascii-Math, or math as you would write with a keyboard.""",
    )

    REVIEWED_BY = Semantic(
        id="reviewedBy",
        ref="schema:reviewedBy",
        text="""People or organizations that have reviewed the content on this web page for accuracy and/or completeness.""",
    )

    RETURN_FEES = Semantic(
        id="returnFees",
        ref="schema:returnFees",
        text="""The type of return fees for purchased products (for any return reason)""",
    )

    REST_PERIODS = Semantic(
        id="restPeriods",
        ref="schema:restPeriods",
        text="""How often one should break from the activity.""",
    )

    ALCOHOL_WARNING = Semantic(
        id="alcoholWarning",
        ref="schema:alcoholWarning",
        text="""Any precaution, guidance, contraindication, etc. related to consumption of alcohol while taking this drug.""",
    )

    PUBLIC_HEALTH = Semantic(
        id="PublicHealth",
        ref="schema:PublicHealth",
        text="""Branch of medicine that pertains to the health services to improve and protect community health, especially epidemiology, sanitation, immunization, and preventive medicine.""",
    )

    FLOOR_LIMIT = Semantic(
        id="floorLimit",
        ref="schema:floorLimit",
        text="""A floor limit is the amount of money above which credit card transactions must be authorized.""",
    )

    QUESTION = Semantic(
        id="question",
        ref="schema:question",
        text="""A sub property of object. A question.""",
    )

    CONTAGIOUSNESS_HEALTH_ASPECT = Semantic(
        id="ContagiousnessHealthAspect",
        ref="schema:ContagiousnessHealthAspect",
        text="""Content about contagion mechanisms and contagiousness information over the topic.""",
    )

    FLIGHT_RESERVATION = Semantic(
        id="FlightReservation",
        ref="schema:FlightReservation",
        text="""A reservation for air travel.\\n\\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].""",
    )

    APPEND_ACTION = Semantic(
        id="AppendAction",
        ref="schema:AppendAction",
        text="""The act of inserting at the end if an ordered collection.""",
    )

    SIBLINGS = Semantic(
        id="siblings", ref="schema:siblings", text="""A sibling of the person."""
    )

    EMPLOYER_OVERVIEW = Semantic(
        id="employerOverview",
        ref="schema:employerOverview",
        text="""A description of the employer, career opportunities and work environment for this position.""",
    )

    DIFFERENTIAL_DIAGNOSIS = Semantic(
        id="differentialDiagnosis",
        ref="schema:differentialDiagnosis",
        text="""One of a set of differential diagnoses for the condition. Specifically, a closely-related or competing diagnosis typically considered later in the cognitive process whereby this medical condition is distinguished from others most likely responsible for a similar collection of signs and symptoms to reach the most parsimonious diagnosis or diagnoses in a patient.""",
    )

    ROLE_NAME = Semantic(
        id="roleName",
        ref="schema:roleName",
        text="""A role played, performed or filled by a person or organization. For example, the team of creators for a comic book might fill the roles named \'inker\', \'penciller\', and \'letterer\'; or an athlete in a SportsTeam might play in the position named \'Quarterback\'.""",
    )

    NONPROFIT501C9 = Semantic(
        id="Nonprofit501c9",
        ref="schema:Nonprofit501c9",
        text="""Nonprofit501c9: Non-profit type referring to Voluntary Employee Beneficiary Associations.""",
    )

    STADIUM_OR_ARENA = Semantic(
        id="StadiumOrArena", ref="schema:StadiumOrArena", text="""A stadium."""
    )

    PHYSICIAN = Semantic(
        id="Physician", ref="schema:Physician", text="""A doctor\'s office."""
    )

    MONETARY_AMOUNT_DISTRIBUTION = Semantic(
        id="MonetaryAmountDistribution",
        ref="schema:MonetaryAmountDistribution",
        text="""A statistical distribution of monetary amounts.""",
    )

    SERVICE_POSTAL_ADDRESS = Semantic(
        id="servicePostalAddress",
        ref="schema:servicePostalAddress",
        text="""The address for accessing the service by mail.""",
    )

    DIET = Semantic(
        id="diet",
        ref="schema:diet",
        text="""A sub property of instrument. The diet used in this action.""",
    )

    PROGRAMMING_MODEL = Semantic(
        id="programmingModel",
        ref="schema:programmingModel",
        text="""Indicates whether API is managed or unmanaged.""",
    )

    THEATER_EVENT = Semantic(
        id="TheaterEvent",
        ref="schema:TheaterEvent",
        text="""Event type: Theater performance.""",
    )

    LINK_RELATIONSHIP = Semantic(
        id="linkRelationship",
        ref="schema:linkRelationship",
        text="""Indicates the relationship type of a Web link. """,
    )

    MEETING_ROOM = Semantic(
        id="MeetingRoom",
        ref="schema:MeetingRoom",
        text="""A meeting room, conference room, or conference hall is a room provided for singular events such as business conferences and meetings (Source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Conference_hall">http://en.wikipedia.org/wiki/Conference_hall</a>).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
""",
    )

    NUMBER_OF_LOAN_PAYMENTS = Semantic(
        id="numberOfLoanPayments",
        ref="schema:numberOfLoanPayments",
        text="""The number of payments contractually required at origination to repay the loan. For monthly paying loans this is the number of months from the contractual first payment date to the maturity date.""",
    )

    QUANTITY = Semantic(
        id="Quantity",
        ref="schema:Quantity",
        text="""Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like \'3 Kg\' or \'4 milligrams\'.""",
    )

    EVENT_STATUS_TYPE = Semantic(
        id="EventStatusType",
        ref="schema:EventStatusType",
        text="""EventStatusType is an enumeration type whose instances represent several states that an Event may be in.""",
    )

    COUNTRY_OF_ORIGIN = Semantic(
        id="countryOfOrigin",
        ref="schema:countryOfOrigin",
        text="""The country of origin of something, including products as well as creative  works such as movie and TV content.

In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties such as [[contentLocation]] and [[locationCreated]] may be more applicable.

In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.""",
    )

    ACTION_APPLICATION = Semantic(
        id="actionApplication",
        ref="schema:actionApplication",
        text="""An application that can complete the request.""",
    )

    REVIEW_RATING = Semantic(
        id="reviewRating",
        ref="schema:reviewRating",
        text="""The rating given in this review. Note that reviews can themselves be rated. The ```reviewRating``` applies to rating given by the review. The [[aggregateRating]] property applies to the review itself, as a creative work.""",
    )

    PREVIOUS_START_DATE = Semantic(
        id="previousStartDate",
        ref="schema:previousStartDate",
        text="""Used in conjunction with eventStatus for rescheduled or cancelled events. This property contains the previously scheduled start date. For rescheduled events, the startDate property should be used for the newly scheduled start date. In the (rare) case of an event that has been postponed and rescheduled multiple times, this field may be repeated.""",
    )

    DRAINS_TO = Semantic(
        id="drainsTo",
        ref="schema:drainsTo",
        text="""The vasculature that the vein drains into.""",
    )

    NUMBER_OF_BEDS = Semantic(
        id="numberOfBeds",
        ref="schema:numberOfBeds",
        text="""The quantity of the given bed type available in the HotelRoom, Suite, House, or Apartment.""",
    )

    ARCHIVE_COMPONENT = Semantic(
        id="ArchiveComponent",
        ref="schema:ArchiveComponent",
        text="""An intangible type to be applied to any archive content, carrying with it a set of properties required to describe archival items and collections.""",
    )

    BAR_OR_PUB = Semantic(
        id="BarOrPub", ref="schema:BarOrPub", text="""A bar or pub."""
    )

    ENERGY_CONSUMPTION_DETAILS = Semantic(
        id="EnergyConsumptionDetails",
        ref="schema:EnergyConsumptionDetails",
        text="""EnergyConsumptionDetails represents information related to the energy efficiency of a product that consumes energy. The information that can be provided is based on international regulations such as for example [EU directive 2017/1369](https://eur-lex.europa.eu/eli/reg/2017/1369/oj) for energy labeling and the [Energy labeling rule](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/energy-water-use-labeling-consumer) under the Energy Policy and Conservation Act (EPCA) in the US.""",
    )

    EDUCATIONAL_OCCUPATIONAL_CREDENTIAL = Semantic(
        id="EducationalOccupationalCredential",
        ref="schema:EducationalOccupationalCredential",
        text="""An educational or occupational credential. A diploma, academic degree, certification, qualification, badge, etc., that may be awarded to a person or other entity that meets the requirements defined by the credentialer.""",
    )

    DRUG_UNIT = Semantic(
        id="drugUnit",
        ref="schema:drugUnit",
        text="""The unit in which the drug is measured, e.g. \'5 mg tablet\'.""",
    )

    LEGISLATION_LEGAL_FORCE = Semantic(
        id="legislationLegalForce",
        ref="schema:legislationLegalForce",
        text="""Whether the legislation is currently in force, not in force, or partially in force.""",
    )

    MULTICELLULAR_PARASITE = Semantic(
        id="MulticellularParasite",
        ref="schema:MulticellularParasite",
        text="""Multicellular parasite that causes an infection.""",
    )

    FIND_ACTION = Semantic(
        id="FindAction",
        ref="schema:FindAction",
        text="""The act of finding an object.\\n\\nRelated actions:\\n\\n* [[SearchAction]]: FindAction is generally lead by a SearchAction, but not necessarily.""",
    )

    OFFER_FOR_LEASE = Semantic(
        id="OfferForLease",
        ref="schema:OfferForLease",
        text="""An [[OfferForLease]] in Schema.org represents an [[Offer]] to lease out something, i.e. an [[Offer]] whose
  [[businessFunction]] is [lease out](http://purl.org/goodrelations/v1#LeaseOut.). See [Good Relations](https://en.wikipedia.org/wiki/GoodRelations) for
  background on the underlying concepts.
  """,
    )

    EXCHANGE_REFUND = Semantic(
        id="ExchangeRefund",
        ref="schema:ExchangeRefund",
        text="""Specifies that a refund can be done as an exchange for the same product.""",
    )

    AVAILABLE_SERVICE = Semantic(
        id="availableService",
        ref="schema:availableService",
        text="""A medical service available from this provider.""",
    )

    DOSE_VALUE = Semantic(
        id="doseValue",
        ref="schema:doseValue",
        text="""The value of the dose, e.g. 500.""",
    )

    PROPRIETARY_NAME = Semantic(
        id="proprietaryName",
        ref="schema:proprietaryName",
        text="""Proprietary name given to the diet plan, typically by its originator or creator.""",
    )

    PROGRAM_PREREQUISITES = Semantic(
        id="programPrerequisites",
        ref="schema:programPrerequisites",
        text="""Prerequisites for enrolling in the program.""",
    )

    TIP_ACTION = Semantic(
        id="TipAction",
        ref="schema:TipAction",
        text="""The act of giving money voluntarily to a beneficiary in recognition of services rendered.""",
    )

    NUMBER_OF_ROOMS = Semantic(
        id="numberOfRooms",
        ref="schema:numberOfRooms",
        text="""The number of rooms (excluding bathrooms and closets) of the accommodation or lodging business.
Typical unit code(s): ROM for room or C62 for no unit. The type of room can be put in the unitText property of the QuantitativeValue.""",
    )

    AVAILABLE_IN = Semantic(
        id="availableIn",
        ref="schema:availableIn",
        text="""The location in which the strength is available.""",
    )

    HAS_BIO_CHEM_ENTITY_PART = Semantic(
        id="hasBioChemEntityPart",
        ref="schema:hasBioChemEntityPart",
        text="""Indicates a BioChemEntity that (in some sense) has this BioChemEntity as a part. """,
    )

    ASK_ACTION = Semantic(
        id="AskAction",
        ref="schema:AskAction",
        text="""The act of posing a question / favor to someone.\\n\\nRelated actions:\\n\\n* [[ReplyAction]]: Appears generally as a response to AskAction.""",
    )

    PARENT_TAXON = Semantic(
        id="parentTaxon",
        ref="schema:parentTaxon",
        text="""Closest parent taxon of the taxon in question.""",
    )

    H_V_A_C_BUSINESS = Semantic(
        id="HVACBusiness",
        ref="schema:HVACBusiness",
        text="""A business that provide Heating, Ventilation and Air Conditioning services.""",
    )

    APPLICABLE_LOCATION = Semantic(
        id="applicableLocation",
        ref="schema:applicableLocation",
        text="""The location in which the status applies.""",
    )

    RADIO_SERIES = Semantic(
        id="RadioSeries",
        ref="schema:RadioSeries",
        text="""CreativeWorkSeries dedicated to radio broadcast and associated online delivery.""",
    )

    TREATMENT_INDICATION = Semantic(
        id="TreatmentIndication",
        ref="schema:TreatmentIndication",
        text="""An indication for treating an underlying condition, symptom, etc.""",
    )

    ERROR = Semantic(
        id="error",
        ref="schema:error",
        text="""For failed actions, more information on the cause of the failure.""",
    )

    WESTERN_CONVENTIONAL = Semantic(
        id="WesternConventional",
        ref="schema:WesternConventional",
        text="""The conventional Western system of medicine, that aims to apply the best available evidence gained from the scientific method to clinical decision making. Also known as conventional or Western medicine.""",
    )

    TRAIN_TRIP = Semantic(
        id="TrainTrip",
        ref="schema:TrainTrip",
        text="""A trip on a commercial train line.""",
    )

    JOB_POSTING = Semantic(
        id="JobPosting",
        ref="schema:JobPosting",
        text="""A listing that describes a job opening in a certain organization.""",
    )

    PRINT_PAGE = Semantic(
        id="printPage",
        ref="schema:printPage",
        text="""If this NewsArticle appears in print, this field indicates the name of the page on which the article is found. Please note that this field is intended for the exact page name (e.g. A5, B18).""",
    )

    BUS_STATION = Semantic(
        id="BusStation", ref="schema:BusStation", text="""A bus station."""
    )

    PLAY_ACTION = Semantic(
        id="PlayAction",
        ref="schema:PlayAction",
        text="""The act of playing/exercising/training/performing for enjoyment, leisure, recreation, Competition or exercise.\\n\\nRelated actions:\\n\\n* [[ListenAction]]: Unlike ListenAction (which is under ConsumeAction), PlayAction refers to performing for an audience or at an event, rather than consuming music.\\n* [[WatchAction]]: Unlike WatchAction (which is under ConsumeAction), PlayAction refers to showing/displaying for an audience or at an event, rather than consuming visual content.""",
    )

    WEARABLE_SIZE_SYSTEM_U_K = Semantic(
        id="WearableSizeSystemUK",
        ref="schema:WearableSizeSystemUK",
        text="""United Kingdom size system for wearables.""",
    )

    FUEL_EFFICIENCY = Semantic(
        id="fuelEfficiency",
        ref="schema:fuelEfficiency",
        text="""The distance traveled per unit of fuel used; most commonly miles per gallon (mpg) or kilometers per liter (km/L).\\n\\n* Note 1: There are unfortunately no standard unit codes for miles per gallon or kilometers per liter. Use [[unitText]] to indicate the unit of measurement, e.g. mpg or km/L.\\n* Note 2: There are two ways of indicating the fuel consumption, [[fuelConsumption]] (e.g. 8 liters per 100 km) and [[fuelEfficiency]] (e.g. 30 miles per gallon). They are reciprocal.\\n* Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use [[valueReference]] to link the value for the fuel economy to another value.""",
    )

    WEARABLE_MEASUREMENT_OUTSIDE_LEG = Semantic(
        id="WearableMeasurementOutsideLeg",
        ref="schema:WearableMeasurementOutsideLeg",
        text="""Measurement of the outside leg, for example of pants""",
    )

    COLLECTION = Semantic(
        id="Collection",
        ref="schema:Collection",
        text="""A collection of items e.g. creative works or products.""",
    )

    MANUFACTURER = Semantic(
        id="manufacturer",
        ref="schema:manufacturer",
        text="""The manufacturer of the product.""",
    )

    EVIDENCE_LEVEL = Semantic(
        id="evidenceLevel",
        ref="schema:evidenceLevel",
        text="""Strength of evidence of the data used to formulate the guideline (enumerated).""",
    )

    MERCHANT_RETURN_LINK = Semantic(
        id="merchantReturnLink",
        ref="schema:merchantReturnLink",
        text="""Specifies a Web page or service by URL, for product returns.""",
    )

    PROGRAMMING_LANGUAGE = Semantic(
        id="programmingLanguage",
        ref="schema:programmingLanguage",
        text="""The computer programming language.""",
    )

    ESTIMATED_COST = Semantic(
        id="estimatedCost",
        ref="schema:estimatedCost",
        text="""The estimated cost of the supply or supplies consumed when performing instructions.""",
    )

    MOVE_ACTION = Semantic(
        id="MoveAction",
        ref="schema:MoveAction",
        text="""The act of an agent relocating to a place.\\n\\nRelated actions:\\n\\n* [[TransferAction]]: Unlike TransferAction, the subject of the move is a living Person or Organization rather than an inanimate object.""",
    )

    SKIN = Semantic(
        id="Skin",
        ref="schema:Skin",
        text="""Skin assessment with clinical examination.""",
    )

    RUNS_TO = Semantic(
        id="runsTo",
        ref="schema:runsTo",
        text="""The vasculature the lymphatic structure runs, or efferents, to.""",
    )

    DIRECTOR = Semantic(
        id="director",
        ref="schema:director",
        text="""A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.""",
    )

    F_D_ACATEGORY_D = Semantic(
        id="FDAcategoryD",
        ref="schema:FDAcategoryD",
        text="""A designation by the US FDA signifying that there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience or studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.""",
    )

    MIDDLE_SCHOOL = Semantic(
        id="MiddleSchool",
        ref="schema:MiddleSchool",
        text="""A middle school (typically for children aged around 11-14, although this varies somewhat).""",
    )

    LYRICS = Semantic(
        id="lyrics", ref="schema:lyrics", text="""The words in the song."""
    )

    GRAPHIC_NOVEL = Semantic(
        id="GraphicNovel",
        ref="schema:GraphicNovel",
        text="""Book format: GraphicNovel. May represent a bound collection of ComicIssue instances.""",
    )

    BRAND = Semantic(
        id="brand",
        ref="schema:brand",
        text="""The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.""",
    )

    POSTAL_CODE_RANGE_SPECIFICATION = Semantic(
        id="PostalCodeRangeSpecification",
        ref="schema:PostalCodeRangeSpecification",
        text="""Indicates a range of postalcodes, usually defined as the set of valid codes between [[postalCodeBegin]] and [[postalCodeEnd]], inclusively.""",
    )

    APPLICATION = Semantic(
        id="application",
        ref="schema:application",
        text="""An application that can complete the request.""",
    )

    EMERGENCY = Semantic(
        id="Emergency",
        ref="schema:Emergency",
        text="""A specific branch of medical science that deals with the evaluation and initial treatment of medical conditions caused by trauma or sudden illness.""",
    )

    DUNS = Semantic(
        id="duns",
        ref="schema:duns",
        text="""The Dun & Bradstreet DUNS number for identifying an organization or business person.""",
    )

    STORAGE_REQUIREMENTS = Semantic(
        id="storageRequirements",
        ref="schema:storageRequirements",
        text="""Storage requirements (free space required).""",
    )

    SINGLE_RELEASE = Semantic(
        id="SingleRelease", ref="schema:SingleRelease", text="""SingleRelease."""
    )

    SIGNIFICANCE = Semantic(
        id="significance",
        ref="schema:significance",
        text="""The significance associated with the superficial anatomy; as an example, how characteristics of the superficial anatomy can suggest underlying medical conditions or courses of treatment.""",
    )

    NONPROFIT501C15 = Semantic(
        id="Nonprofit501c15",
        ref="schema:Nonprofit501c15",
        text="""Nonprofit501c15: Non-profit type referring to Mutual Insurance Companies or Associations.""",
    )

    EMPLOYER_AGGREGATE_RATING = Semantic(
        id="EmployerAggregateRating",
        ref="schema:EmployerAggregateRating",
        text="""An aggregate rating of an Organization related to its role as an employer.""",
    )

    CATEGORY = Semantic(
        id="category",
        ref="schema:category",
        text="""A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.""",
    )

    MEDICAL_AUDIENCE = Semantic(
        id="medicalAudience",
        ref="schema:medicalAudience",
        text="""Medical audience for page.""",
    )

    AUTO_BODY_SHOP = Semantic(
        id="AutoBodyShop", ref="schema:AutoBodyShop", text="""Auto body shop."""
    )

    EMPLOYMENT_AGENCY = Semantic(
        id="EmploymentAgency",
        ref="schema:EmploymentAgency",
        text="""An employment agency.""",
    )

    TICKET = Semantic(
        id="Ticket",
        ref="schema:Ticket",
        text="""Used to describe a ticket to an event, a flight, a bus ride, etc.""",
    )

    RXCUI = Semantic(
        id="rxcui",
        ref="schema:rxcui",
        text="""The RxCUI drug identifier from RXNORM.""",
    )

    EDIT_E_I_D_R = Semantic(
        id="editEIDR",
        ref="schema:editEIDR",
        text="""An [EIDR](https://eidr.org/) (Entertainment Identifier Registry) [[identifier]] representing a specific edit / edition for a work of film or television.

For example, the motion picture known as "Ghostbusters" whose [[titleEIDR]] is "10.5240/7EC7-228A-510A-053E-CBB8-J", has several edits e.g. "10.5240/1F2A-E1C5-680A-14C6-E76B-I" and "10.5240/8A35-3BEE-6497-5D12-9E4F-3".

Since schema.org types like [[Movie]] and [[TVEpisode]] can be used for both works and their multiple expressions, it is possible to use [[titleEIDR]] alone (for a general description), or alongside [[editEIDR]] for a more edit-specific description.
""",
    )

    WEARABLE_SIZE_GROUP_REGULAR = Semantic(
        id="WearableSizeGroupRegular",
        ref="schema:WearableSizeGroupRegular",
        text="""Size group "Regular" for wearables.""",
    )

    CONTAINS_PLACE = Semantic(
        id="containsPlace",
        ref="schema:containsPlace",
        text="""The basic containment relation between a place and another that it contains.""",
    )

    SATIRE_OR_PARODY_CONTENT = Semantic(
        id="SatireOrParodyContent",
        ref="schema:SatireOrParodyContent",
        text="""Content coded \'satire or parody content\' in a [[MediaReview]], considered in the context of how it was published or shared.

For a [[VideoObject]] to be \'satire or parody content\': A video that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)

For an [[ImageObject]] to be \'satire or parody content\': An image that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)

For an [[ImageObject]] with embedded text to be \'satire or parody content\': An image that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)

For an [[AudioObject]] to be \'satire or parody content\': Audio that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)
""",
    )

    BROADCAST_FREQUENCY_SPECIFICATION = Semantic(
        id="BroadcastFrequencySpecification",
        ref="schema:BroadcastFrequencySpecification",
        text="""The frequency in MHz and the modulation used for a particular BroadcastService.""",
    )

    PRODUCTION_COMPANY = Semantic(
        id="productionCompany",
        ref="schema:productionCompany",
        text="""The production company or studio responsible for the item e.g. series, video game, episode etc.""",
    )

    HAS_MERCHANT_RETURN_POLICY = Semantic(
        id="hasMerchantReturnPolicy",
        ref="schema:hasMerchantReturnPolicy",
        text="""Specifies a MerchantReturnPolicy that may be applicable.""",
    )

    RADIO_STATION = Semantic(
        id="RadioStation", ref="schema:RadioStation", text="""A radio station."""
    )

    GENDER_TYPE = Semantic(
        id="GenderType", ref="schema:GenderType", text="""An enumeration of genders."""
    )

    VETERINARY_CARE = Semantic(
        id="VeterinaryCare", ref="schema:VeterinaryCare", text="""A vet\'s office."""
    )

    SD_PUBLISHER = Semantic(
        id="sdPublisher",
        ref="schema:sdPublisher",
        text="""Indicates the party responsible for generating and publishing the current structured data markup, typically in cases where the structured data is derived automatically from existing published content but published on a different site. For example, student projects and open data initiatives often re-publish existing content with more explicitly structured metadata. The
[[sdPublisher]] property helps make such practices more explicit.""",
    )

    UNOFFICIAL_LEGAL_VALUE = Semantic(
        id="UnofficialLegalValue",
        ref="schema:UnofficialLegalValue",
        text="""Indicates that a document has no particular or special standing (e.g. a republication of a law by a private publisher).""",
    )

    SERIES = Semantic(
        id="Series",
        ref="schema:Series",
        text="""A Series in schema.org is a group of related items, typically but not necessarily of the same kind. See also [[CreativeWorkSeries]], [[EventSeries]].""",
    )

    NONPROFIT501C10 = Semantic(
        id="Nonprofit501c10",
        ref="schema:Nonprofit501c10",
        text="""Nonprofit501c10: Non-profit type referring to Domestic Fraternal Societies and Associations.""",
    )

    BORROWER = Semantic(
        id="borrower",
        ref="schema:borrower",
        text="""A sub property of participant. The person that borrows the object being lent.""",
    )

    GLUTEN_FREE_DIET = Semantic(
        id="GlutenFreeDiet",
        ref="schema:GlutenFreeDiet",
        text="""A diet exclusive of gluten.""",
    )

    HANDLING_TIME = Semantic(
        id="handlingTime",
        ref="schema:handlingTime",
        text="""The typical delay between the receipt of the order and the goods either leaving the warehouse or being prepared for pickup, in case the delivery method is on site pickup. Typical properties: minValue, maxValue, unitCode (d for DAY).  This is by common convention assumed to mean business days (if a unitCode is used, coded as "d"), i.e. only counting days when the business normally operates.""",
    )

    ACTION_ACCESSIBILITY_REQUIREMENT = Semantic(
        id="actionAccessibilityRequirement",
        ref="schema:actionAccessibilityRequirement",
        text="""A set of requirements that a must be fulfilled in order to perform an Action. If more than one value is specied, fulfilling one set of requirements will allow the Action to be performed.""",
    )

    COST_CURRENCY = Semantic(
        id="costCurrency",
        ref="schema:costCurrency",
        text="""The currency (in 3-letter of the drug cost. See: http://en.wikipedia.org/wiki/ISO_4217. """,
    )

    U_R_L = Semantic(id="URL", ref="schema:URL", text="""Data type: URL.""")

    WIN_ACTION = Semantic(
        id="WinAction",
        ref="schema:WinAction",
        text="""The act of achieving victory in a competitive activity.""",
    )

    STORE = Semantic(id="Store", ref="schema:Store", text="""A retail good store.""")

    SATIRICAL_ARTICLE = Semantic(
        id="SatiricalArticle",
        ref="schema:SatiricalArticle",
        text="""An [[Article]] whose content is primarily [[satirical]](https://en.wikipedia.org/wiki/Satire) in nature, i.e. unlikely to be literally true. A satirical article is sometimes but not necessarily also a [[NewsArticle]]. [[ScholarlyArticle]]s are also sometimes satirized.""",
    )

    COMMENT_TEXT = Semantic(
        id="commentText",
        ref="schema:commentText",
        text="""The text of the UserComment.""",
    )

    IDENTIFIER = Semantic(
        id="identifier",
        ref="schema:identifier",
        text="""The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.
        """,
    )

    BOOK = Semantic(id="Book", ref="schema:Book", text="""A book.""")

    SERVING_SIZE = Semantic(
        id="servingSize",
        ref="schema:servingSize",
        text="""The serving size, in terms of the number of volume or mass.""",
    )

    BLOOD_TEST = Semantic(
        id="BloodTest",
        ref="schema:BloodTest",
        text="""A medical test performed on a sample of a patient\'s blood.""",
    )

    PLAYERS_ONLINE = Semantic(
        id="playersOnline",
        ref="schema:playersOnline",
        text="""Number of players on the server.""",
    )

    SPECIAL_COMMITMENTS = Semantic(
        id="specialCommitments",
        ref="schema:specialCommitments",
        text="""Any special commitments associated with this job posting. Valid entries include VeteranCommit, MilitarySpouseCommit, etc.""",
    )

    INSERT_ACTION = Semantic(
        id="InsertAction",
        ref="schema:InsertAction",
        text="""The act of adding at a specific location in an ordered collection.""",
    )

    EXPECTED_ARRIVAL_UNTIL = Semantic(
        id="expectedArrivalUntil",
        ref="schema:expectedArrivalUntil",
        text="""The latest date the package may arrive.""",
    )

    WEARABLE_MEASUREMENT_CUP = Semantic(
        id="WearableMeasurementCup",
        ref="schema:WearableMeasurementCup",
        text="""Measurement of the cup, for example of a bra""",
    )

    POTENTIAL_ACTION = Semantic(
        id="potentialAction",
        ref="schema:potentialAction",
        text="""Indicates a potential Action, which describes an idealized action in which this thing would play an \'object\' role.""",
    )

    WEARABLE_SIZE_SYSTEM_C_N = Semantic(
        id="WearableSizeSystemCN",
        ref="schema:WearableSizeSystemCN",
        text="""Chinese size system for wearables.""",
    )

    NUMBER_OF_CREDITS = Semantic(
        id="numberOfCredits",
        ref="schema:numberOfCredits",
        text="""The number of credits or units awarded by a Course or required to complete an EducationalOccupationalProgram.""",
    )

    BROADCASTER = Semantic(
        id="broadcaster",
        ref="schema:broadcaster",
        text="""The organization owning or operating the broadcast service.""",
    )

    DISABILITY_SUPPORT = Semantic(
        id="DisabilitySupport",
        ref="schema:DisabilitySupport",
        text="""DisabilitySupport: this is a benefit for disability support.""",
    )

    HAS_ENERGY_CONSUMPTION_DETAILS = Semantic(
        id="hasEnergyConsumptionDetails",
        ref="schema:hasEnergyConsumptionDetails",
        text="""Defines the energy efficiency Category (also known as "class" or "rating") for a product according to an international energy efficiency standard.""",
    )

    DATASET_TIME_INTERVAL = Semantic(
        id="datasetTimeInterval",
        ref="schema:datasetTimeInterval",
        text="""The range of temporal applicability of a dataset, e.g. for a 2011 census dataset, the year 2011 (in ISO 8601 time interval format).""",
    )

    AVAILABILITY_STARTS = Semantic(
        id="availabilityStarts",
        ref="schema:availabilityStarts",
        text="""The beginning of the availability of the product or service included in the offer.""",
    )

    LOCATION = Semantic(
        id="location",
        ref="schema:location",
        text="""The location of, for example, where an event is happening, where an organization is located, or where an action takes place.""",
    )

    OCCUPATION = Semantic(
        id="Occupation",
        ref="schema:Occupation",
        text="""A profession, may involve prolonged training and/or a formal qualification.""",
    )

    PLUMBER = Semantic(
        id="Plumber", ref="schema:Plumber", text="""A plumbing service."""
    )

    LICENSE = Semantic(
        id="license",
        ref="schema:license",
        text="""A license document that applies to this content, typically indicated by URL.""",
    )

    AUTHORITATIVE_LEGAL_VALUE = Semantic(
        id="AuthoritativeLegalValue",
        ref="schema:AuthoritativeLegalValue",
        text="""Indicates that the publisher gives some special status to the publication of the document. ("The Queens Printer" version of a UK Act of Parliament, or the PDF version of a Directive published by the EU Office of Publications). Something "Authoritative" is considered to be also [[OfficialLegalValue]]".""",
    )

    CAUSES_HEALTH_ASPECT = Semantic(
        id="CausesHealthAspect",
        ref="schema:CausesHealthAspect",
        text="""Information about the causes and main actions that gave rise to the topic.""",
    )

    IS_ACCEPTING_NEW_PATIENTS = Semantic(
        id="isAcceptingNewPatients",
        ref="schema:isAcceptingNewPatients",
        text="""Whether the provider is accepting new patients.""",
    )

    OPTICIAN = Semantic(
        id="Optician",
        ref="schema:Optician",
        text="""A store that sells reading glasses and similar devices for improving vision.""",
    )

    PARTY_SIZE = Semantic(
        id="partySize",
        ref="schema:partySize",
        text="""Number of people the reservation should accommodate.""",
    )

    GAME_PLATFORM = Semantic(
        id="gamePlatform",
        ref="schema:gamePlatform",
        text="""The electronic systems used to play <a href="http://en.wikipedia.org/wiki/Category:Video_game_platforms">video games</a>.""",
    )

    VALUE_PATTERN = Semantic(
        id="valuePattern",
        ref="schema:valuePattern",
        text="""Specifies a regular expression for testing literal values according to the HTML spec.""",
    )

    FLIGHT_NUMBER = Semantic(
        id="flightNumber",
        ref="schema:flightNumber",
        text="""The unique identifier for a flight including the airline IATA code. For example, if describing United flight 110, where the IATA code for United is \'UA\', the flightNumber is \'UA110\'.""",
    )

    TRAIN_NUMBER = Semantic(
        id="trainNumber",
        ref="schema:trainNumber",
        text="""The unique identifier for the train.""",
    )

    GERIATRIC = Semantic(
        id="Geriatric",
        ref="schema:Geriatric",
        text="""A specific branch of medical science that is concerned with the diagnosis and treatment of diseases, debilities and provision of care to the aged.""",
    )

    GOVERNMENT_OFFICE = Semantic(
        id="GovernmentOffice",
        ref="schema:GovernmentOffice",
        text="""A government office&#x2014;for example, an IRS or DMV office.""",
    )

    SINGLE_CENTER_TRIAL = Semantic(
        id="SingleCenterTrial",
        ref="schema:SingleCenterTrial",
        text="""A trial that takes place at a single center.""",
    )

    PRESCHOOL = Semantic(
        id="Preschool", ref="schema:Preschool", text="""A preschool."""
    )

    ITEM_DEFECT_RETURN_LABEL_SOURCE = Semantic(
        id="itemDefectReturnLabelSource",
        ref="schema:itemDefectReturnLabelSource",
        text="""The method (from an enumeration) by which the customer obtains a return shipping label for a defect product.""",
    )

    LODGING_BUSINESS = Semantic(
        id="LodgingBusiness",
        ref="schema:LodgingBusiness",
        text="""A lodging business, such as a motel, hotel, or inn.""",
    )

    EDU_QUESTION_TYPE = Semantic(
        id="eduQuestionType",
        ref="schema:eduQuestionType",
        text="""For questions that are part of learning resources (e.g. Quiz), eduQuestionType indicates the format of question being given. Example: "Multiple choice", "Open ended", "Flashcard".""",
    )

    MENU = Semantic(
        id="menu",
        ref="schema:menu",
        text="""Either the actual menu as a structured representation, as text, or a URL of the menu.""",
    )

    WORD_COUNT = Semantic(
        id="wordCount",
        ref="schema:wordCount",
        text="""The number of words in the text of the Article.""",
    )

    AVAILABLE_ON_DEVICE = Semantic(
        id="availableOnDevice",
        ref="schema:availableOnDevice",
        text="""Device required to run the application. Used in cases where a specific make/model is required to run the application.""",
    )

    ORDERED_ITEM = Semantic(
        id="orderedItem", ref="schema:orderedItem", text="""The item ordered."""
    )

    DOWNLOAD_ACTION = Semantic(
        id="DownloadAction",
        ref="schema:DownloadAction",
        text="""The act of downloading an object.""",
    )

    JOB_LOCATION_TYPE = Semantic(
        id="jobLocationType",
        ref="schema:jobLocationType",
        text="""A description of the job location (e.g TELECOMMUTE for telecommute jobs).""",
    )

    ARTICLE_BODY = Semantic(
        id="articleBody",
        ref="schema:articleBody",
        text="""The actual body of the article.""",
    )

    HAIR_SALON = Semantic(
        id="HairSalon", ref="schema:HairSalon", text="""A hair salon."""
    )

    ROOF_LOAD = Semantic(
        id="roofLoad",
        ref="schema:roofLoad",
        text="""The permitted total weight of cargo and installations (e.g. a roof rack) on top of the vehicle.\\n\\nTypical unit code(s): KGM for kilogram, LBR for pound\\n\\n* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.\\n* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]]\\n* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.""",
    )

    STEERING_POSITION_VALUE = Semantic(
        id="SteeringPositionValue",
        ref="schema:SteeringPositionValue",
        text="""A value indicating a steering position.""",
    )

    LEGISLATION_IDENTIFIER = Semantic(
        id="legislationIdentifier",
        ref="schema:legislationIdentifier",
        text="""An identifier for the legislation. This can be either a string-based identifier, like the CELEX at EU level or the NOR in France, or a web-based, URL/URI identifier, like an ELI (European Legislation Identifier) or an URN-Lex.""",
    )

    INTERACTION_STATISTIC = Semantic(
        id="interactionStatistic",
        ref="schema:interactionStatistic",
        text="""The number of interactions for the CreativeWork using the WebSite or SoftwareApplication. The most specific child type of InteractionCounter should be used.""",
    )

    FOOD_WARNING = Semantic(
        id="foodWarning",
        ref="schema:foodWarning",
        text="""Any precaution, guidance, contraindication, etc. related to consumption of specific foods while taking this drug.""",
    )

    ACCEPT_ACTION = Semantic(
        id="AcceptAction",
        ref="schema:AcceptAction",
        text="""The act of committing to/adopting an object.\\n\\nRelated actions:\\n\\n* [[RejectAction]]: The antonym of AcceptAction.""",
    )

    ACCOUNT_MINIMUM_INFLOW = Semantic(
        id="accountMinimumInflow",
        ref="schema:accountMinimumInflow",
        text="""A minimum amount that has to be paid in every month.""",
    )

    ABDOMEN = Semantic(
        id="Abdomen", ref="schema:Abdomen", text="""Abdomen clinical examination."""
    )

    DRIVE_WHEEL_CONFIGURATION = Semantic(
        id="driveWheelConfiguration",
        ref="schema:driveWheelConfiguration",
        text="""The drive wheel configuration, i.e. which roadwheels will receive torque from the vehicle\'s engine via the drivetrain.""",
    )

    GRANT = Semantic(
        id="Grant",
        ref="schema:Grant",
        text="""A grant, typically financial or otherwise quantifiable, of resources. Typically a [[funder]] sponsors some [[MonetaryAmount]] to an [[Organization]] or [[Person]],
    sometimes not necessarily via a dedicated or long-lived [[Project]], resulting in one or more outputs, or [[fundedItem]]s. For financial sponsorship, indicate the [[funder]] of a [[MonetaryGrant]]. For non-financial support, indicate [[sponsor]] of [[Grant]]s of resources (e.g. office space).

Grants support  activities directed towards some agreed collective goals, often but not always organized as [[Project]]s. Long-lived projects are sometimes sponsored by a variety of grants over time, but it is also common for a project to be associated with a single grant.

The amount of a [[Grant]] is represented using [[amount]] as a [[MonetaryAmount]].
    """,
    )

    CO_OP = Semantic(
        id="CoOp",
        ref="schema:CoOp",
        text="""Play mode: CoOp. Co-operative games, where you play on the same team with friends.""",
    )

    PAYMENT_STATUS = Semantic(
        id="paymentStatus",
        ref="schema:paymentStatus",
        text="""The status of payment; whether the invoice has been paid or not.""",
    )

    MESSAGE_ATTACHMENT = Semantic(
        id="messageAttachment",
        ref="schema:messageAttachment",
        text="""A CreativeWork attached to the message.""",
    )

    SUGGESTED_MAX_AGE = Semantic(
        id="suggestedMaxAge",
        ref="schema:suggestedMaxAge",
        text="""Maximum recommended age in years for the audience or user.""",
    )

    USER_PLAYS = Semantic(
        id="UserPlays",
        ref="schema:UserPlays",
        text="""UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].""",
    )

    SCHOLARLY_ARTICLE = Semantic(
        id="ScholarlyArticle",
        ref="schema:ScholarlyArticle",
        text="""A scholarly article.""",
    )

    MEDICAL_AUDIENCE_TYPE = Semantic(
        id="MedicalAudienceType",
        ref="schema:MedicalAudienceType",
        text="""Target audiences types for medical web pages. Enumerated type.""",
    )

    REPEAT_COUNT = Semantic(
        id="repeatCount",
        ref="schema:repeatCount",
        text="""Defines the number of times a recurring [[Event]] will take place""",
    )

    SHIPPING_SETTINGS_LINK = Semantic(
        id="shippingSettingsLink",
        ref="schema:shippingSettingsLink",
        text="""Link to a page containing [[ShippingRateSettings]] and [[DeliveryTimeSettings]] details.""",
    )

    MEDICAL_STUDY_STATUS = Semantic(
        id="MedicalStudyStatus",
        ref="schema:MedicalStudyStatus",
        text="""The status of a medical study. Enumerated type.""",
    )

    OVERVIEW_HEALTH_ASPECT = Semantic(
        id="OverviewHealthAspect",
        ref="schema:OverviewHealthAspect",
        text="""Overview of the content. Contains a summarized view of the topic with the most relevant information for an introduction.""",
    )

    SOFTWARE_REQUIREMENTS = Semantic(
        id="softwareRequirements",
        ref="schema:softwareRequirements",
        text="""Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (Examples: DirectX, Java or .NET runtime).""",
    )

    ENTERTAINMENT_BUSINESS = Semantic(
        id="EntertainmentBusiness",
        ref="schema:EntertainmentBusiness",
        text="""A business providing entertainment.""",
    )

    MOTORCYCLE_DEALER = Semantic(
        id="MotorcycleDealer",
        ref="schema:MotorcycleDealer",
        text="""A motorcycle dealer.""",
    )

    WHEELBASE = Semantic(
        id="wheelbase",
        ref="schema:wheelbase",
        text="""The distance between the centers of the front and rear wheels.\\n\\nTypical unit code(s): CMT for centimeters, MTR for meters, INH for inches, FOT for foot/feet""",
    )

    UTTERANCES = Semantic(
        id="utterances",
        ref="schema:utterances",
        text="""Text of an utterances (spoken words, lyrics etc.) that occurs at a certain section of a media object, represented as a [[HyperTocEntry]].""",
    )

    PHONETIC_TEXT = Semantic(
        id="phoneticText",
        ref="schema:phoneticText",
        text="""Representation of a text [[textValue]] using the specified [[speechToTextMarkup]]. For example the city name of Houston in IPA: /ˈhjuːstən/.""",
    )

    ASSEMBLY = Semantic(
        id="assembly",
        ref="schema:assembly",
        text="""Library file name e.g., mscorlib.dll, system.web.dll.""",
    )

    HAS_CREDENTIAL = Semantic(
        id="hasCredential",
        ref="schema:hasCredential",
        text="""A credential awarded to the Person or Organization.""",
    )

    SYMPTOMS_HEALTH_ASPECT = Semantic(
        id="SymptomsHealthAspect",
        ref="schema:SymptomsHealthAspect",
        text="""Symptoms or related symptoms of a Topic.""",
    )

    DRUG = Semantic(
        id="Drug",
        ref="schema:Drug",
        text="""A chemical or biologic substance, used as a medical therapy, that has a physiological effect on an organism. Here the term drug is used interchangeably with the term medicine although clinical knowledge make a clear difference between them.""",
    )

    FOOD_ESTABLISHMENT = Semantic(
        id="foodEstablishment",
        ref="schema:foodEstablishment",
        text="""A sub property of location. The specific food establishment where the action occurred.""",
    )

    NONPROFIT_STATUS = Semantic(
        id="nonprofitStatus",
        ref="schema:nonprofitStatus",
        text="""nonprofit Status indicates the legal status of a non-profit organization in its primary place of business.""",
    )

    PAYMENT_COMPLETE = Semantic(
        id="PaymentComplete",
        ref="schema:PaymentComplete",
        text="""The payment has been received and processed.""",
    )

    VALUE_REQUIRED = Semantic(
        id="valueRequired",
        ref="schema:valueRequired",
        text="""Whether the property must be filled in to complete the action.  Default is false.""",
    )

    REGIONS_ALLOWED = Semantic(
        id="regionsAllowed",
        ref="schema:regionsAllowed",
        text="""The regions where the media is allowed. If not specified, then it\'s assumed to be allowed everywhere. Specify the countries in [ISO 3166 format](http://en.wikipedia.org/wiki/ISO_3166).""",
    )

    SERVICE_URL = Semantic(
        id="serviceUrl",
        ref="schema:serviceUrl",
        text="""The website to access the service.""",
    )

    COHORT_STUDY = Semantic(
        id="CohortStudy",
        ref="schema:CohortStudy",
        text="""Also known as a panel study. A cohort study is a form of longitudinal study used in medicine and social science. It is one type of study design and should be compared with a cross-sectional study.  A cohort is a group of people who share a common characteristic or experience within a defined period (e.g., are born, leave school, lose their job, are exposed to a drug or a vaccine, etc.). The comparison group may be the general population from which the cohort is drawn, or it may be another cohort of persons thought to have had little or no exposure to the substance under investigation, but otherwise similar. Alternatively, subgroups within the cohort may be compared with each other.""",
    )

    SURGICAL_PROCEDURE = Semantic(
        id="SurgicalProcedure",
        ref="schema:SurgicalProcedure",
        text="""A medical procedure involving an incision with instruments; performed for diagnose, or therapeutic purposes.""",
    )

    THEATER_GROUP = Semantic(
        id="TheaterGroup",
        ref="schema:TheaterGroup",
        text="""A theater group or company, for example, the Royal Shakespeare Company or Druid Theatre.""",
    )

    BROWSER_REQUIREMENTS = Semantic(
        id="browserRequirements",
        ref="schema:browserRequirements",
        text="""Specifies browser requirements in human-readable text. For example, \'requires HTML5 support\'.""",
    )

    PRICE_CURRENCY = Semantic(
        id="priceCurrency",
        ref="schema:priceCurrency",
        text="""The currency of the price, or a price component when attached to [[PriceSpecification]] and its subtypes.\\n\\nUse standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217) e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies e.g. "BTC"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types e.g. "Ithaca HOUR".""",
    )

    ENROLLING_BY_INVITATION = Semantic(
        id="EnrollingByInvitation",
        ref="schema:EnrollingByInvitation",
        text="""Enrolling participants by invitation only.""",
    )

    TITLE = Semantic(id="title", ref="schema:title", text="""The title of the job.""")

    PAYMENT_SERVICE = Semantic(
        id="PaymentService",
        ref="schema:PaymentService",
        text="""A Service to transfer funds from a person or organization to a beneficiary person or organization.""",
    )

    ACCESSIBILITY_FEATURE = Semantic(
        id="accessibilityFeature",
        ref="schema:accessibilityFeature",
        text="""Content features of the resource, such as accessible media, alternatives and supported enhancements for accessibility ([WebSchemas wiki lists possible values](http://www.w3.org/wiki/WebSchemas/Accessibility)).""",
    )

    WEARABLE_MEASUREMENT_LENGTH = Semantic(
        id="WearableMeasurementLength",
        ref="schema:WearableMeasurementLength",
        text="""Represents the length, for example of a dress""",
    )

    MERCHANT_RETURN_DAYS = Semantic(
        id="merchantReturnDays",
        ref="schema:merchantReturnDays",
        text="""Specifies either a fixed return date or the number of days (from the delivery date) that a product can be returned. Used when the [[returnPolicyCategory]] property is specified as [[MerchantReturnFiniteReturnWindow]].""",
    )

    PRIMARY_CARE = Semantic(
        id="PrimaryCare",
        ref="schema:PrimaryCare",
        text="""The medical care by a physician, or other health-care professional, who is the patient\'s first contact with the health-care system and who may recommend a specialist if necessary.""",
    )

    ARRIVAL_BOAT_TERMINAL = Semantic(
        id="arrivalBoatTerminal",
        ref="schema:arrivalBoatTerminal",
        text="""The terminal or port from which the boat arrives.""",
    )

    MENTIONS = Semantic(
        id="mentions",
        ref="schema:mentions",
        text="""Indicates that the CreativeWork contains a reference to, but is not necessarily about a concept.""",
    )

    ETHICS_POLICY = Semantic(
        id="ethicsPolicy",
        ref="schema:ethicsPolicy",
        text="""Statement about ethics policy, e.g. of a [[NewsMediaOrganization]] regarding journalistic and publishing practices, or of a [[Restaurant]], a page describing food source policies. In the case of a [[NewsMediaOrganization]], an ethicsPolicy is typically a statement describing the personal, organizational, and corporate standards of behavior expected by the organization.""",
    )

    WEB_APPLICATION = Semantic(
        id="WebApplication", ref="schema:WebApplication", text="""Web applications."""
    )

    NEXT_ITEM = Semantic(
        id="nextItem",
        ref="schema:nextItem",
        text="""A link to the ListItem that follows the current one.""",
    )

    CITY_HALL = Semantic(id="CityHall", ref="schema:CityHall", text="""A city hall.""")

    SHOE_STORE = Semantic(
        id="ShoeStore", ref="schema:ShoeStore", text="""A shoe store."""
    )

    FUEL_CAPACITY = Semantic(
        id="fuelCapacity",
        ref="schema:fuelCapacity",
        text="""The capacity of the fuel tank or in the case of electric cars, the battery. If there are multiple components for storage, this should indicate the total of all storage of the same type.\\n\\nTypical unit code(s): LTR for liters, GLL of US gallons, GLI for UK / imperial gallons, AMH for ampere-hours (for electrical vehicles).""",
    )

    CATALOG_NUMBER = Semantic(
        id="catalogNumber",
        ref="schema:catalogNumber",
        text="""The catalog number for the release.""",
    )

    CORRECTIONS_POLICY = Semantic(
        id="correctionsPolicy",
        ref="schema:correctionsPolicy",
        text="""For an [[Organization]] (e.g. [[NewsMediaOrganization]]), a statement describing (in news media, the newsroom’s) disclosure and correction policy for errors.""",
    )

    INTERACTION_COUNTER = Semantic(
        id="InteractionCounter",
        ref="schema:InteractionCounter",
        text="""A summary of how users have interacted with this CreativeWork. In most cases, authors will use a subtype to specify the specific type of interaction.""",
    )

    CHILDRENS_EVENT = Semantic(
        id="ChildrensEvent",
        ref="schema:ChildrensEvent",
        text="""Event type: Children\'s event.""",
    )

    PRICE = Semantic(
        id="price",
        ref="schema:price",
        text="""The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.\\n\\nUsage guidelines:\\n\\n* Use the [[priceCurrency]] property (with standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217) e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies e.g. "BTC"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types e.g. "Ithaca HOUR") instead of including [ambiguous symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign) such as \'$\' in the value.\\n* Use \'.\' (Unicode \'FULL STOP\' (U+002E)) rather than \',\' to indicate a decimal point. Avoid using these symbols as a readability separator.\\n* Note that both [RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute) and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values alongside more human-friendly formatting.\\n* Use values from 0123456789 (Unicode \'DIGIT ZERO\' (U+0030) to \'DIGIT NINE\' (U+0039)) rather than superficially similiar Unicode symbols.
      """,
    )

    REVIEW_ACTION = Semantic(
        id="ReviewAction",
        ref="schema:ReviewAction",
        text="""The act of producing a balanced opinion about the object for an audience. An agent reviews an object with participants resulting in a review.""",
    )

    VARIES_BY = Semantic(
        id="variesBy",
        ref="schema:variesBy",
        text="""Indicates the property or properties by which the variants in a [[ProductGroup]] vary, e.g. their size, color etc. Schema.org properties can be referenced by their short name e.g. "color"; terms defined elsewhere can be referenced with their URIs.""",
    )

    RETURN_LABEL_IN_BOX = Semantic(
        id="ReturnLabelInBox",
        ref="schema:ReturnLabelInBox",
        text="""Specifies that a return label will be provided by the seller in the shipping box.""",
    )

    TEMPORAL = Semantic(
        id="temporal",
        ref="schema:temporal",
        text="""The "temporal" property can be used in cases where more specific properties
(e.g. [[temporalCoverage]], [[dateCreated]], [[dateModified]], [[datePublished]]) are not known to be appropriate.""",
    )

    MEASUREMENT_TECHNIQUE = Semantic(
        id="measurementTechnique",
        ref="schema:measurementTechnique",
        text="""A technique or technology used in a [[Dataset]] (or [[DataDownload]], [[DataCatalog]]),
corresponding to the method used for measuring the corresponding variable(s) (described using [[variableMeasured]]). This is oriented towards scientific and scholarly dataset publication but may have broader applicability; it is not intended as a full representation of measurement, but rather as a high level summary for dataset discovery.

For example, if [[variableMeasured]] is: molecule concentration, [[measurementTechnique]] could be: "mass spectrometry" or "nmr spectroscopy" or "colorimetry" or "immunofluorescence".

If the [[variableMeasured]] is "depression rating", the [[measurementTechnique]] could be "Zung Scale" or "HAM-D" or "Beck Depression Inventory".

If there are several [[variableMeasured]] properties recorded for some given data object, use a [[PropertyValue]] for each [[variableMeasured]] and attach the corresponding [[measurementTechnique]].
      """,
    )

    MEDICAL_ENTITY = Semantic(
        id="MedicalEntity",
        ref="schema:MedicalEntity",
        text="""The most generic type of entity related to health and the practice of medicine.""",
    )

    FRONT_WHEEL_DRIVE_CONFIGURATION = Semantic(
        id="FrontWheelDriveConfiguration",
        ref="schema:FrontWheelDriveConfiguration",
        text="""Front-wheel drive is a transmission layout where the engine drives the front wheels.""",
    )

    RATING_VALUE = Semantic(
        id="ratingValue",
        ref="schema:ratingValue",
        text="""The rating for the content.\\n\\nUsage guidelines:\\n\\n* Use values from 0123456789 (Unicode \'DIGIT ZERO\' (U+0030) to \'DIGIT NINE\' (U+0039)) rather than superficially similiar Unicode symbols.\\n* Use \'.\' (Unicode \'FULL STOP\' (U+002E)) rather than \',\' to indicate a decimal point. Avoid using these symbols as a readability separator.""",
    )

    BILLING_START = Semantic(
        id="billingStart",
        ref="schema:billingStart",
        text="""Specifies after how much time this price (or price component) becomes valid and billing starts. Can be used, for example, to model a price increase after the first year of a subscription. The unit of measurement is specified by the unitCode property.""",
    )

    NONPROFIT501C3 = Semantic(
        id="Nonprofit501c3",
        ref="schema:Nonprofit501c3",
        text="""Nonprofit501c3: Non-profit type referring to Religious, Educational, Charitable, Scientific, Literary, Testing for Public Safety, to Foster National or International Amateur Sports Competition, or Prevention of Cruelty to Children or Animals Organizations.""",
    )

    BRAIN_STRUCTURE = Semantic(
        id="BrainStructure",
        ref="schema:BrainStructure",
        text="""Any anatomical structure which pertains to the soft nervous tissue functioning as the coordinating center of sensation and intellectual and nervous activity.""",
    )

    STRENGTH_UNIT = Semantic(
        id="strengthUnit",
        ref="schema:strengthUnit",
        text="""The units of an active ingredient\'s strength, e.g. mg.""",
    )

    MUSIC_VENUE = Semantic(
        id="MusicVenue", ref="schema:MusicVenue", text="""A music venue."""
    )

    SELL_ACTION = Semantic(
        id="SellAction",
        ref="schema:SellAction",
        text="""The act of taking money from a buyer in exchange for goods or services rendered. An agent sells an object, product, or service to a buyer for a price. Reciprocal of BuyAction.""",
    )

    DIGITAL_FORMAT = Semantic(
        id="DigitalFormat", ref="schema:DigitalFormat", text="""DigitalFormat."""
    )

    VISUAL_ARTS_EVENT = Semantic(
        id="VisualArtsEvent",
        ref="schema:VisualArtsEvent",
        text="""Event type: Visual arts event.""",
    )

    VIDEO_FORMAT = Semantic(
        id="videoFormat",
        ref="schema:videoFormat",
        text="""The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).""",
    )

    NUTRITION = Semantic(
        id="nutrition",
        ref="schema:nutrition",
        text="""Nutrition information about the recipe or menu item.""",
    )

    USAGE_INFO = Semantic(
        id="usageInfo",
        ref="schema:usageInfo",
        text="""The schema.org [[usageInfo]] property indicates further information about a [[CreativeWork]]. This property is applicable both to works that are freely available and to those that require payment or other transactions. It can reference additional information e.g. community expectations on preferred linking and citation conventions, as well as purchasing details. For something that can be commercially licensed, usageInfo can provide detailed, resource-specific information about licensing options.

This property can be used alongside the license property which indicates license(s) applicable to some piece of content. The usageInfo property can provide information about other licensing options, e.g. acquiring commercial usage rights for an image that is also available under non-commercial creative commons licenses.""",
    )

    AUDIOBOOK = Semantic(
        id="Audiobook", ref="schema:Audiobook", text="""An audiobook."""
    )

    CHECK_OUT_ACTION = Semantic(
        id="CheckOutAction",
        ref="schema:CheckOutAction",
        text="""The act of an agent communicating (service provider, social media, etc) their departure of a previously reserved service (e.g. flight check in) or place (e.g. hotel).\\n\\nRelated actions:\\n\\n* [[CheckInAction]]: The antonym of CheckOutAction.\\n* [[DepartAction]]: Unlike DepartAction, CheckOutAction implies that the agent is informing/confirming the end of a previously reserved service.\\n* [[CancelAction]]: Unlike CancelAction, CheckOutAction implies that the agent is informing/confirming the end of a previously reserved service.""",
    )

    SUGGESTED_MIN_AGE = Semantic(
        id="suggestedMinAge",
        ref="schema:suggestedMinAge",
        text="""Minimum recommended age in years for the audience or user.""",
    )

    UNIT_PRICE_SPECIFICATION = Semantic(
        id="UnitPriceSpecification",
        ref="schema:UnitPriceSpecification",
        text="""The price asked for a given offer by the respective organization or person.""",
    )

    PRIMARY_PREVENTION = Semantic(
        id="primaryPrevention",
        ref="schema:primaryPrevention",
        text="""A preventative therapy used to prevent an initial occurrence of the medical condition, such as vaccination.""",
    )

    BOAT_TRIP = Semantic(
        id="BoatTrip",
        ref="schema:BoatTrip",
        text="""A trip on a commercial ferry line.""",
    )

    RECIPE_INGREDIENT = Semantic(
        id="recipeIngredient",
        ref="schema:recipeIngredient",
        text="""A single ingredient used in the recipe, e.g. sugar, flour or garlic.""",
    )

    SUBJECT_OF = Semantic(
        id="subjectOf",
        ref="schema:subjectOf",
        text="""A CreativeWork or Event about this Thing.""",
    )

    REPLY_TO_URL = Semantic(
        id="replyToUrl",
        ref="schema:replyToUrl",
        text="""The URL at which a reply may be posted to the specified UserComment.""",
    )

    FIRE_STATION = Semantic(
        id="FireStation",
        ref="schema:FireStation",
        text="""A fire station. With firemen.""",
    )

    NUM_CONSTRAINTS = Semantic(
        id="numConstraints",
        ref="schema:numConstraints",
        text="""Indicates the number of constraints (not counting [[populationType]]) defined for a particular [[StatisticalPopulation]]. This helps applications understand if they have access to a sufficiently complete description of a [[StatisticalPopulation]].""",
    )

    CREATIVE_WORK_STATUS = Semantic(
        id="creativeWorkStatus",
        ref="schema:creativeWorkStatus",
        text="""The status of a creative work in terms of its stage in a lifecycle. Example terms include Incomplete, Draft, Published, Obsolete. Some organizations define a set of terms for the stages of their publication lifecycle.""",
    )

    HEARING_IMPAIRED_SUPPORTED = Semantic(
        id="HearingImpairedSupported",
        ref="schema:HearingImpairedSupported",
        text="""Uses devices to support users with hearing impairments.""",
    )

    OFFER_SHIPPING_DETAILS = Semantic(
        id="OfferShippingDetails",
        ref="schema:OfferShippingDetails",
        text="""OfferShippingDetails represents information about shipping destinations.

Multiple of these entities can be used to represent different shipping rates for different destinations:

One entity for Alaska/Hawaii. A different one for continental US.A different one for all France.

Multiple of these entities can be used to represent different shipping costs and delivery times.

Two entities that are identical but differ in rate and time:

e.g. Cheaper and slower: $5 in 5-7days
or Fast and expensive: $15 in 1-2 days.""",
    )

    MENU_ITEM = Semantic(
        id="MenuItem",
        ref="schema:MenuItem",
        text="""A food or drink item listed in a menu or menu section.""",
    )

    CATALOG = Semantic(
        id="catalog",
        ref="schema:catalog",
        text="""A data catalog which contains this dataset.""",
    )

    QUERY = Semantic(
        id="query",
        ref="schema:query",
        text="""A sub property of instrument. The query used on this action.""",
    )

    CREMATORIUM = Semantic(
        id="Crematorium", ref="schema:Crematorium", text="""A crematorium."""
    )

    BILLING_ADDRESS = Semantic(
        id="billingAddress",
        ref="schema:billingAddress",
        text="""The billing address for the order.""",
    )

    VEHICLE_CONFIGURATION = Semantic(
        id="vehicleConfiguration",
        ref="schema:vehicleConfiguration",
        text="""A short text indicating the configuration of the vehicle, e.g. \'5dr hatchback ST 2.5 MT 225 hp\' or \'limited edition\'.""",
    )

    ASPECT = Semantic(
        id="aspect",
        ref="schema:aspect",
        text="""An aspect of medical practice that is considered on the page, such as \'diagnosis\', \'treatment\', \'causes\', \'prognosis\', \'etiology\', \'epidemiology\', etc.""",
    )

    PROTEIN = Semantic(
        id="Protein",
        ref="schema:Protein",
        text="""Protein is here used in its widest possible definition, as classes of amino acid based molecules. Amyloid-beta Protein in human (UniProt P05067), eukaryota (e.g. an OrthoDB group) or even a single molecule that one can point to are all of type schema:Protein. A protein can thus be a subclass of another protein, e.g. schema:Protein as a UniProt record can have multiple isoforms inside it which would also be schema:Protein. They can be imagined, synthetic, hypothetical or naturally occurring.""",
    )

    WEARABLE_MEASUREMENT_CHEST_OR_BUST = Semantic(
        id="WearableMeasurementChestOrBust",
        ref="schema:WearableMeasurementChestOrBust",
        text="""Measurement of the chest/bust section, for example of a suit""",
    )

    WANT_ACTION = Semantic(
        id="WantAction",
        ref="schema:WantAction",
        text="""The act of expressing a desire about the object. An agent wants an object.""",
    )

    SOFTWARE_HELP = Semantic(
        id="softwareHelp",
        ref="schema:softwareHelp",
        text="""Software application help.""",
    )

    HYPER_TOC = Semantic(
        id="HyperToc",
        ref="schema:HyperToc",
        text="""A HyperToc represents a hypertext table of contents for complex media objects, such as [[VideoObject]], [[AudioObject]]. Items in the table of contents are indicated using the [[tocEntry]] property, and typed [[HyperTocEntry]]. For cases where the same larger work is split into multiple files, [[associatedMedia]] can be used on individual [[HyperTocEntry]] items.""",
    )

    TRACK_ACTION = Semantic(
        id="TrackAction",
        ref="schema:TrackAction",
        text="""An agent tracks an object for updates.\\n\\nRelated actions:\\n\\n* [[FollowAction]]: Unlike FollowAction, TrackAction refers to the interest on the location of innanimates objects.\\n* [[SubscribeAction]]: Unlike SubscribeAction, TrackAction refers to  the interest on the location of innanimate objects.""",
    )

    PAGE_START = Semantic(
        id="pageStart",
        ref="schema:pageStart",
        text="""The page on which the work starts; for example "135" or "xiii".""",
    )

    COMMUNITY_HEALTH = Semantic(
        id="CommunityHealth",
        ref="schema:CommunityHealth",
        text="""A field of public health focusing on improving health characteristics of a defined population in relation with their geographical or environment areas.""",
    )

    SEATING_TYPE = Semantic(
        id="seatingType",
        ref="schema:seatingType",
        text="""The type/class of the seat.""",
    )

    ELIGIBLE_REGION = Semantic(
        id="eligibleRegion",
        ref="schema:eligibleRegion",
        text="""The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.\\n\\nSee also [[ineligibleRegion]].
    """,
    )

    BROADCAST_OF_EVENT = Semantic(
        id="broadcastOfEvent",
        ref="schema:broadcastOfEvent",
        text="""The event being broadcast such as a sporting event or awards ceremony.""",
    )

    PRINT_COLUMN = Semantic(
        id="printColumn",
        ref="schema:printColumn",
        text="""The number of the column in which the NewsArticle appears in the print edition.""",
    )

    MIN_VALUE = Semantic(
        id="minValue",
        ref="schema:minValue",
        text="""The lower value of some characteristic or property.""",
    )

    DRUG_PREGNANCY_CATEGORY = Semantic(
        id="DrugPregnancyCategory",
        ref="schema:DrugPregnancyCategory",
        text="""Categories that represent an assessment of the risk of fetal injury due to a drug or pharmaceutical used as directed by the mother during pregnancy.""",
    )

    OFFICIAL_LEGAL_VALUE = Semantic(
        id="OfficialLegalValue",
        ref="schema:OfficialLegalValue",
        text="""All the documents published by an official publisher should have at least the legal value level "OfficialLegalValue". This indicates that the document was published by an organisation with the public task of making it available (e.g. a consolidated version of a EU directive published by the EU Office of Publications).""",
    )

    INSTALLMENT = Semantic(
        id="Installment",
        ref="schema:Installment",
        text="""Represents the installment pricing component of the total price for an offered product.""",
    )

    WEARABLE_SIZE_GROUP_HUSKY = Semantic(
        id="WearableSizeGroupHusky",
        ref="schema:WearableSizeGroupHusky",
        text="""Size group "Husky" (or "Stocky") for wearables.""",
    )

    MUSIC_PLAYLIST = Semantic(
        id="MusicPlaylist",
        ref="schema:MusicPlaylist",
        text="""A collection of music tracks in playlist form.""",
    )

    REQUIRES_SUBSCRIPTION = Semantic(
        id="requiresSubscription",
        ref="schema:requiresSubscription",
        text="""Indicates if use of the media require a subscription  (either paid or free). Allowed values are ```true``` or ```false``` (note that an earlier version had \'yes\', \'no\').""",
    )

    RUNTIME = Semantic(
        id="runtime",
        ref="schema:runtime",
        text="""Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3, .Net Framework 3.0).""",
    )

    MEDICINE_SYSTEM = Semantic(
        id="MedicineSystem",
        ref="schema:MedicineSystem",
        text="""Systems of medical practice.""",
    )

    EMERGENCY_SERVICE = Semantic(
        id="EmergencyService",
        ref="schema:EmergencyService",
        text="""An emergency service, such as a fire station or ER.""",
    )

    DURATION = Semantic(
        id="Duration",
        ref="schema:Duration",
        text="""Quantity: Duration (use [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601)).""",
    )

    PUBLISHER = Semantic(
        id="publisher",
        ref="schema:publisher",
        text="""The publisher of the creative work.""",
    )

    NONPROFIT_S_B_B_I = Semantic(
        id="NonprofitSBBI",
        ref="schema:NonprofitSBBI",
        text="""NonprofitSBBI: Non-profit type referring to a Social Interest Promoting Institution (NL).""",
    )

    MEMBER_OF = Semantic(
        id="memberOf",
        ref="schema:memberOf",
        text="""An Organization (or ProgramMembership) to which this Person or Organization belongs.""",
    )

    PICKUP_LOCATION = Semantic(
        id="pickupLocation",
        ref="schema:pickupLocation",
        text="""Where a taxi will pick up a passenger or a rental car can be picked up.""",
    )

    BACKGROUND_NEWS_ARTICLE = Semantic(
        id="BackgroundNewsArticle",
        ref="schema:BackgroundNewsArticle",
        text="""A [[NewsArticle]] providing historical context, definition and detail on a specific topic (aka "explainer" or "backgrounder"). For example, an in-depth article or frequently-asked-questions ([FAQ](https://en.wikipedia.org/wiki/FAQ)) document on topics such as Climate Change or the European Union. Other kinds of background material from a non-news setting are often described using [[Book]] or [[Article]], in particular [[ScholarlyArticle]]. See also [[NewsArticle]] for related vocabulary from a learning/education perspective.""",
    )

    EDUCATIONAL_PROGRAM_MODE = Semantic(
        id="educationalProgramMode",
        ref="schema:educationalProgramMode",
        text="""Similar to courseMode, The medium or means of delivery of the program as a whole. The value may either be a text label (e.g. "online", "onsite" or "blended"; "synchronous" or "asynchronous"; "full-time" or "part-time") or a URL reference to a term from a controlled vocabulary (e.g. https://ceds.ed.gov/element/001311#Asynchronous ).""",
    )

    COURSE = Semantic(
        id="Course",
        ref="schema:Course",
        text="""A description of an educational course which may be offered as distinct instances at which take place at different times or take place at different locations, or be offered through different media or modes of study. An educational course is a sequence of one or more educational events and/or creative works which aims to build knowledge, competence or ability of learners.""",
    )

    RESPIRATORY_THERAPY = Semantic(
        id="RespiratoryTherapy",
        ref="schema:RespiratoryTherapy",
        text="""The therapy that is concerned with the maintenance or improvement of respiratory function (as in patients with pulmonary disease).""",
    )

    COMMENT_TIME = Semantic(
        id="commentTime",
        ref="schema:commentTime",
        text="""The time at which the UserComment was made.""",
    )

    DATE_READ = Semantic(
        id="dateRead",
        ref="schema:dateRead",
        text="""The date/time at which the message has been read by the recipient if a single recipient exists.""",
    )

    BAKERY = Semantic(id="Bakery", ref="schema:Bakery", text="""A bakery.""")

    RECIPE_CATEGORY = Semantic(
        id="recipeCategory",
        ref="schema:recipeCategory",
        text="""The category of the recipe—for example, appetizer, entree, etc.""",
    )

    HOW_TO = Semantic(
        id="HowTo",
        ref="schema:HowTo",
        text="""Instructions that explain how to achieve a result by performing a sequence of steps.""",
    )

    HACKATHON = Semantic(
        id="Hackathon",
        ref="schema:Hackathon",
        text="""A [hackathon](https://en.wikipedia.org/wiki/Hackathon) event.""",
    )

    HEALTH_PLAN_ID = Semantic(
        id="healthPlanId",
        ref="schema:healthPlanId",
        text="""The 14-character, HIOS-generated Plan ID number. (Plan IDs must be unique, even across different markets.)""",
    )

    MUSIC_RELEASE_FORMAT_TYPE = Semantic(
        id="MusicReleaseFormatType",
        ref="schema:MusicReleaseFormatType",
        text="""Format of this release (the type of recording media used, ie. compact disc, digital media, LP, etc.).""",
    )

    RETURN_AT_KIOSK = Semantic(
        id="ReturnAtKiosk",
        ref="schema:ReturnAtKiosk",
        text="""Specifies that product returns must be made at a kiosk.""",
    )

    HOW_TO_DIRECTION = Semantic(
        id="HowToDirection",
        ref="schema:HowToDirection",
        text="""A direction indicating a single action to do in the instructions for how to achieve a result.""",
    )

    POSTAL_ADDRESS = Semantic(
        id="PostalAddress", ref="schema:PostalAddress", text="""The mailing address."""
    )

    ITEM_LIST_ORDER_TYPE = Semantic(
        id="ItemListOrderType",
        ref="schema:ItemListOrderType",
        text="""Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized.""",
    )

    PAYLOAD = Semantic(
        id="payload",
        ref="schema:payload",
        text="""The permitted weight of passengers and cargo, EXCLUDING the weight of the empty vehicle.\\n\\nTypical unit code(s): KGM for kilogram, LBR for pound\\n\\n* Note 1: Many databases specify the permitted TOTAL weight instead, which is the sum of [[weight]] and [[payload]]\\n* Note 2: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.\\n* Note 3: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].\\n* Note 4: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.""",
    )

    SURGICAL = Semantic(
        id="Surgical",
        ref="schema:Surgical",
        text="""A specific branch of medical science that pertains to treating diseases, injuries and deformities by manual and instrumental means.""",
    )

    SLOGAN = Semantic(
        id="slogan",
        ref="schema:slogan",
        text="""A slogan or motto associated with the item.""",
    )

    SUB_TRIP = Semantic(
        id="subTrip",
        ref="schema:subTrip",
        text="""Identifies a [[Trip]] that is a subTrip of this Trip.  For example Day 1, Day 2, etc. of a multi-day trip.""",
    )

    ASSOCIATED_CLAIM_REVIEW = Semantic(
        id="associatedClaimReview",
        ref="schema:associatedClaimReview",
        text="""An associated [[ClaimReview]], related by specific common content, topic or claim. The expectation is that this property would be most typically used in cases where a single activity is conducting both claim reviews and media reviews, in which case [[relatedMediaReview]] would commonly be used on a [[ClaimReview]], while [[relatedClaimReview]] would be used on [[MediaReview]].""",
    )

    RELEASED_EVENT = Semantic(
        id="releasedEvent",
        ref="schema:releasedEvent",
        text="""The place and time the release was issued, expressed as a PublicationEvent.""",
    )

    MALE = Semantic(id="Male", ref="schema:Male", text="""The male gender.""")

    USER_BLOCKS = Semantic(
        id="UserBlocks",
        ref="schema:UserBlocks",
        text="""UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].""",
    )

    AUTHORIZE_ACTION = Semantic(
        id="AuthorizeAction",
        ref="schema:AuthorizeAction",
        text="""The act of granting permission to an object.""",
    )

    PAYMENT_METHOD = Semantic(
        id="PaymentMethod",
        ref="schema:PaymentMethod",
        text="""A payment method is a standardized procedure for transferring the monetary amount for a purchase. Payment methods are characterized by the legal and technical structures used, and by the organization or group carrying out the transaction.\\n\\nCommonly used values:\\n\\n* http://purl.org/goodrelations/v1#ByBankTransferInAdvance\\n* http://purl.org/goodrelations/v1#ByInvoice\\n* http://purl.org/goodrelations/v1#Cash\\n* http://purl.org/goodrelations/v1#CheckInAdvance\\n* http://purl.org/goodrelations/v1#COD\\n* http://purl.org/goodrelations/v1#DirectDebit\\n* http://purl.org/goodrelations/v1#GoogleCheckout\\n* http://purl.org/goodrelations/v1#PayPal\\n* http://purl.org/goodrelations/v1#PaySwarm
        """,
    )

    ANSWER_EXPLANATION = Semantic(
        id="answerExplanation",
        ref="schema:answerExplanation",
        text="""A step-by-step or full explanation about Answer. Can outline how this Answer was achieved or contain more broad clarification or statement about it. """,
    )

    USED_CONDITION = Semantic(
        id="UsedCondition",
        ref="schema:UsedCondition",
        text="""Indicates that the item is used.""",
    )

    USER_PLUS_ONES = Semantic(
        id="UserPlusOnes",
        ref="schema:UserPlusOnes",
        text="""UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].""",
    )

    DOWNVOTE_COUNT = Semantic(
        id="downvoteCount",
        ref="schema:downvoteCount",
        text="""The number of downvotes this question, answer or comment has received from the community.""",
    )

    CONTAINED_IN_PLACE = Semantic(
        id="containedInPlace",
        ref="schema:containedInPlace",
        text="""The basic containment relation between a place and one that contains it.""",
    )

    CUSTOMER = Semantic(
        id="customer",
        ref="schema:customer",
        text="""Party placing the order or paying the invoice.""",
    )

    INCLUDED_RISK_FACTOR = Semantic(
        id="includedRiskFactor",
        ref="schema:includedRiskFactor",
        text="""A modifiable or non-modifiable risk factor included in the calculation, e.g. age, coexisting condition.""",
    )

    UPLOAD_DATE = Semantic(
        id="uploadDate",
        ref="schema:uploadDate",
        text="""Date when this media object was uploaded to this site.""",
    )

    SEASONS = Semantic(
        id="seasons", ref="schema:seasons", text="""A season in a media series."""
    )

    RANDOMIZED_TRIAL = Semantic(
        id="RandomizedTrial",
        ref="schema:RandomizedTrial",
        text="""A randomized trial design.""",
    )

    SUPPLY_TO = Semantic(
        id="supplyTo",
        ref="schema:supplyTo",
        text="""The area to which the artery supplies blood.""",
    )

    PROGRAM_TYPE = Semantic(
        id="programType",
        ref="schema:programType",
        text="""The type of educational or occupational program. For example, classroom, internship, alternance, etc..""",
    )

    W_P_HEADER = Semantic(
        id="WPHeader", ref="schema:WPHeader", text="""The header section of the page."""
    )

    FUEL_TYPE = Semantic(
        id="fuelType",
        ref="schema:fuelType",
        text="""The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only one engine, this property can be attached directly to the vehicle.""",
    )

    IS_SIMILAR_TO = Semantic(
        id="isSimilarTo",
        ref="schema:isSimilarTo",
        text="""A pointer to another, functionally similar product (or multiple products).""",
    )

    ARRIVAL_PLATFORM = Semantic(
        id="arrivalPlatform",
        ref="schema:arrivalPlatform",
        text="""The platform where the train arrives.""",
    )

    USER_INTERACTION = Semantic(
        id="UserInteraction",
        ref="schema:UserInteraction",
        text="""UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].""",
    )

    CREATIVE_WORK = Semantic(
        id="CreativeWork",
        ref="schema:CreativeWork",
        text="""The most generic kind of creative work, including books, movies, photographs, software programs, etc.""",
    )

    QUOTATION = Semantic(
        id="Quotation",
        ref="schema:Quotation",
        text="""A quotation. Often but not necessarily from some written work, attributable to a real world author and - if associated with a fictional character - to any fictional Person. Use [[isBasedOn]] to link to source/origin. The [[recordedIn]] property can be used to reference a Quotation from an [[Event]].""",
    )

    TRADITIONAL_CHINESE = Semantic(
        id="TraditionalChinese",
        ref="schema:TraditionalChinese",
        text="""A system of medicine based on common theoretical concepts that originated in China and evolved over thousands of years, that uses herbs, acupuncture, exercise, massage, dietary therapy, and other methods to treat a wide range of conditions.""",
    )

    MUSIC_VIDEO_OBJECT = Semantic(
        id="MusicVideoObject",
        ref="schema:MusicVideoObject",
        text="""A music video file.""",
    )

    PLASTIC_SURGERY = Semantic(
        id="PlasticSurgery",
        ref="schema:PlasticSurgery",
        text="""A specific branch of medical science that pertains to therapeutic or cosmetic repair or re-formation of missing, injured or malformed tissues or body parts by manual and instrumental means.""",
    )

    ALTERNATIVE_HEADLINE = Semantic(
        id="alternativeHeadline",
        ref="schema:alternativeHeadline",
        text="""A secondary title of the CreativeWork.""",
    )

    STAR_RATING = Semantic(
        id="starRating",
        ref="schema:starRating",
        text="""An official rating for a lodging business or food establishment, e.g. from national associations or standards bodies. Use the author property to indicate the rating organization, e.g. as an Organization with name such as (e.g. HOTREC, DEHOGA, WHR, or Hotelstars).""",
    )

    EVENT_SERIES = Semantic(
        id="EventSeries",
        ref="schema:EventSeries",
        text="""A series of [[Event]]s. Included events can relate with the series using the [[superEvent]] property.

An EventSeries is a collection of events that share some unifying characteristic. For example, "The Olympic Games" is a series, which
is repeated regularly. The "2012 London Olympics" can be presented both as an [[Event]] in the series "Olympic Games", and as an
[[EventSeries]] that included a number of sporting competitions as Events.

The nature of the association between the events in an [[EventSeries]] can vary, but typical examples could
include a thematic event series (e.g. topical meetups or classes), or a series of regular events that share a location, attendee group and/or organizers.

EventSeries has been defined as a kind of Event to make it easy for publishers to use it in an Event context without
worrying about which kinds of series are really event-like enough to call an Event. In general an EventSeries
may seem more Event-like when the period of time is compact and when aspects such as location are fixed, but
it may also sometimes prove useful to describe a longer-term series as an Event.
   """,
    )

    THURSDAY = Semantic(
        id="Thursday",
        ref="schema:Thursday",
        text="""The day of the week between Wednesday and Friday.""",
    )

    LEGAL_FORCE_STATUS = Semantic(
        id="LegalForceStatus",
        ref="schema:LegalForceStatus",
        text="""A list of possible statuses for the legal force of a legislation.""",
    )

    PROFICIENCY_LEVEL = Semantic(
        id="proficiencyLevel",
        ref="schema:proficiencyLevel",
        text="""Proficiency needed for this content; expected values: \'Beginner\', \'Expert\'.""",
    )

    MEDICAL_RISK_FACTOR = Semantic(
        id="MedicalRiskFactor",
        ref="schema:MedicalRiskFactor",
        text="""A risk factor is anything that increases a person\'s likelihood of developing or contracting a disease, medical condition, or complication.""",
    )

    FLIGHT = Semantic(id="Flight", ref="schema:Flight", text="""An airline flight.""")

    BANK_ACCOUNT_TYPE = Semantic(
        id="bankAccountType",
        ref="schema:bankAccountType",
        text="""The type of a bank account.""",
    )

    TOTAL_JOB_OPENINGS = Semantic(
        id="totalJobOpenings",
        ref="schema:totalJobOpenings",
        text="""The number of positions open for this job posting. Use a positive integer. Do not use if the number of positions is unclear or not known.""",
    )

    APPLICATION_DEADLINE = Semantic(
        id="applicationDeadline",
        ref="schema:applicationDeadline",
        text="""The date at which the program stops collecting applications for the next enrollment cycle.""",
    )

    SELLER = Semantic(
        id="seller",
        ref="schema:seller",
        text="""An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.""",
    )

    CONTACT_POINT_OPTION = Semantic(
        id="ContactPointOption",
        ref="schema:ContactPointOption",
        text="""Enumerated options related to a ContactPoint.""",
    )

    EXECUTABLE_LIBRARY_NAME = Semantic(
        id="executableLibraryName",
        ref="schema:executableLibraryName",
        text="""Library file name e.g., mscorlib.dll, system.web.dll.""",
    )

    MOVIE = Semantic(id="Movie", ref="schema:Movie", text="""A movie.""")

    UPVOTE_COUNT = Semantic(
        id="upvoteCount",
        ref="schema:upvoteCount",
        text="""The number of upvotes this question, answer or comment has received from the community.""",
    )

    DEPARTMENT = Semantic(
        id="department",
        ref="schema:department",
        text="""A relationship between an organization and a department of that organization, also described as an organization (allowing different urls, logos, opening hours). For example: a store with a pharmacy, or a bakery with a cafe.""",
    )

    OCCUPATION_LOCATION = Semantic(
        id="occupationLocation",
        ref="schema:occupationLocation",
        text=""" The region/country for which this occupational description is appropriate. Note that educational requirements and qualifications can vary between jurisdictions.""",
    )

    NEWSPAPER = Semantic(
        id="Newspaper",
        ref="schema:Newspaper",
        text="""A publication containing information about varied topics that are pertinent to general information, a geographic area, or a specific subject matter (i.e. business, culture, education). Often published daily.""",
    )

    OBSTETRIC = Semantic(
        id="Obstetric",
        ref="schema:Obstetric",
        text="""A specific branch of medical science that specializes in the care of women during the prenatal and postnatal care and with the delivery of the child.""",
    )

    FOOD_EVENT = Semantic(
        id="FoodEvent", ref="schema:FoodEvent", text="""Event type: Food event."""
    )

    MOVIE_RENTAL_STORE = Semantic(
        id="MovieRentalStore",
        ref="schema:MovieRentalStore",
        text="""A movie rental store.""",
    )

    BANK_ACCOUNT = Semantic(
        id="BankAccount",
        ref="schema:BankAccount",
        text="""A product or service offered by a bank whereby one may deposit, withdraw or transfer money and in some cases be paid interest.""",
    )

    WEARABLE_SIZE_GROUP_EXTRA_TALL = Semantic(
        id="WearableSizeGroupExtraTall",
        ref="schema:WearableSizeGroupExtraTall",
        text="""Size group "Extra Tall" for wearables.""",
    )

    LEARNING_RESOURCE = Semantic(
        id="LearningResource",
        ref="schema:LearningResource",
        text="""The LearningResource type can be used to indicate [[CreativeWork]]s (whether physical or digital) that have a particular and explicit orientation towards learning, education, skill acquisition, and other educational purposes.

[[LearningResource]] is expected to be used as an addition to a primary type such as [[Book]], [[VideoObject]], [[Product]] etc.

[[EducationEvent]] serves a similar purpose for event-like things (e.g. a [[Trip]]). A [[LearningResource]] may be created as a result of an [[EducationEvent]], for example by recording one.""",
    )

    BODY_MEASUREMENT_HEIGHT = Semantic(
        id="BodyMeasurementHeight",
        ref="schema:BodyMeasurementHeight",
        text="""Body height (measured between crown of head and soles of feet). Used, for example, to fit jackets.""",
    )

    LEAVE_ACTION = Semantic(
        id="LeaveAction",
        ref="schema:LeaveAction",
        text="""An agent leaves an event / group with participants/friends at a location.\\n\\nRelated actions:\\n\\n* [[JoinAction]]: The antonym of LeaveAction.\\n* [[UnRegisterAction]]: Unlike UnRegisterAction, LeaveAction implies leaving a group/team of people rather than a service.""",
    )

    INTENSITY = Semantic(
        id="intensity",
        ref="schema:intensity",
        text="""Quantitative measure gauging the degree of force involved in the exercise, for example, heartbeats per minute. May include the velocity of the movement.""",
    )

    MUSIC_COMPOSITION = Semantic(
        id="MusicComposition",
        ref="schema:MusicComposition",
        text="""A musical composition.""",
    )

    ACTION_OPTION = Semantic(
        id="actionOption",
        ref="schema:actionOption",
        text="""A sub property of object. The options subject to this action.""",
    )

    STRENGTH_VALUE = Semantic(
        id="strengthValue",
        ref="schema:strengthValue",
        text="""The value of an active ingredient\'s strength, e.g. 325.""",
    )

    COMPLETED_ACTION_STATUS = Semantic(
        id="CompletedActionStatus",
        ref="schema:CompletedActionStatus",
        text="""An action that has already taken place.""",
    )

    GIVEN_NAME = Semantic(
        id="givenName",
        ref="schema:givenName",
        text="""Given name. In the U.S., the first name of a Person.""",
    )

    SOFTWARE_VERSION = Semantic(
        id="softwareVersion",
        ref="schema:softwareVersion",
        text="""Version of the software instance.""",
    )

    VEHICLE_INTERIOR_TYPE = Semantic(
        id="vehicleInteriorType",
        ref="schema:vehicleInteriorType",
        text="""The type or material of the interior of the vehicle (e.g. synthetic fabric, leather, wood, etc.). While most interior types are characterized by the material used, an interior type can also be based on vehicle usage or target audience.""",
    )

    PERMISSIONS = Semantic(
        id="permissions",
        ref="schema:permissions",
        text="""Permission(s) required to run the app (for example, a mobile app may require full internet access or may run only on wifi).""",
    )

    TRACK = Semantic(
        id="track",
        ref="schema:track",
        text="""A music recording (track)&#x2014;usually a single song. If an ItemList is given, the list should contain items of type MusicRecording.""",
    )

    NERVE_MOTOR = Semantic(
        id="nerveMotor",
        ref="schema:nerveMotor",
        text="""The neurological pathway extension that involves muscle control.""",
    )

    DIAGNOSTIC_LAB = Semantic(
        id="DiagnosticLab",
        ref="schema:DiagnosticLab",
        text="""A medical laboratory that offers on-site or off-site diagnostic services.""",
    )

    UPDATE_ACTION = Semantic(
        id="UpdateAction",
        ref="schema:UpdateAction",
        text="""The act of managing by changing/editing the state of the object.""",
    )

    F_A_Q_PAGE = Semantic(
        id="FAQPage",
        ref="schema:FAQPage",
        text="""A [[FAQPage]] is a [[WebPage]] presenting one or more "[Frequently asked questions](https://en.wikipedia.org/wiki/FAQ)" (see also [[QAPage]]).""",
    )

    SALE_EVENT = Semantic(
        id="SaleEvent", ref="schema:SaleEvent", text="""Event type: Sales event."""
    )

    MEDICAL_DEVICE_PURPOSE = Semantic(
        id="MedicalDevicePurpose",
        ref="schema:MedicalDevicePurpose",
        text="""Categories of medical devices, organized by the purpose or intended use of the device.""",
    )

    SERVICE_TYPE = Semantic(
        id="serviceType",
        ref="schema:serviceType",
        text="""The type of service being offered, e.g. veterans\' benefits, emergency relief, etc.""",
    )

    AREA = Semantic(
        id="area",
        ref="schema:area",
        text="""The area within which users can expect to reach the broadcast service.""",
    )

    SD_LICENSE = Semantic(
        id="sdLicense",
        ref="schema:sdLicense",
        text="""A license document that applies to this structured data, typically indicated by URL.""",
    )

    JOINT = Semantic(
        id="Joint",
        ref="schema:Joint",
        text="""The anatomical location at which two or more bones make contact.""",
    )

    FILE_SIZE = Semantic(
        id="fileSize",
        ref="schema:fileSize",
        text="""Size of the application / package (e.g. 18MB). In the absence of a unit (MB, KB etc.), KB will be assumed.""",
    )

    DELIVERY_ADDRESS = Semantic(
        id="deliveryAddress",
        ref="schema:deliveryAddress",
        text="""Destination address.""",
    )

    GARDEN_STORE = Semantic(
        id="GardenStore", ref="schema:GardenStore", text="""A garden store."""
    )

    PRONOUNCEABLE_TEXT = Semantic(
        id="PronounceableText",
        ref="schema:PronounceableText",
        text="""Data type: PronounceableText.""",
    )

    LOAN_PAYMENT_FREQUENCY = Semantic(
        id="loanPaymentFrequency",
        ref="schema:loanPaymentFrequency",
        text="""Frequency of payments due, i.e. number of months between payments. This is defined as a frequency, i.e. the reciprocal of a period of time.""",
    )

    PET_STORE = Semantic(id="PetStore", ref="schema:PetStore", text="""A pet store.""")

    UNSATURATED_FAT_CONTENT = Semantic(
        id="unsaturatedFatContent",
        ref="schema:unsaturatedFatContent",
        text="""The number of grams of unsaturated fat.""",
    )

    EDUCATIONAL_CREDENTIAL_AWARDED = Semantic(
        id="educationalCredentialAwarded",
        ref="schema:educationalCredentialAwarded",
        text="""A description of the qualification, award, certificate, diploma or other educational credential awarded as a consequence of successful completion of this course or program.""",
    )

    HAS_DIGITAL_DOCUMENT_PERMISSION = Semantic(
        id="hasDigitalDocumentPermission",
        ref="schema:hasDigitalDocumentPermission",
        text="""A permission related to the access to this document (e.g. permission to read or write an electronic document). For a public document, specify a grantee with an Audience with audienceType equal to "public".""",
    )

    BEAUTY_SALON = Semantic(
        id="BeautySalon", ref="schema:BeautySalon", text="""Beauty salon."""
    )

    SEE_DOCTOR_HEALTH_ASPECT = Semantic(
        id="SeeDoctorHealthAspect",
        ref="schema:SeeDoctorHealthAspect",
        text="""Information about questions that may be asked, when to see a professional, measures before seeing a doctor or content about the first consultation.""",
    )

    HEIGHT = Semantic(
        id="height", ref="schema:height", text="""The height of the item."""
    )

    LEGISLATION_TRANSPOSES = Semantic(
        id="legislationTransposes",
        ref="schema:legislationTransposes",
        text="""Indicates that this legislation (or part of legislation) fulfills the objectives set by another legislation, by passing appropriate implementation measures. Typically, some legislations of European Union\'s member states or regions transpose European Directives. This indicates a legally binding link between the 2 legislations.""",
    )

    BED = Semantic(
        id="bed",
        ref="schema:bed",
        text="""The type of bed or beds included in the accommodation. For the single case of just one bed of a certain type, you use bed directly with a text.
      If you want to indicate the quantity of a certain kind of bed, use an instance of BedDetails. For more detailed information, use the amenityFeature property.""",
    )

    NONPROFIT_A_N_B_I = Semantic(
        id="NonprofitANBI",
        ref="schema:NonprofitANBI",
        text="""NonprofitANBI: Non-profit type referring to a Public Benefit Organization (NL).""",
    )

    DRUG_LEGAL_STATUS = Semantic(
        id="DrugLegalStatus",
        ref="schema:DrugLegalStatus",
        text="""The legal availability status of a medical drug.""",
    )

    RELEASE_NOTES = Semantic(
        id="releaseNotes",
        ref="schema:releaseNotes",
        text="""Description of what changed in this version.""",
    )

    PREP_TIME = Semantic(
        id="prepTime",
        ref="schema:prepTime",
        text="""The length of time it takes to prepare the items to be used in instructions or a direction, in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).""",
    )

    SEARCH_ACTION = Semantic(
        id="SearchAction",
        ref="schema:SearchAction",
        text="""The act of searching for an object.\\n\\nRelated actions:\\n\\n* [[FindAction]]: SearchAction generally leads to a FindAction, but not necessarily.""",
    )

    NONPROFIT527 = Semantic(
        id="Nonprofit527",
        ref="schema:Nonprofit527",
        text="""Nonprofit527: Non-profit type referring to Political organizations.""",
    )

    MEDIA_AUTHENTICITY_CATEGORY = Semantic(
        id="mediaAuthenticityCategory",
        ref="schema:mediaAuthenticityCategory",
        text="""Indicates a MediaManipulationRatingEnumeration classification of a media object (in the context of how it was published or shared).""",
    )

    VALUE_NAME = Semantic(
        id="valueName",
        ref="schema:valueName",
        text="""Indicates the name of the PropertyValueSpecification to be used in URL templates and form encoding in a manner analogous to HTML\'s input@name.""",
    )

    DEFINITIVE_LEGAL_VALUE = Semantic(
        id="DefinitiveLegalValue",
        ref="schema:DefinitiveLegalValue",
        text="""Indicates a document for which the text is conclusively what the law says and is legally binding. (e.g. The digitally signed version of an Official Journal.)
  Something "Definitive" is considered to be also [[AuthoritativeLegalValue]].""",
    )

    SUPERFICIAL_ANATOMY = Semantic(
        id="SuperficialAnatomy",
        ref="schema:SuperficialAnatomy",
        text="""Anatomical features that can be observed by sight (without dissection), including the form and proportions of the human body as well as surface landmarks that correspond to deeper subcutaneous structures. Superficial anatomy plays an important role in sports medicine, phlebotomy, and other medical specialties as underlying anatomical structures can be identified through surface palpation. For example, during back surgery, superficial anatomy can be used to palpate and count vertebrae to find the site of incision. Or in phlebotomy, superficial anatomy can be used to locate an underlying vein; for example, the median cubital vein can be located by palpating the borders of the cubital fossa (such as the epicondyles of the humerus) and then looking for the superficial signs of the vein, such as size, prominence, ability to refill after depression, and feel of surrounding tissue support. As another example, in a subluxation (dislocation) of the glenohumeral joint, the bony structure becomes pronounced with the deltoid muscle failing to cover the glenohumeral joint allowing the edges of the scapula to be superficially visible. Here, the superficial anatomy is the visible edges of the scapula, implying the underlying dislocation of the joint (the related anatomical structure).""",
    )

    SUITABLE_FOR_DIET = Semantic(
        id="suitableForDiet",
        ref="schema:suitableForDiet",
        text="""Indicates a dietary restriction or guideline for which this recipe or menu item is suitable, e.g. diabetic, halal etc.""",
    )

    SOLVE_MATH_ACTION = Semantic(
        id="SolveMathAction",
        ref="schema:SolveMathAction",
        text="""The action that takes in a math expression and directs users to a page potentially capable of solving/simplifying that expression.""",
    )

    ACCOUNTABLE_PERSON = Semantic(
        id="accountablePerson",
        ref="schema:accountablePerson",
        text="""Specifies the Person that is legally accountable for the CreativeWork.""",
    )

    BACTERIA = Semantic(
        id="Bacteria",
        ref="schema:Bacteria",
        text="""Pathogenic bacteria that cause bacterial infection.""",
    )

    HEMATOLOGIC = Semantic(
        id="Hematologic",
        ref="schema:Hematologic",
        text="""A specific branch of medical science that pertains to diagnosis and treatment of disorders of blood and blood producing organs.""",
    )

    STEP = Semantic(
        id="step",
        ref="schema:step",
        text="""A single step item (as HowToStep, text, document, video, etc.) or a HowToSection.""",
    )

    TAXON = Semantic(
        id="Taxon",
        ref="schema:Taxon",
        text="""A set of organisms asserted to represent a natural cohesive biological unit.""",
    )

    SALARY_CURRENCY = Semantic(
        id="salaryCurrency",
        ref="schema:salaryCurrency",
        text="""The currency (coded using [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217) ) used for the main salary information in this job posting or for this employee.""",
    )

    SPOKEN_WORD_ALBUM = Semantic(
        id="SpokenWordAlbum", ref="schema:SpokenWordAlbum", text="""SpokenWordAlbum."""
    )

    COLLECTION = Semantic(
        id="collection",
        ref="schema:collection",
        text="""A sub property of object. The collection target of the action.""",
    )

    GETTING_ACCESS_HEALTH_ASPECT = Semantic(
        id="GettingAccessHealthAspect",
        ref="schema:GettingAccessHealthAspect",
        text="""Content that discusses practical and policy aspects for getting access to specific kinds of healthcare (e.g. distribution mechanisms for vaccines).""",
    )

    ITEM_LOCATION = Semantic(
        id="itemLocation",
        ref="schema:itemLocation",
        text="""Current location of the item.""",
    )

    CREDIT_CARD = Semantic(
        id="CreditCard",
        ref="schema:CreditCard",
        text="""A card payment method of a particular brand or name.  Used to mark up a particular payment method and/or the financial product/service that supplies the card account.\\n\\nCommonly used values:\\n\\n* http://purl.org/goodrelations/v1#AmericanExpress\\n* http://purl.org/goodrelations/v1#DinersClub\\n* http://purl.org/goodrelations/v1#Discover\\n* http://purl.org/goodrelations/v1#JCB\\n* http://purl.org/goodrelations/v1#MasterCard\\n* http://purl.org/goodrelations/v1#VISA
       """,
    )

    RESPONSIBILITIES = Semantic(
        id="responsibilities",
        ref="schema:responsibilities",
        text="""Responsibilities associated with this role or Occupation.""",
    )

    BUDDHIST_TEMPLE = Semantic(
        id="BuddhistTemple", ref="schema:BuddhistTemple", text="""A Buddhist temple."""
    )

    END_TIME = Semantic(
        id="endTime",
        ref="schema:endTime",
        text="""The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to *December*. For media, including audio and video, it\'s the time offset of the end of a clip within a larger file.\\n\\nNote that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.""",
    )

    WEARABLE_MEASUREMENT_HEIGHT = Semantic(
        id="WearableMeasurementHeight",
        ref="schema:WearableMeasurementHeight",
        text="""Measurement of the height, for example the heel height of a shoe""",
    )

    DEFINED_TERM = Semantic(
        id="DefinedTerm",
        ref="schema:DefinedTerm",
        text="""A word, name, acronym, phrase, etc. with a formal definition. Often used in the context of category or subject classification, glossaries or dictionaries, product or creative work types, etc. Use the name property for the term being defined, use termCode if the term has an alpha-numeric code allocated, use description to provide the definition of the term.""",
    )

    MUSICAL_KEY = Semantic(
        id="musicalKey",
        ref="schema:musicalKey",
        text="""The key, mode, or scale this composition uses.""",
    )

    EDUCATIONAL_ORGANIZATION = Semantic(
        id="EducationalOrganization",
        ref="schema:EducationalOrganization",
        text="""An educational organization.""",
    )

    VOLUME_NUMBER = Semantic(
        id="volumeNumber",
        ref="schema:volumeNumber",
        text="""Identifies the volume of publication or multi-part work; for example, "iii" or "2".""",
    )

    DAMAGED_CONDITION = Semantic(
        id="DamagedCondition",
        ref="schema:DamagedCondition",
        text="""Indicates that the item is damaged.""",
    )

    ARRIVAL_TIME = Semantic(
        id="arrivalTime",
        ref="schema:arrivalTime",
        text="""The expected arrival time.""",
    )

    PERFORMING_GROUP = Semantic(
        id="PerformingGroup",
        ref="schema:PerformingGroup",
        text="""A performance group, such as a band, an orchestra, or a circus.""",
    )

    GAME = Semantic(
        id="Game",
        ref="schema:Game",
        text="""The Game type represents things which are games. These are typically rule-governed recreational activities, e.g. role-playing games in which players assume the role of characters in a fictional setting.""",
    )

    DATE_SENT = Semantic(
        id="dateSent",
        ref="schema:dateSent",
        text="""The date/time at which the message was sent.""",
    )

    ASSESS_ACTION = Semantic(
        id="AssessAction",
        ref="schema:AssessAction",
        text="""The act of forming one\'s opinion, reaction or sentiment.""",
    )

    SATURATED_FAT_CONTENT = Semantic(
        id="saturatedFatContent",
        ref="schema:saturatedFatContent",
        text="""The number of grams of saturated fat.""",
    )

    SCHOOL_CLOSURES_INFO = Semantic(
        id="schoolClosuresInfo",
        ref="schema:schoolClosuresInfo",
        text="""Information about school closures.""",
    )

    ALGORITHM = Semantic(
        id="algorithm",
        ref="schema:algorithm",
        text="""The algorithm or rules to follow to compute the score.""",
    )

    PAYMENT_STATUS_TYPE = Semantic(
        id="PaymentStatusType",
        ref="schema:PaymentStatusType",
        text="""A specific payment status. For example, PaymentDue, PaymentComplete, etc.""",
    )

    DIAGNOSTIC_PROCEDURE = Semantic(
        id="DiagnosticProcedure",
        ref="schema:DiagnosticProcedure",
        text="""A medical procedure intended primarily for diagnostic, as opposed to therapeutic, purposes.""",
    )

    RETURN_FEES_ENUMERATION = Semantic(
        id="ReturnFeesEnumeration",
        ref="schema:ReturnFeesEnumeration",
        text="""Enumerates several kinds of policies for product return fees.""",
    )

    CAR = Semantic(
        id="Car",
        ref="schema:Car",
        text="""A car is a wheeled, self-powered motor vehicle used for transportation.""",
    )

    COPYRIGHT_NOTICE = Semantic(
        id="copyrightNotice",
        ref="schema:copyrightNotice",
        text="""Text of a notice appropriate for describing the copyright aspects of this Creative Work, ideally indicating the owner of the copyright for the Work.""",
    )

    BRANCH_CODE = Semantic(
        id="branchCode",
        ref="schema:branchCode",
        text="""A short textual code (also called "store code") that uniquely identifies a place of business. The code is typically assigned by the parentOrganization and used in structured URLs.\\n\\nFor example, in the URL http://www.starbucks.co.uk/store-locator/etc/detail/3047 the code "3047" is a branchCode for a particular branch.
      """,
    )

    PATHOLOGY = Semantic(
        id="Pathology",
        ref="schema:Pathology",
        text="""A specific branch of medical science that is concerned with the study of the cause, origin and nature of a disease state, including its consequences as a result of manifestation of the disease. In clinical care, the term is used to designate a branch of medicine using laboratory tests to diagnose and determine the prognostic significance of illness.""",
    )

    NONPROFIT501C23 = Semantic(
        id="Nonprofit501c23",
        ref="schema:Nonprofit501c23",
        text="""Nonprofit501c23: Non-profit type referring to Veterans Organizations.""",
    )

    SCULPTURE = Semantic(
        id="Sculpture", ref="schema:Sculpture", text="""A piece of sculpture."""
    )

    SEASON = Semantic(
        id="season", ref="schema:season", text="""A season in a media series."""
    )

    PERCENTILE25 = Semantic(
        id="percentile25",
        ref="schema:percentile25",
        text="""The 25th percentile value.""",
    )

    BALANCE = Semantic(
        id="Balance",
        ref="schema:Balance",
        text="""Physical activity that is engaged to help maintain posture and balance.""",
    )

    VIDEO_GAME_CLIP = Semantic(
        id="VideoGameClip",
        ref="schema:VideoGameClip",
        text="""A short segment/part of a video game.""",
    )

    DELIVERY_CHARGE_SPECIFICATION = Semantic(
        id="DeliveryChargeSpecification",
        ref="schema:DeliveryChargeSpecification",
        text="""The price for the delivery of an offer using a particular delivery method.""",
    )

    VAT_I_D = Semantic(
        id="vatID",
        ref="schema:vatID",
        text="""The Value-added Tax ID of the organization or person.""",
    )

    FOOD_ESTABLISHMENT_RESERVATION = Semantic(
        id="FoodEstablishmentReservation",
        ref="schema:FoodEstablishmentReservation",
        text="""A reservation to dine at a food-related business.\\n\\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.""",
    )

    RADIO_CHANNEL = Semantic(
        id="RadioChannel",
        ref="schema:RadioChannel",
        text="""A unique instance of a radio BroadcastService on a CableOrSatelliteService lineup.""",
    )

    CAUSE_OF = Semantic(
        id="causeOf",
        ref="schema:causeOf",
        text="""The condition, complication, symptom, sign, etc. caused.""",
    )

    CONSUME_ACTION = Semantic(
        id="ConsumeAction",
        ref="schema:ConsumeAction",
        text="""The act of ingesting information/resources/food.""",
    )

    COMPLETE_DATA_FEED = Semantic(
        id="CompleteDataFeed",
        ref="schema:CompleteDataFeed",
        text="""A [[CompleteDataFeed]] is a [[DataFeed]] whose standard representation includes content for every item currently in the feed.

This is the equivalent of Atom\'s element as defined in Feed Paging and Archiving [RFC 5005](https://tools.ietf.org/html/rfc5005), For example (and as defined for Atom), when using data from a feed that represents a collection of items that varies over time (e.g. "Top Twenty Records") there is no need to have newer entries mixed in alongside older, obsolete entries. By marking this feed as a CompleteDataFeed, old entries can be safely discarded when the feed is refreshed, since we can assume the feed has provided descriptions for all current items.""",
    )

    DISCUSSION_FORUM_POSTING = Semantic(
        id="DiscussionForumPosting",
        ref="schema:DiscussionForumPosting",
        text="""A posting to a discussion forum.""",
    )

    PROGNOSIS_HEALTH_ASPECT = Semantic(
        id="PrognosisHealthAspect",
        ref="schema:PrognosisHealthAspect",
        text="""Typical progression and happenings of life course of the topic.""",
    )

    REPRESENTATIVE_OF_PAGE = Semantic(
        id="representativeOfPage",
        ref="schema:representativeOfPage",
        text="""Indicates whether this image is representative of the content of the page.""",
    )

    RATING_EXPLANATION = Semantic(
        id="ratingExplanation",
        ref="schema:ratingExplanation",
        text="""A short explanation (e.g. one to two sentences) providing background context and other information that led to the conclusion expressed in the rating. This is particularly applicable to ratings associated with "fact check" markup using [[ClaimReview]].""",
    )

    RECOURSE_LOAN = Semantic(
        id="recourseLoan",
        ref="schema:recourseLoan",
        text="""The only way you get the money back in the event of default is the security. Recourse is where you still have the opportunity to go back to the borrower for the rest of the money.""",
    )

    DOSE_SCHEDULE = Semantic(
        id="doseSchedule",
        ref="schema:doseSchedule",
        text="""A dosing schedule for the drug for a given population, either observed, recommended, or maximum dose based on the type used.""",
    )

    MEDICAL_PROCEDURE_TYPE = Semantic(
        id="MedicalProcedureType",
        ref="schema:MedicalProcedureType",
        text="""An enumeration that describes different types of medical procedures.""",
    )

    TOTAL_TIME = Semantic(
        id="totalTime",
        ref="schema:totalTime",
        text="""The total time required to perform instructions or a direction (including time to prepare the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).""",
    )

    ASSOCIATED_DISEASE = Semantic(
        id="associatedDisease",
        ref="schema:associatedDisease",
        text="""Disease associated to this BioChemEntity. Such disease can be a MedicalCondition or a URL. If you want to add an evidence supporting the association, please use PropertyValue.""",
    )

    RELEVANT_SPECIALTY = Semantic(
        id="relevantSpecialty",
        ref="schema:relevantSpecialty",
        text="""If applicable, a medical specialty in which this entity is relevant.""",
    )

    GEO_CONTAINS = Semantic(
        id="geoContains",
        ref="schema:geoContains",
        text="""Represents a relationship between two geometries (or the places they represent), relating a containing geometry to a contained geometry. "a contains b iff no points of b lie in the exterior of a, and at least one point of the interior of b lies in the interior of a". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).""",
    )

    RECIPE_YIELD = Semantic(
        id="recipeYield",
        ref="schema:recipeYield",
        text="""The quantity produced by the recipe (for example, number of people served, number of servings, etc).""",
    )

    TITLE_E_I_D_R = Semantic(
        id="titleEIDR",
        ref="schema:titleEIDR",
        text="""An [EIDR](https://eidr.org/) (Entertainment Identifier Registry) [[identifier]] representing at the most general/abstract level, a work of film or television.

For example, the motion picture known as "Ghostbusters" has a titleEIDR of  "10.5240/7EC7-228A-510A-053E-CBB8-J". This title (or work) may have several variants, which EIDR calls "edits". See [[editEIDR]].

Since schema.org types like [[Movie]] and [[TVEpisode]] can be used for both works and their multiple expressions, it is possible to use [[titleEIDR]] alone (for a general description), or alongside [[editEIDR]] for a more edit-specific description.
""",
    )

    SECURITY_CLEARANCE_REQUIREMENT = Semantic(
        id="securityClearanceRequirement",
        ref="schema:securityClearanceRequirement",
        text="""A description of any security clearance requirements of the job.""",
    )

    N_G_O = Semantic(
        id="NGO",
        ref="schema:NGO",
        text="""Organization: Non-governmental Organization.""",
    )

    DISTANCE = Semantic(
        id="Distance",
        ref="schema:Distance",
        text="""Properties that take Distances as values are of the form \'&lt;Number&gt; &lt;Length unit of measure&gt;\'. E.g., \'7 ft\'.""",
    )

    LIVING_WITH_HEALTH_ASPECT = Semantic(
        id="LivingWithHealthAspect",
        ref="schema:LivingWithHealthAspect",
        text="""Information about coping or life related to the topic.""",
    )

    U_K_NONPROFIT_TYPE = Semantic(
        id="UKNonprofitType",
        ref="schema:UKNonprofitType",
        text="""UKNonprofitType: Non-profit organization type originating from the United Kingdom.""",
    )

    PHARMACY_SPECIALTY = Semantic(
        id="PharmacySpecialty",
        ref="schema:PharmacySpecialty",
        text="""The practice or art and science of preparing and dispensing drugs and medicines.""",
    )

    DIAGRAM = Semantic(
        id="diagram",
        ref="schema:diagram",
        text="""An image containing a diagram that illustrates the structure and/or its component substructures and/or connections with other structures.""",
    )

    E_U_ENERGY_EFFICIENCY_CATEGORY_A3_PLUS = Semantic(
        id="EUEnergyEfficiencyCategoryA3Plus",
        ref="schema:EUEnergyEfficiencyCategoryA3Plus",
        text="""Represents EU Energy Efficiency Class A+++ as defined in EU energy labeling regulations.""",
    )

    ORDER_PROBLEM = Semantic(
        id="OrderProblem",
        ref="schema:OrderProblem",
        text="""OrderStatus representing that there is a problem with the order.""",
    )

    CODE_SAMPLE_TYPE = Semantic(
        id="codeSampleType",
        ref="schema:codeSampleType",
        text="""What type of code sample: full (compile ready) solution, code snippet, inline code, scripts, template.""",
    )

    AIRLINE = Semantic(
        id="Airline",
        ref="schema:Airline",
        text="""An organization that provides flights for passengers.""",
    )

    OFFLINE_EVENT_ATTENDANCE_MODE = Semantic(
        id="OfflineEventAttendanceMode",
        ref="schema:OfflineEventAttendanceMode",
        text="""OfflineEventAttendanceMode - an event that is primarily conducted offline. """,
    )

    MEDICAL_CONDITION_STAGE = Semantic(
        id="MedicalConditionStage",
        ref="schema:MedicalConditionStage",
        text="""A stage of a medical condition, such as \'Stage IIIa\'.""",
    )

    LIMITED_BY_GUARANTEE_CHARITY = Semantic(
        id="LimitedByGuaranteeCharity",
        ref="schema:LimitedByGuaranteeCharity",
        text="""LimitedByGuaranteeCharity: Non-profit type referring to a charitable company that is limited by guarantee (UK).""",
    )

    MAXIMUM_ENROLLMENT = Semantic(
        id="maximumEnrollment",
        ref="schema:maximumEnrollment",
        text="""The maximum number of students who may be enrolled in the program.""",
    )

    RISKS_OR_COMPLICATIONS_HEALTH_ASPECT = Semantic(
        id="RisksOrComplicationsHealthAspect",
        ref="schema:RisksOrComplicationsHealthAspect",
        text="""Information about the risk factors and possible complications that may follow a topic.""",
    )

    TOUR_BOOKING_PAGE = Semantic(
        id="tourBookingPage",
        ref="schema:tourBookingPage",
        text="""A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]] or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate.""",
    )

    CATHOLIC_CHURCH = Semantic(
        id="CatholicChurch", ref="schema:CatholicChurch", text="""A Catholic church."""
    )

    BROADCAST_DISPLAY_NAME = Semantic(
        id="broadcastDisplayName",
        ref="schema:broadcastDisplayName",
        text="""The name displayed in the channel guide. For many US affiliates, it is the network name.""",
    )

    ESTIMATED_FLIGHT_DURATION = Semantic(
        id="estimatedFlightDuration",
        ref="schema:estimatedFlightDuration",
        text="""The estimated time the flight will take.""",
    )

    STRUCTURAL_CLASS = Semantic(
        id="structuralClass",
        ref="schema:structuralClass",
        text="""The name given to how bone physically connects to each other.""",
    )

    GEOSPATIAL_GEOMETRY = Semantic(
        id="GeospatialGeometry",
        ref="schema:GeospatialGeometry",
        text="""(Eventually to be defined as) a supertype of GeoShape designed to accommodate definitions from Geo-Spatial best practices.""",
    )

    TYPE_OF_GOOD = Semantic(
        id="typeOfGood",
        ref="schema:typeOfGood",
        text="""The product that this structured value is referring to.""",
    )

    PROVIDES_SERVICE = Semantic(
        id="providesService",
        ref="schema:providesService",
        text="""The service provided by this channel.""",
    )

    MOLECULAR_WEIGHT = Semantic(
        id="molecularWeight",
        ref="schema:molecularWeight",
        text="""This is the molecular weight of the entity being described, not of the parent. Units should be included in the form \'&lt;Number&gt; &lt;unit&gt;\', for example \'12 amu\' or as \'&lt;QuantitativeValue&gt;.""",
    )

    TEACHES = Semantic(
        id="teaches",
        ref="schema:teaches",
        text="""The item being described is intended to help a person learn the competency or learning outcome defined by the referenced term.""",
    )

    MUSCLE = Semantic(
        id="Muscle",
        ref="schema:Muscle",
        text="""A muscle is an anatomical structure consisting of a contractile form of tissue that animals use to effect movement.""",
    )

    OPINION_NEWS_ARTICLE = Semantic(
        id="OpinionNewsArticle",
        ref="schema:OpinionNewsArticle",
        text="""An [[OpinionNewsArticle]] is a [[NewsArticle]] that primarily expresses opinions rather than journalistic reporting of news and events. For example, a [[NewsArticle]] consisting of a column or [[Blog]]/[[BlogPosting]] entry in the Opinions section of a news publication. """,
    )

    ORDER_QUANTITY = Semantic(
        id="orderQuantity",
        ref="schema:orderQuantity",
        text="""The number of the item ordered. If the property is not set, assume the quantity is one.""",
    )

    STATUS_ENUMERATION = Semantic(
        id="StatusEnumeration",
        ref="schema:StatusEnumeration",
        text="""Lists or enumerations dealing with status types.""",
    )

    ENTERTAINMENT_BUSINESS = Semantic(
        id="entertainmentBusiness",
        ref="schema:entertainmentBusiness",
        text="""A sub property of location. The entertainment business where the action occurred.""",
    )

    HOW_TO_TOOL = Semantic(
        id="HowToTool",
        ref="schema:HowToTool",
        text="""A tool used (but not consumed) when performing instructions for how to achieve a result.""",
    )

    BODY_MEASUREMENT_TYPE_ENUMERATION = Semantic(
        id="BodyMeasurementTypeEnumeration",
        ref="schema:BodyMeasurementTypeEnumeration",
        text="""Enumerates types (or dimensions) of a person\'s body measurements, for example for fitting of clothes.""",
    )

    ICE_CREAM_SHOP = Semantic(
        id="IceCreamShop", ref="schema:IceCreamShop", text="""An ice cream shop."""
    )

    BUS_OR_COACH = Semantic(
        id="BusOrCoach",
        ref="schema:BusOrCoach",
        text="""A bus (also omnibus or autobus) is a road vehicle designed to carry passengers. Coaches are luxury busses, usually in service for long distance travel.""",
    )

    ENDORSERS = Semantic(
        id="endorsers",
        ref="schema:endorsers",
        text="""People or organizations that endorse the plan.""",
    )

    DEPOSIT_ACCOUNT = Semantic(
        id="DepositAccount",
        ref="schema:DepositAccount",
        text="""A type of Bank Account with a main purpose of depositing funds to gain interest or other benefits.""",
    )

    EDITED_OR_CROPPED_CONTENT = Semantic(
        id="EditedOrCroppedContent",
        ref="schema:EditedOrCroppedContent",
        text="""Content coded \'edited or cropped content\' in a [[MediaReview]], considered in the context of how it was published or shared.

For a [[VideoObject]] to be \'edited or cropped content\': The video has been edited or rearranged. This category applies to time edits, including editing multiple videos together to alter the story being told or editing out large portions from a video.

For an [[ImageObject]] to be \'edited or cropped content\': Presenting a part of an image from a larger whole to mislead the viewer.

For an [[ImageObject]] with embedded text to be \'edited or cropped content\': Presenting a part of an image from a larger whole to mislead the viewer.

For an [[AudioObject]] to be \'edited or cropped content\': The audio has been edited or rearranged. This category applies to time edits, including editing multiple audio clips together to alter the story being told or editing out large portions from the recording.
""",
    )

    PARKING_FACILITY = Semantic(
        id="ParkingFacility",
        ref="schema:ParkingFacility",
        text="""A parking lot or other parking facility.""",
    )

    RETURN_LABEL_SOURCE = Semantic(
        id="returnLabelSource",
        ref="schema:returnLabelSource",
        text="""The method (from an enumeration) by which the customer obtains a return shipping label for a product returned for any reason.""",
    )

    RECRUITING = Semantic(
        id="Recruiting", ref="schema:Recruiting", text="""Recruiting participants."""
    )

    THING = Semantic(
        id="Thing", ref="schema:Thing", text="""The most generic type of item."""
    )

    HOW_TO_TIP = Semantic(
        id="HowToTip",
        ref="schema:HowToTip",
        text="""An explanation in the instructions for how to achieve a result. It provides supplementary information about a technique, supply, author\'s preference, etc. It can explain what could be done, or what should not be done, but doesn\'t specify what should be done (see HowToDirection).""",
    )

    DATE_POSTED = Semantic(
        id="datePosted",
        ref="schema:datePosted",
        text="""Publication date of an online listing.""",
    )

    EVENT = Semantic(
        id="Event",
        ref="schema:Event",
        text="""An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the [[offers]] property. Repeated events may be structured as separate Event objects.""",
    )

    GEO_COVERED_BY = Semantic(
        id="geoCoveredBy",
        ref="schema:geoCoveredBy",
        text="""Represents a relationship between two geometries (or the places they represent), relating a geometry to another that covers it. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).""",
    )

    PHOTOS = Semantic(
        id="photos", ref="schema:photos", text="""Photographs of this place."""
    )

    VIDEO_GAME = Semantic(
        id="VideoGame",
        ref="schema:VideoGame",
        text="""A video game is an electronic game that involves human interaction with a user interface to generate visual feedback on a video device.""",
    )

    RENT_ACTION = Semantic(
        id="RentAction",
        ref="schema:RentAction",
        text="""The act of giving money in return for temporary use, but not ownership, of an object such as a vehicle or property. For example, an agent rents a property from a landlord in exchange for a periodic payment.""",
    )

    EVENT_STATUS = Semantic(
        id="eventStatus",
        ref="schema:eventStatus",
        text="""An eventStatus of an event represents its status; particularly useful when an event is cancelled or rescheduled.""",
    )

    IN_ALBUM = Semantic(
        id="inAlbum",
        ref="schema:inAlbum",
        text="""The album to which this recording belongs.""",
    )

    D_J_MIX_ALBUM = Semantic(
        id="DJMixAlbum", ref="schema:DJMixAlbum", text="""DJMixAlbum."""
    )

    PASSENGER_SEQUENCE_NUMBER = Semantic(
        id="passengerSequenceNumber",
        ref="schema:passengerSequenceNumber",
        text="""The passenger\'s sequence number as assigned by the airline.""",
    )

    NONPROFIT501N = Semantic(
        id="Nonprofit501n",
        ref="schema:Nonprofit501n",
        text="""Nonprofit501n: Non-profit type referring to Charitable Risk Pools.""",
    )

    QUALIFICATIONS = Semantic(
        id="qualifications",
        ref="schema:qualifications",
        text="""Specific qualifications required for this role or Occupation.""",
    )

    AMUSEMENT_PARK = Semantic(
        id="AmusementPark", ref="schema:AmusementPark", text="""An amusement park."""
    )

    NONPROFIT501C19 = Semantic(
        id="Nonprofit501c19",
        ref="schema:Nonprofit501c19",
        text="""Nonprofit501c19: Non-profit type referring to Post or Organization of Past or Present Members of the Armed Forces.""",
    )

    AFFILIATION = Semantic(
        id="affiliation",
        ref="schema:affiliation",
        text="""An organization that this person is affiliated with. For example, a school/university, a club, or a team.""",
    )

    SPEED = Semantic(
        id="speed",
        ref="schema:speed",
        text="""The speed range of the vehicle. If the vehicle is powered by an engine, the upper limit of the speed range (indicated by [[maxValue]] should be the maximum speed achievable under regular conditions.\\n\\nTypical unit code(s): KMH for km/h, HM for mile per hour (0.447 04 m/s), KNT for knot\\n\\n*Note 1: Use [[minValue]] and [[maxValue]] to indicate the range. Typically, the minimal value is zero.\\n* Note 2: There are many different ways of measuring the speed range. You can link to information about how the given value has been determined using the [[valueReference]] property.""",
    )

    EARLY_PREPAYMENT_PENALTY = Semantic(
        id="earlyPrepaymentPenalty",
        ref="schema:earlyPrepaymentPenalty",
        text="""The amount to be paid as a penalty in the event of early payment of the loan.""",
    )

    EXAMPLE_OF_WORK = Semantic(
        id="exampleOfWork",
        ref="schema:exampleOfWork",
        text="""A creative work that this work is an example/instance/realization/derivation of.""",
    )

    COVER_ART = Semantic(
        id="CoverArt",
        ref="schema:CoverArt",
        text="""The artwork on the outer surface of a CreativeWork.""",
    )

    LINE = Semantic(
        id="line",
        ref="schema:line",
        text="""A line is a point-to-point path consisting of two or more points. A line is expressed as a series of two or more point objects separated by space.""",
    )

    ORIGINAL_MEDIA_CONTENT = Semantic(
        id="OriginalMediaContent",
        ref="schema:OriginalMediaContent",
        text="""Content coded \'as original media content\' in a [[MediaReview]], considered in the context of how it was published or shared.

For a [[VideoObject]] to be \'original\': No evidence the footage has been misleadingly altered or manipulated, though it may contain false or misleading claims.

For an [[ImageObject]] to be \'original\': No evidence the image has been misleadingly altered or manipulated, though it may still contain false or misleading claims.

For an [[ImageObject]] with embedded text to be \'original\': No evidence the image has been misleadingly altered or manipulated, though it may still contain false or misleading claims.

For an [[AudioObject]] to be \'original\': No evidence the audio has been misleadingly altered or manipulated, though it may contain false or misleading claims.
""",
    )

    AUDIOBOOK_FORMAT = Semantic(
        id="AudiobookFormat",
        ref="schema:AudiobookFormat",
        text="""Book format: Audiobook. This is an enumerated value for use with the bookFormat property. There is also a type \'Audiobook\' in the bib extension which includes Audiobook specific properties.""",
    )

    DISTRIBUTION = Semantic(
        id="distribution",
        ref="schema:distribution",
        text="""A downloadable form of this dataset, at a specific location, in a specific format.""",
    )

    START_OFFSET = Semantic(
        id="startOffset",
        ref="schema:startOffset",
        text="""The start time of the clip expressed as the number of seconds from the beginning of the work.""",
    )

    SHA256 = Semantic(
        id="sha256",
        ref="schema:sha256",
        text="""The [SHA-2](https://en.wikipedia.org/wiki/SHA-2) SHA256 hash of the content of the item. For example, a zero-length input has value \'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\'""",
    )

    CARBOHYDRATE_CONTENT = Semantic(
        id="carbohydrateContent",
        ref="schema:carbohydrateContent",
        text="""The number of grams of carbohydrates.""",
    )

    PATIENT_EXPERIENCE_HEALTH_ASPECT = Semantic(
        id="PatientExperienceHealthAspect",
        ref="schema:PatientExperienceHealthAspect",
        text="""Content about the real life experience of patients or people that have lived a similar experience about the topic. May be forums, topics, Q-and-A and related material.""",
    )

    CIVIC_STRUCTURE = Semantic(
        id="CivicStructure",
        ref="schema:CivicStructure",
        text="""A public structure, such as a town hall or concert hall.""",
    )

    SERVICE_SMS_NUMBER = Semantic(
        id="serviceSmsNumber",
        ref="schema:serviceSmsNumber",
        text="""The number to access the service by text message.""",
    )

    MAXIMUM_PHYSICAL_ATTENDEE_CAPACITY = Semantic(
        id="maximumPhysicalAttendeeCapacity",
        ref="schema:maximumPhysicalAttendeeCapacity",
        text="""The maximum physical attendee capacity of an [[Event]] whose [[eventAttendanceMode]] is [[OfflineEventAttendanceMode]] (or the offline aspects, in the case of a [[MixedEventAttendanceMode]]). """,
    )

    EMISSIONS_C_O2 = Semantic(
        id="emissionsCO2",
        ref="schema:emissionsCO2",
        text="""The CO2 emissions in g/km. When used in combination with a QuantitativeValue, put "g/km" into the unitText property of that value, since there is no UN/CEFACT Common Code for "g/km".""",
    )

    DATASET = Semantic(
        id="dataset",
        ref="schema:dataset",
        text="""A dataset contained in this catalog.""",
    )

    MAX_PRICE = Semantic(
        id="maxPrice",
        ref="schema:maxPrice",
        text="""The highest price if the price is a range.""",
    )

    PREPARATION = Semantic(
        id="preparation",
        ref="schema:preparation",
        text="""Typical preparation that a patient must undergo before having the procedure performed.""",
    )

    PROTEIN_CONTENT = Semantic(
        id="proteinContent",
        ref="schema:proteinContent",
        text="""The number of grams of protein.""",
    )

    WARRANTY = Semantic(
        id="warranty",
        ref="schema:warranty",
        text="""The warranty promise(s) included in the offer.""",
    )

    PERFORM_TIME = Semantic(
        id="performTime",
        ref="schema:performTime",
        text="""The length of time it takes to perform instructions or a direction (not including time to prepare the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).""",
    )

    DOCUMENTATION = Semantic(
        id="documentation",
        ref="schema:documentation",
        text="""Further documentation describing the Web API in more detail.""",
    )

    T_V_SEASON = Semantic(
        id="TVSeason",
        ref="schema:TVSeason",
        text="""Season dedicated to TV broadcast and associated online delivery.""",
    )

    RECORDED_AT = Semantic(
        id="recordedAt",
        ref="schema:recordedAt",
        text="""The Event where the CreativeWork was recorded. The CreativeWork may capture all or part of the event.""",
    )

    LOW_PRICE = Semantic(
        id="lowPrice",
        ref="schema:lowPrice",
        text="""The lowest price of all offers available.\\n\\nUsage guidelines:\\n\\n* Use values from 0123456789 (Unicode \'DIGIT ZERO\' (U+0030) to \'DIGIT NINE\' (U+0039)) rather than superficially similiar Unicode symbols.\\n* Use \'.\' (Unicode \'FULL STOP\' (U+002E)) rather than \',\' to indicate a decimal point. Avoid using these symbols as a readability separator.""",
    )

    BENEFICIARY_BANK = Semantic(
        id="beneficiaryBank",
        ref="schema:beneficiaryBank",
        text="""A bank or bank’s branch, financial institution or international financial institution operating the beneficiary’s bank account or releasing funds for the beneficiary.""",
    )

    GEO_CROSSES = Semantic(
        id="geoCrosses",
        ref="schema:geoCrosses",
        text="""Represents a relationship between two geometries (or the places they represent), relating a geometry to another that crosses it: "a crosses b: they have some but not all interior points in common, and the dimension of the intersection is less than that of at least one of them". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).""",
    )

    REMAINING_ATTENDEE_CAPACITY = Semantic(
        id="remainingAttendeeCapacity",
        ref="schema:remainingAttendeeCapacity",
        text="""The number of attendee places for an event that remain unallocated.""",
    )

    JOB_START_DATE = Semantic(
        id="jobStartDate",
        ref="schema:jobStartDate",
        text="""The date on which a successful applicant for this job would be expected to start work. Choose a specific date in the future or use the jobImmediateStart property to indicate the position is to be filled as soon as possible.""",
    )

    FEES_AND_COMMISSIONS_SPECIFICATION = Semantic(
        id="feesAndCommissionsSpecification",
        ref="schema:feesAndCommissionsSpecification",
        text="""Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.""",
    )

    PRESCRIPTION_ONLY = Semantic(
        id="PrescriptionOnly",
        ref="schema:PrescriptionOnly",
        text="""Available by prescription only.""",
    )

    CONDITIONS_OF_ACCESS = Semantic(
        id="conditionsOfAccess",
        ref="schema:conditionsOfAccess",
        text="""Conditions that affect the availability of, or method(s) of access to, an item. Typically used for real world items such as an [[ArchiveComponent]] held by an [[ArchiveOrganization]]. This property is not suitable for use as a general Web access control mechanism. It is expressed only in natural language.\\n\\nFor example "Available by appointment from the Reading Room" or "Accessible only from logged-in accounts ". """,
    )

    DISTINGUISHING_SIGN = Semantic(
        id="distinguishingSign",
        ref="schema:distinguishingSign",
        text="""One of a set of signs and symptoms that can be used to distinguish this diagnosis from others in the differential diagnosis.""",
    )

    NUM_CHILDREN = Semantic(
        id="numChildren",
        ref="schema:numChildren",
        text="""The number of children staying in the unit.""",
    )

    BUS_TRIP = Semantic(
        id="BusTrip", ref="schema:BusTrip", text="""A trip on a commercial bus line."""
    )

    TIME = Semantic(
        id="Time",
        ref="schema:Time",
        text="""A point in time recurring on multiple days in the form hh:mm:ss[Z|(+|-)hh:mm] (see [XML schema for details](http://www.w3.org/TR/xmlschema-2/#time)).""",
    )

    IATA_CODE = Semantic(
        id="iataCode",
        ref="schema:iataCode",
        text="""IATA identifier for an airline or airport.""",
    )

    OPPONENT = Semantic(
        id="opponent",
        ref="schema:opponent",
        text="""A sub property of participant. The opponent on this action.""",
    )

    BED_DETAILS = Semantic(
        id="BedDetails",
        ref="schema:BedDetails",
        text="""An entity holding detailed information about the available bed types, e.g. the quantity of twin beds for a hotel room. For the single case of just one bed of a certain type, you can use bed directly with a text. See also [[BedType]] (under development).""",
    )

    LANDLORD = Semantic(
        id="landlord",
        ref="schema:landlord",
        text="""A sub property of participant. The owner of the real estate property.""",
    )

    SUITE = Semantic(
        id="Suite",
        ref="schema:Suite",
        text="""A suite in a hotel or other public accommodation, denotes a class of luxury accommodations, the key feature of which is multiple rooms (Source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Suite_(hotel)">http://en.wikipedia.org/wiki/Suite_(hotel)</a>).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
""",
    )

    WEARABLE_SIZE_GROUP_GIRLS = Semantic(
        id="WearableSizeGroupGirls",
        ref="schema:WearableSizeGroupGirls",
        text="""Size group "Girls" for wearables.""",
    )

    HEALTH_PLAN_COPAY_OPTION = Semantic(
        id="healthPlanCopayOption",
        ref="schema:healthPlanCopayOption",
        text="""Whether the copay is before or after deductible, etc. TODO: Is this a closed set?""",
    )

    RECOGNIZING_AUTHORITY = Semantic(
        id="recognizingAuthority",
        ref="schema:recognizingAuthority",
        text="""If applicable, the organization that officially recognizes this entity as part of its endorsed system of medicine.""",
    )

    SUBSCRIPTION = Semantic(
        id="Subscription",
        ref="schema:Subscription",
        text="""Represents the subscription pricing component of the total price for an offered product.""",
    )

    IS_RESIZABLE = Semantic(
        id="isResizable",
        ref="schema:isResizable",
        text="""Whether the 3DModel allows resizing. For example, room layout applications often do not allow 3DModel elements to be resized to reflect reality.""",
    )

    CATEGORY_CODE_SET = Semantic(
        id="CategoryCodeSet",
        ref="schema:CategoryCodeSet",
        text="""A set of Category Code values.""",
    )

    WORK_EXAMPLE = Semantic(
        id="workExample",
        ref="schema:workExample",
        text="""Example/instance/realization/derivation of the concept of this creative work. eg. The paperback edition, first edition, or eBook.""",
    )

    SIZE = Semantic(
        id="size",
        ref="schema:size",
        text="""A standardized size of a product or creative work, specified either through a simple textual string (for example \'XL\', \'32Wx34L\'), a  QuantitativeValue with a unitCode, or a comprehensive and structured [[SizeSpecification]]; in other cases, the [[width]], [[height]], [[depth]] and [[weight]] properties may be more applicable. """,
    )

    LUNG = Semantic(
        id="Lung",
        ref="schema:Lung",
        text="""Lung and respiratory system clinical examination.""",
    )

    ATTENDEE = Semantic(
        id="attendee",
        ref="schema:attendee",
        text="""A person or organization attending the event.""",
    )

    ACCESSIBILITY_HAZARD = Semantic(
        id="accessibilityHazard",
        ref="schema:accessibilityHazard",
        text="""A characteristic of the described resource that is physiologically dangerous to some users. Related to WCAG 2.0 guideline 2.3 ([WebSchemas wiki lists possible values](http://www.w3.org/wiki/WebSchemas/Accessibility)).""",
    )

    MUSIC_ARRANGEMENT = Semantic(
        id="musicArrangement",
        ref="schema:musicArrangement",
        text="""An arrangement derived from the composition.""",
    )

    LEI_CODE = Semantic(
        id="leiCode",
        ref="schema:leiCode",
        text="""An organization identifier that uniquely identifies a legal entity as defined in ISO 17442.""",
    )

    RETURN_POLICY_SEASONAL_OVERRIDE = Semantic(
        id="returnPolicySeasonalOverride",
        ref="schema:returnPolicySeasonalOverride",
        text="""Seasonal override of a return policy.""",
    )

    NONPROFIT501C22 = Semantic(
        id="Nonprofit501c22",
        ref="schema:Nonprofit501c22",
        text="""Nonprofit501c22: Non-profit type referring to Withdrawal Liability Payment Funds.""",
    )

    INCLUDED_IN_DATA_CATALOG = Semantic(
        id="includedInDataCatalog",
        ref="schema:includedInDataCatalog",
        text="""A data catalog which contains this dataset.""",
    )

    COPYRIGHT_YEAR = Semantic(
        id="copyrightYear",
        ref="schema:copyrightYear",
        text="""The year during which the claimed copyright for the CreativeWork was first asserted.""",
    )

    PROFESSIONAL_SERVICE = Semantic(
        id="ProfessionalService",
        ref="schema:ProfessionalService",
        text="""Original definition: "provider of professional services."\\n\\nThe general [[ProfessionalService]] type for local businesses was deprecated due to confusion with [[Service]]. For reference, the types that it included were: [[Dentist]],
        [[AccountingService]], [[Attorney]], [[Notary]], as well as types for several kinds of [[HomeAndConstructionBusiness]]: [[Electrician]], [[GeneralContractor]],
        [[HousePainter]], [[Locksmith]], [[Plumber]], [[RoofingContractor]]. [[LegalService]] was introduced as a more inclusive supertype of [[Attorney]].""",
    )

    LENDER = Semantic(
        id="lender",
        ref="schema:lender",
        text="""A sub property of participant. The person that lends the object being borrowed.""",
    )

    INVERSE_OF = Semantic(
        id="inverseOf",
        ref="schema:inverseOf",
        text="""Relates a property to a property that is its inverse. Inverse properties relate the same pairs of items to each other, but in reversed direction. For example, the \'alumni\' and \'alumniOf\' properties are inverseOf each other. Some properties don\'t have explicit inverses; in these situations RDFa and JSON-LD syntax for reverse properties can be used.""",
    )

    WEB_CONTENT = Semantic(
        id="WebContent",
        ref="schema:WebContent",
        text="""WebContent is a type representing all [[WebPage]], [[WebSite]] and [[WebPageElement]] content. It is sometimes the case that detailed distinctions between Web pages, sites and their parts is not always important or obvious. The  [[WebContent]] type makes it easier to describe Web-addressable content without requiring such distinctions to always be stated. (The intent is that the existing types [[WebPage]], [[WebSite]] and [[WebPageElement]] will eventually be declared as subtypes of [[WebContent]]).""",
    )

    VIDEO_GALLERY = Semantic(
        id="VideoGallery",
        ref="schema:VideoGallery",
        text="""Web page type: Video gallery page.""",
    )

    MERCHANT_RETURN_FINITE_RETURN_WINDOW = Semantic(
        id="MerchantReturnFiniteReturnWindow",
        ref="schema:MerchantReturnFiniteReturnWindow",
        text="""Specifies that there is a finite window for product returns.""",
    )

    TERM_DURATION = Semantic(
        id="termDuration",
        ref="schema:termDuration",
        text="""The amount of time in a term as defined by the institution. A term is a length of time where students take one or more classes. Semesters and quarters are common units for term.""",
    )

    DRAW_ACTION = Semantic(
        id="DrawAction",
        ref="schema:DrawAction",
        text="""The act of producing a visual/graphical representation of an object, typically with a pen/pencil and paper as instruments.""",
    )

    REFUND_TYPE = Semantic(
        id="refundType",
        ref="schema:refundType",
        text="""A refund type, from an enumerated list.""",
    )

    GROCERY_STORE = Semantic(
        id="GroceryStore", ref="schema:GroceryStore", text="""A grocery store."""
    )

    T_V_CLIP = Semantic(
        id="TVClip",
        ref="schema:TVClip",
        text="""A short TV program or a segment/part of a TV program.""",
    )

    NORMAL_RANGE = Semantic(
        id="normalRange",
        ref="schema:normalRange",
        text="""Range of acceptable values for a typical patient, when applicable.""",
    )

    TOURIST_ATTRACTION = Semantic(
        id="TouristAttraction",
        ref="schema:TouristAttraction",
        text="""A tourist attraction.  In principle any Thing can be a [[TouristAttraction]], from a [[Mountain]] and [[LandmarksOrHistoricalBuildings]] to a [[LocalBusiness]].  This Type can be used on its own to describe a general [[TouristAttraction]], or be used as an [[additionalType]] to add tourist attraction properties to any other type.  (See examples below)""",
    )

    MEDIA_SUBSCRIPTION = Semantic(
        id="MediaSubscription",
        ref="schema:MediaSubscription",
        text="""A subscription which allows a user to access media including audio, video, books, etc.""",
    )

    AGENT = Semantic(
        id="agent",
        ref="schema:agent",
        text="""The direct performer or driver of the action (animate or inanimate). e.g. *John* wrote a book.""",
    )

    RECORDED_AS = Semantic(
        id="recordedAs",
        ref="schema:recordedAs",
        text="""An audio recording of the work.""",
    )

    LITERARY_EVENT = Semantic(
        id="LiteraryEvent",
        ref="schema:LiteraryEvent",
        text="""Event type: Literary event.""",
    )

    PHOTOGRAPH = Semantic(
        id="Photograph", ref="schema:Photograph", text="""A photograph."""
    )

    JURISDICTION = Semantic(
        id="jurisdiction",
        ref="schema:jurisdiction",
        text="""Indicates a legal jurisdiction, e.g. of some legislation, or where some government service is based.""",
    )

    ORGANIZATION_ROLE = Semantic(
        id="OrganizationRole",
        ref="schema:OrganizationRole",
        text="""A subclass of Role used to describe roles within organizations.""",
    )

    RESERVATION_CONFIRMED = Semantic(
        id="ReservationConfirmed",
        ref="schema:ReservationConfirmed",
        text="""The status of a confirmed reservation.""",
    )

    HOSPITAL = Semantic(id="Hospital", ref="schema:Hospital", text="""A hospital.""")

    C_D_FORMAT = Semantic(id="CDFormat", ref="schema:CDFormat", text="""CDFormat.""")

    AGGREGATE_RATING = Semantic(
        id="AggregateRating",
        ref="schema:AggregateRating",
        text="""The average rating based on multiple ratings or reviews.""",
    )

    BREADCRUMB = Semantic(
        id="breadcrumb",
        ref="schema:breadcrumb",
        text="""A set of links that can help a user understand and navigate a website hierarchy.""",
    )

    MAXIMUM_INTAKE = Semantic(
        id="maximumIntake",
        ref="schema:maximumIntake",
        text="""Recommended intake of this supplement for a given population as defined by a specific recommending authority.""",
    )

    WEAR_ACTION = Semantic(
        id="WearAction",
        ref="schema:WearAction",
        text="""The act of dressing oneself in clothing.""",
    )

    EXIF_DATA = Semantic(
        id="exifData", ref="schema:exifData", text="""exif data for this object."""
    )

    IS_AVAILABLE_GENERICALLY = Semantic(
        id="isAvailableGenerically",
        ref="schema:isAvailableGenerically",
        text="""True if the drug is available in a generic form (regardless of name).""",
    )

    RHEUMATOLOGIC = Semantic(
        id="Rheumatologic",
        ref="schema:Rheumatologic",
        text="""A specific branch of medical science that deals with the study and treatment of rheumatic, autoimmune or joint diseases.""",
    )

    W_P_SIDE_BAR = Semantic(
        id="WPSideBar",
        ref="schema:WPSideBar",
        text="""A sidebar section of the page.""",
    )

    OCCUPATIONAL_THERAPY = Semantic(
        id="OccupationalTherapy",
        ref="schema:OccupationalTherapy",
        text="""A treatment of people with physical, emotional, or social problems, using purposeful activity to help them overcome or learn to deal with their problems.""",
    )

    MUSIC_ALBUM_PRODUCTION_TYPE = Semantic(
        id="MusicAlbumProductionType",
        ref="schema:MusicAlbumProductionType",
        text="""Classification of the album by it\'s type of content: soundtrack, live album, studio album, etc.""",
    )

    PLAY_MODE = Semantic(
        id="playMode",
        ref="schema:playMode",
        text="""Indicates whether this game is multi-player, co-op or single-player.  The game can be marked as multi-player, co-op and single-player at the same time.""",
    )

    SUGGESTED_MEASUREMENT = Semantic(
        id="suggestedMeasurement",
        ref="schema:suggestedMeasurement",
        text="""A suggested range of body measurements for the intended audience or person, for example inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size chart for wearable products.""",
    )

    BEFRIEND_ACTION = Semantic(
        id="BefriendAction",
        ref="schema:BefriendAction",
        text="""The act of forming a personal connection with someone (object) mutually/bidirectionally/symmetrically.\\n\\nRelated actions:\\n\\n* [[FollowAction]]: Unlike FollowAction, BefriendAction implies that the connection is reciprocal.""",
    )

    ANSWER_COUNT = Semantic(
        id="answerCount",
        ref="schema:answerCount",
        text="""The number of answers this question has received.""",
    )

    ITEM_LIST_ORDER_DESCENDING = Semantic(
        id="ItemListOrderDescending",
        ref="schema:ItemListOrderDescending",
        text="""An ItemList ordered with higher values listed first.""",
    )

    ENCODINGS = Semantic(
        id="encodings",
        ref="schema:encodings",
        text="""A media object that encodes this CreativeWork.""",
    )

    POST_OFFICE = Semantic(
        id="PostOffice", ref="schema:PostOffice", text="""A post office."""
    )

    ORDER_STATUS = Semantic(
        id="orderStatus",
        ref="schema:orderStatus",
        text="""The current status of the order.""",
    )

    WINERY = Semantic(id="Winery", ref="schema:Winery", text="""A winery.""")

    FILM_ACTION = Semantic(
        id="FilmAction",
        ref="schema:FilmAction",
        text="""The act of capturing sound and moving images on film, video, or digitally.""",
    )

    TARGET = Semantic(
        id="target",
        ref="schema:target",
        text="""Indicates a target EntryPoint for an Action.""",
    )

    CVD_NUM_I_C_U_BEDS_OCC = Semantic(
        id="cvdNumICUBedsOcc",
        ref="schema:cvdNumICUBedsOcc",
        text="""numicubedsocc - ICU BED OCCUPANCY: Total number of staffed inpatient ICU beds that are occupied.""",
    )

    RSVP_RESPONSE_TYPE = Semantic(
        id="RsvpResponseType",
        ref="schema:RsvpResponseType",
        text="""RsvpResponseType is an enumeration type whose instances represent responding to an RSVP request.""",
    )

    BODY_TYPE = Semantic(
        id="bodyType",
        ref="schema:bodyType",
        text="""Indicates the design and body style of the vehicle (e.g. station wagon, hatchback, etc.).""",
    )

    ORDER_PICKUP_AVAILABLE = Semantic(
        id="OrderPickupAvailable",
        ref="schema:OrderPickupAvailable",
        text="""OrderStatus representing availability of an order for pickup.""",
    )

    MOBILE_PHONE_STORE = Semantic(
        id="MobilePhoneStore",
        ref="schema:MobilePhoneStore",
        text="""A store that sells mobile phones and related accessories.""",
    )

    CONTINENT = Semantic(
        id="Continent",
        ref="schema:Continent",
        text="""One of the continents (for example, Europe or Africa).""",
    )

    MEDICAL_BUSINESS = Semantic(
        id="MedicalBusiness",
        ref="schema:MedicalBusiness",
        text="""A particular physical or virtual business of an organization for medical purposes. Examples of MedicalBusiness include differents business run by health professionals.""",
    )

    VITAL_SIGN = Semantic(
        id="VitalSign",
        ref="schema:VitalSign",
        text="""Vital signs are measures of various physiological functions in order to assess the most basic body functions.""",
    )

    BILLING_INCREMENT = Semantic(
        id="billingIncrement",
        ref="schema:billingIncrement",
        text="""This property specifies the minimal quantity and rounding increment that will be the basis for the billing. The unit of measurement is specified by the unitCode property.""",
    )

    MEASURED_PROPERTY = Semantic(
        id="measuredProperty",
        ref="schema:measuredProperty",
        text="""The measuredProperty of an [[Observation]], either a schema.org property, a property from other RDF-compatible systems e.g. W3C RDF Data Cube, or schema.org extensions such as [GS1\'s](https://www.gs1.org/voc/?show=properties).""",
    )

    COURSE_CODE = Semantic(
        id="courseCode",
        ref="schema:courseCode",
        text="""The identifier for the [[Course]] used by the course [[provider]] (e.g. CS101 or 6.001).""",
    )

    APPLIES_TO_DELIVERY_METHOD = Semantic(
        id="appliesToDeliveryMethod",
        ref="schema:appliesToDeliveryMethod",
        text="""The delivery method(s) to which the delivery charge or payment charge specification applies.""",
    )

    CVD_NUM_VENT = Semantic(
        id="cvdNumVent",
        ref="schema:cvdNumVent",
        text="""numvent - MECHANICAL VENTILATORS: Total number of ventilators available.""",
    )

    USER_TWEETS = Semantic(
        id="UserTweets",
        ref="schema:UserTweets",
        text="""UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].""",
    )

    NUMBER_OF_ACCOMMODATION_UNITS = Semantic(
        id="numberOfAccommodationUnits",
        ref="schema:numberOfAccommodationUnits",
        text="""Indicates the total (available plus unavailable) number of accommodation units in an [[ApartmentComplex]], or the number of accommodation units for a specific [[FloorPlan]] (within its specific [[ApartmentComplex]]). See also [[numberOfAvailableAccommodationUnits]].""",
    )

    DOWNLOAD_URL = Semantic(
        id="downloadUrl",
        ref="schema:downloadUrl",
        text="""If the file can be downloaded, URL to download the binary.""",
    )

    OBSERVATION = Semantic(
        id="Observation",
        ref="schema:Observation",
        text="""Instances of the class [[Observation]] are used to specify observations about an entity (which may or may not be an instance of a [[StatisticalPopulation]]), at a particular time. The principal properties of an [[Observation]] are [[observedNode]], [[measuredProperty]], [[measuredValue]] (or [[median]], etc.) and [[observationDate]] ([[measuredProperty]] properties can, but need not always, be W3C RDF Data Cube "measure properties", as in the [lifeExpectancy example](https://www.w3.org/TR/vocab-data-cube/#dsd-example)).
See also [[StatisticalPopulation]], and the [data and datasets](/docs/data-and-datasets.html) overview for more details.
  """,
    )

    MUSIC_RELEASE_FORMAT = Semantic(
        id="musicReleaseFormat",
        ref="schema:musicReleaseFormat",
        text="""Format of this release (the type of recording media used, ie. compact disc, digital media, LP, etc.).""",
    )

    SUBWAY_STATION = Semantic(
        id="SubwayStation", ref="schema:SubwayStation", text="""A subway station."""
    )

    CHILD_MAX_AGE = Semantic(
        id="childMaxAge", ref="schema:childMaxAge", text="""Maximal age of the child."""
    )

    CHILDREN = Semantic(
        id="children", ref="schema:children", text="""A child of the person."""
    )

    RADIO_BROADCAST_SERVICE = Semantic(
        id="RadioBroadcastService",
        ref="schema:RadioBroadcastService",
        text="""A delivery service through which radio content is provided via broadcast over the air or online.""",
    )

    SPOUSE = Semantic(
        id="spouse", ref="schema:spouse", text="""The person\'s spouse."""
    )

    CREATOR = Semantic(
        id="creator",
        ref="schema:creator",
        text="""The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork.""",
    )

    CHECKIN_TIME = Semantic(
        id="checkinTime",
        ref="schema:checkinTime",
        text="""The earliest someone may check into a lodging establishment.""",
    )

    LEGISLATION = Semantic(
        id="Legislation",
        ref="schema:Legislation",
        text="""A legal document such as an act, decree, bill, etc. (enforceable or not) or a component of a legal act (like an article).""",
    )

    PUBLISHED_BY = Semantic(
        id="publishedBy",
        ref="schema:publishedBy",
        text="""An agent associated with the publication event.""",
    )

    FREE_SHIPPING_THRESHOLD = Semantic(
        id="freeShippingThreshold",
        ref="schema:freeShippingThreshold",
        text="""A monetary value above which (or equal to) the shipping rate becomes free. Intended to be used via an [[OfferShippingDetails]] with [[shippingSettingsLink]] matching this [[ShippingRateSettings]].""",
    )

    EXPECTS_ACCEPTANCE_OF = Semantic(
        id="expectsAcceptanceOf",
        ref="schema:expectsAcceptanceOf",
        text="""An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.""",
    )

    EPISODE = Semantic(
        id="Episode",
        ref="schema:Episode",
        text="""A media episode (e.g. TV, radio, video game) which can be part of a series or season.""",
    )

    GROUP_BOARDING_POLICY = Semantic(
        id="GroupBoardingPolicy",
        ref="schema:GroupBoardingPolicy",
        text="""The airline boards by groups based on check-in time, priority, etc.""",
    )

    DRUG_CLASS = Semantic(
        id="DrugClass",
        ref="schema:DrugClass",
        text="""A class of medical drugs, e.g., statins. Classes can represent general pharmacological class, common mechanisms of action, common physiological effects, etc.""",
    )

    MOTORCYCLE = Semantic(
        id="Motorcycle",
        ref="schema:Motorcycle",
        text="""A motorcycle or motorbike is a single-track, two-wheeled motor vehicle.""",
    )

    PHYSICAL_EXAM = Semantic(
        id="PhysicalExam",
        ref="schema:PhysicalExam",
        text="""A type of physical examination of a patient performed by a physician. """,
    )

    DELIVERY_LEAD_TIME = Semantic(
        id="deliveryLeadTime",
        ref="schema:deliveryLeadTime",
        text="""The typical delay between the receipt of the order and the goods either leaving the warehouse or being prepared for pickup, in case the delivery method is on site pickup.""",
    )

    PRESCRIPTION_STATUS = Semantic(
        id="prescriptionStatus",
        ref="schema:prescriptionStatus",
        text="""Indicates the status of drug prescription eg. local catalogs classifications or whether the drug is available by prescription or over-the-counter, etc.""",
    )

    SERVICE_PHONE = Semantic(
        id="servicePhone",
        ref="schema:servicePhone",
        text="""The phone number to use to access the service.""",
    )

    INTEREST_RATE = Semantic(
        id="interestRate",
        ref="schema:interestRate",
        text="""The interest rate, charged or paid, applicable to the financial product. Note: This is different from the calculated annualPercentageRate.""",
    )

    UNIT_TEXT = Semantic(
        id="unitText",
        ref="schema:unitText",
        text="""A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for
<a href=\'unitCode\'>unitCode</a>.""",
    )

    END_DATE = Semantic(
        id="endDate",
        ref="schema:endDate",
        text="""The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).""",
    )

    PULMONARY = Semantic(
        id="Pulmonary",
        ref="schema:Pulmonary",
        text="""A specific branch of medical science that pertains to the study of the respiratory system and its respective disease states.""",
    )

    TRIAL_DESIGN = Semantic(
        id="trialDesign",
        ref="schema:trialDesign",
        text="""Specifics about the trial design (enumerated).""",
    )

    SENSORY_UNIT = Semantic(
        id="sensoryUnit",
        ref="schema:sensoryUnit",
        text="""The neurological pathway extension that inputs and sends information to the brain or spinal cord.""",
    )

    FROM_LOCATION = Semantic(
        id="fromLocation",
        ref="schema:fromLocation",
        text="""A sub property of location. The original location of the object or the agent before the action.""",
    )

    ACCESS_MODE = Semantic(
        id="accessMode",
        ref="schema:accessMode",
        text="""The human sensory perceptual system or cognitive faculty through which a person may process or perceive information. Expected values include: auditory, tactile, textual, visual, colorDependent, chartOnVisual, chemOnVisual, diagramOnVisual, mathOnVisual, musicOnVisual, textOnVisual.
      """,
    )

    TRAILER_WEIGHT = Semantic(
        id="trailerWeight",
        ref="schema:trailerWeight",
        text="""The permitted weight of a trailer attached to the vehicle.\\n\\nTypical unit code(s): KGM for kilogram, LBR for pound\\n* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.\\n* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].\\n* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.""",
    )

    COMPETENCY_REQUIRED = Semantic(
        id="competencyRequired",
        ref="schema:competencyRequired",
        text="""Knowledge, skill, ability or personal attribute that must be demonstrated by a person or other entity in order to do something such as earn an Educational Occupational Credential or understand a LearningResource.""",
    )

    ALBUM_RELEASE = Semantic(
        id="albumRelease",
        ref="schema:albumRelease",
        text="""A release of this album.""",
    )

    PRIMARY_IMAGE_OF_PAGE = Semantic(
        id="primaryImageOfPage",
        ref="schema:primaryImageOfPage",
        text="""Indicates the main image on the page.""",
    )

    RESTRICTED_DIET = Semantic(
        id="RestrictedDiet",
        ref="schema:RestrictedDiet",
        text="""A diet restricted to certain foods or preparations for cultural, religious, health or lifestyle reasons. """,
    )

    RELEASE_DATE = Semantic(
        id="releaseDate",
        ref="schema:releaseDate",
        text="""The release date of a product or product model. This can be used to distinguish the exact variant of a product.""",
    )

    MEDICAL_STUDY = Semantic(
        id="MedicalStudy",
        ref="schema:MedicalStudy",
        text="""A medical study is an umbrella type covering all kinds of research studies relating to human medicine or health, including observational studies and interventional trials and registries, randomized, controlled or not. When the specific type of study is known, use one of the extensions of this type, such as MedicalTrial or MedicalObservationalStudy. Also, note that this type should be used to mark up data that describes the study itself; to tag an article that publishes the results of a study, use MedicalScholarlyArticle. Note: use the code property of MedicalEntity to store study IDs, e.g. clinicaltrials.gov ID.""",
    )

    MOVIE_CLIP = Semantic(
        id="MovieClip",
        ref="schema:MovieClip",
        text="""A short segment/part of a movie.""",
    )

    LYMPHATIC_VESSEL = Semantic(
        id="LymphaticVessel",
        ref="schema:LymphaticVessel",
        text="""A type of blood vessel that specifically carries lymph fluid unidirectionally toward the heart.""",
    )

    FUNDING_AGENCY = Semantic(
        id="FundingAgency",
        ref="schema:FundingAgency",
        text="""A FundingAgency is an organization that implements one or more [[FundingScheme]]s and manages
    the granting process (via [[Grant]]s, typically [[MonetaryGrant]]s).
    A funding agency is not always required for grant funding, e.g. philanthropic giving, corporate sponsorship etc.
    
Examples of funding agencies include ERC, REA, NIH, Bill and Melinda Gates Foundation...
    """,
    )

    CLIP_NUMBER = Semantic(
        id="clipNumber",
        ref="schema:clipNumber",
        text="""Position of the clip within an ordered group of clips.""",
    )

    MORTGAGE_LOAN = Semantic(
        id="MortgageLoan",
        ref="schema:MortgageLoan",
        text="""A loan in which property or real estate is used as collateral. (A loan securitized against some real estate).""",
    )

    CVD_NUM_C19_HOSP_PATS = Semantic(
        id="cvdNumC19HospPats",
        ref="schema:cvdNumC19HospPats",
        text="""numc19hosppats - HOSPITALIZED: Patients currently hospitalized in an inpatient care location who have suspected or confirmed COVID-19.""",
    )

    SPEAKABLE_SPECIFICATION = Semantic(
        id="SpeakableSpecification",
        ref="schema:SpeakableSpecification",
        text="""A SpeakableSpecification indicates (typically via [[xpath]] or [[cssSelector]]) sections of a document that are highlighted as particularly [[speakable]]. Instances of this type are expected to be used primarily as values of the [[speakable]] property.""",
    )

    RESTOCKING_FEES = Semantic(
        id="RestockingFees",
        ref="schema:RestockingFees",
        text="""Specifies that the customer must pay a restocking fee when returning a product""",
    )

    SERVICE_CHANNEL = Semantic(
        id="ServiceChannel",
        ref="schema:ServiceChannel",
        text="""A means for accessing a service, e.g. a government office location, web site, or phone number.""",
    )

    AIRCRAFT = Semantic(
        id="aircraft",
        ref="schema:aircraft",
        text="""The kind of aircraft (e.g., "Boeing 747").""",
    )

    FOUNDERS = Semantic(
        id="founders",
        ref="schema:founders",
        text="""A person who founded this organization.""",
    )

    IMAGE_GALLERY = Semantic(
        id="ImageGallery",
        ref="schema:ImageGallery",
        text="""Web page type: Image gallery page.""",
    )

    TYPE_AND_QUANTITY_NODE = Semantic(
        id="TypeAndQuantityNode",
        ref="schema:TypeAndQuantityNode",
        text="""A structured value indicating the quantity, unit of measurement, and business function of goods included in a bundle offer.""",
    )

    IN_CH_I = Semantic(
        id="inChI",
        ref="schema:inChI",
        text="""Non-proprietary identifier for molecular entity that can be used in printed and electronic data sources thus enabling easier linking of diverse data compilations.""",
    )

    GEO_WITHIN = Semantic(
        id="geoWithin",
        ref="schema:geoWithin",
        text="""Represents a relationship between two geometries (or the places they represent), relating a geometry to one that contains it, i.e. it is inside (i.e. within) its interior. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).""",
    )

    REQUIREMENTS = Semantic(
        id="requirements",
        ref="schema:requirements",
        text="""Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (Examples: DirectX, Java or .NET runtime).""",
    )

    ADULT_ENTERTAINMENT = Semantic(
        id="AdultEntertainment",
        ref="schema:AdultEntertainment",
        text="""An adult entertainment establishment.""",
    )

    TARGET_URL = Semantic(
        id="targetUrl",
        ref="schema:targetUrl",
        text="""The URL of a node in an established educational framework.""",
    )

    ADDITIONAL_NAME = Semantic(
        id="additionalName",
        ref="schema:additionalName",
        text="""An additional name for a Person, can be used for a middle name.""",
    )

    FOLLOWS = Semantic(
        id="follows",
        ref="schema:follows",
        text="""The most generic uni-directional social relation.""",
    )

    MOTORCYCLE_REPAIR = Semantic(
        id="MotorcycleRepair",
        ref="schema:MotorcycleRepair",
        text="""A motorcycle repair shop.""",
    )

    WEARABLE_MEASUREMENT_SLEEVE = Semantic(
        id="WearableMeasurementSleeve",
        ref="schema:WearableMeasurementSleeve",
        text="""Measurement of the sleeve length, for example of a shirt""",
    )

    APPLIES_TO_PAYMENT_METHOD = Semantic(
        id="appliesToPaymentMethod",
        ref="schema:appliesToPaymentMethod",
        text="""The payment method(s) to which the payment charge specification applies.""",
    )

    RSVP_RESPONSE_YES = Semantic(
        id="RsvpResponseYes",
        ref="schema:RsvpResponseYes",
        text="""The invitee will attend.""",
    )

    TISSUE_SAMPLE = Semantic(
        id="tissueSample",
        ref="schema:tissueSample",
        text="""The type of tissue sample required for the test.""",
    )

    GEO_INTERSECTS = Semantic(
        id="geoIntersects",
        ref="schema:geoIntersects",
        text="""Represents spatial relations in which two geometries (or the places they represent) have at least one point in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).""",
    )

    SUPPORTING_DATA = Semantic(
        id="supportingData",
        ref="schema:supportingData",
        text="""Supporting data for a SoftwareApplication.""",
    )

    COMMENT_ACTION = Semantic(
        id="CommentAction",
        ref="schema:CommentAction",
        text="""The act of generating a comment about a subject.""",
    )

    CITY = Semantic(id="City", ref="schema:City", text="""A city or town.""")

    INTERNET_CAFE = Semantic(
        id="InternetCafe", ref="schema:InternetCafe", text="""An internet cafe."""
    )

    ABSTRACT = Semantic(
        id="abstract",
        ref="schema:abstract",
        text="""An abstract is a short description that summarizes a [[CreativeWork]].""",
    )

    TOOL = Semantic(
        id="tool",
        ref="schema:tool",
        text="""A sub property of instrument. An object used (but not consumed) when performing instructions or a direction.""",
    )

    PREVENTION_HEALTH_ASPECT = Semantic(
        id="PreventionHealthAspect",
        ref="schema:PreventionHealthAspect",
        text="""Information about actions or measures that can be taken to avoid getting the topic or reaching a critical situation related to the topic.""",
    )

    RENAL = Semantic(
        id="Renal",
        ref="schema:Renal",
        text="""A specific branch of medical science that pertains to the study of the kidneys and its respective disease states.""",
    )

    NUMBER_OF_PAGES = Semantic(
        id="numberOfPages",
        ref="schema:numberOfPages",
        text="""The number of pages in the book.""",
    )

    TREATMENTS_HEALTH_ASPECT = Semantic(
        id="TreatmentsHealthAspect",
        ref="schema:TreatmentsHealthAspect",
        text="""Treatments or related therapies for a Topic.""",
    )

    FESTIVAL = Semantic(
        id="Festival", ref="schema:Festival", text="""Event type: Festival."""
    )

    LOGO = Semantic(id="logo", ref="schema:logo", text="""An associated logo.""")

    MPN = Semantic(
        id="mpn",
        ref="schema:mpn",
        text="""The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.""",
    )

    VALID_UNTIL = Semantic(
        id="validUntil",
        ref="schema:validUntil",
        text="""The date when the item is no longer valid.""",
    )

    GEO_COORDINATES = Semantic(
        id="GeoCoordinates",
        ref="schema:GeoCoordinates",
        text="""The geographic coordinates of a place or event.""",
    )

    VEGETARIAN_DIET = Semantic(
        id="VegetarianDiet",
        ref="schema:VegetarianDiet",
        text="""A diet exclusive of animal meat.""",
    )

    REPAYMENT_SPECIFICATION = Semantic(
        id="RepaymentSpecification",
        ref="schema:RepaymentSpecification",
        text="""A structured value representing repayment.""",
    )

    DEATH_DATE = Semantic(
        id="deathDate", ref="schema:deathDate", text="""Date of death."""
    )

    MOTEL = Semantic(
        id="Motel",
        ref="schema:Motel",
        text="""A motel.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
""",
    )

    LEGISLATION_RESPONSIBLE = Semantic(
        id="legislationResponsible",
        ref="schema:legislationResponsible",
        text="""An individual or organization that has some kind of responsibility for the legislation. Typically the ministry who is/was in charge of elaborating the legislation, or the adressee for potential questions about the legislation once it is published.""",
    )

    CASE_SERIES = Semantic(
        id="CaseSeries",
        ref="schema:CaseSeries",
        text="""A case series (also known as a clinical series) is a medical research study that tracks patients with a known exposure given similar treatment or examines their medical records for exposure and outcome. A case series can be retrospective or prospective and usually involves a smaller number of patients than the more powerful case-control studies or randomized controlled trials. Case series may be consecutive or non-consecutive, depending on whether all cases presenting to the reporting authors over a period of time were included, or only a selection.""",
    )

    REPORTAGE_NEWS_ARTICLE = Semantic(
        id="ReportageNewsArticle",
        ref="schema:ReportageNewsArticle",
        text="""The [[ReportageNewsArticle]] type is a subtype of [[NewsArticle]] representing
 news articles which are the result of journalistic news reporting conventions.

In practice many news publishers produce a wide variety of article types, many of which might be considered a [[NewsArticle]] but not a [[ReportageNewsArticle]]. For example, opinion pieces, reviews, analysis, sponsored or satirical articles, or articles that combine several of these elements.

The [[ReportageNewsArticle]] type is based on a stricter ideal for "news" as a work of journalism, with articles based on factual information either observed or verified by the author, or reported and verified from knowledgeable sources.  This often includes perspectives from multiple viewpoints on a particular issue (distinguishing news reports from public relations or propaganda).  News reports in the [[ReportageNewsArticle]] sense de-emphasize the opinion of the author, with commentary and value judgements typically expressed elsewhere.

A [[ReportageNewsArticle]] which goes deeper into analysis can also be marked with an additional type of [[AnalysisNewsArticle]].
""",
    )

    OCCUPANCY = Semantic(
        id="occupancy",
        ref="schema:occupancy",
        text="""The allowed total occupancy for the accommodation in persons (including infants etc). For individual accommodations, this is not necessarily the legal maximum but defines the permitted usage as per the contractual agreement (e.g. a double room used by a single person).
Typical unit code(s): C62 for person""",
    )

    MEMBERS = Semantic(
        id="members", ref="schema:members", text="""A member of this organization."""
    )

    RESULT_COMMENT = Semantic(
        id="resultComment",
        ref="schema:resultComment",
        text="""A sub property of result. The Comment created or sent as a result of this action.""",
    )

    OPTOMETRIC = Semantic(
        id="Optometric",
        ref="schema:Optometric",
        text="""The science or practice of testing visual acuity and prescribing corrective lenses.""",
    )

    EVENT_RESERVATION = Semantic(
        id="EventReservation",
        ref="schema:EventReservation",
        text="""A reservation for an event like a concert, sporting event, or lecture.\\n\\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].""",
    )

    QUOTE_ACTION = Semantic(
        id="QuoteAction",
        ref="schema:QuoteAction",
        text="""An agent quotes/estimates/appraises an object/product/service with a price at a location/store.""",
    )

    PUBLICATION_VOLUME = Semantic(
        id="PublicationVolume",
        ref="schema:PublicationVolume",
        text="""A part of a successively published publication such as a periodical or multi-volume work, often numbered. It may represent a time span, such as a year.\\n\\nSee also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).""",
    )

    HEALTH_PLAN_NETWORK_ID = Semantic(
        id="healthPlanNetworkId",
        ref="schema:healthPlanNetworkId",
        text="""Name or unique ID of network. (Networks are often reused across different insurance plans).""",
    )

    TOTAL_PRICE = Semantic(
        id="totalPrice",
        ref="schema:totalPrice",
        text="""The total price for the reservation or ticket, including applicable taxes, shipping, etc.\\n\\nUsage guidelines:\\n\\n* Use values from 0123456789 (Unicode \'DIGIT ZERO\' (U+0030) to \'DIGIT NINE\' (U+0039)) rather than superficially similiar Unicode symbols.\\n* Use \'.\' (Unicode \'FULL STOP\' (U+002E)) rather than \',\' to indicate a decimal point. Avoid using these symbols as a readability separator.""",
    )

    THUMBNAIL_URL = Semantic(
        id="thumbnailUrl",
        ref="schema:thumbnailUrl",
        text="""A thumbnail image relevant to the Thing.""",
    )

    R_V_PARK = Semantic(
        id="RVPark",
        ref="schema:RVPark",
        text="""A place offering space for "Recreational Vehicles", Caravans, mobile homes and the like.""",
    )

    EXPERT_CONSIDERATIONS = Semantic(
        id="expertConsiderations",
        ref="schema:expertConsiderations",
        text="""Medical expert advice related to the plan.""",
    )

    DOWNPAYMENT = Semantic(
        id="Downpayment",
        ref="schema:Downpayment",
        text="""Represents the downpayment (up-front payment) price component of the total price for an offered product that has additional installment payments.""",
    )

    STORE_CREDIT_REFUND = Semantic(
        id="StoreCreditRefund",
        ref="schema:StoreCreditRefund",
        text="""Specifies that the customer receives a store credit as refund when returning a product""",
    )

    RESULTS_AVAILABLE = Semantic(
        id="ResultsAvailable",
        ref="schema:ResultsAvailable",
        text="""Results are available.""",
    )

    COUNTRY_OF_LAST_PROCESSING = Semantic(
        id="countryOfLastProcessing",
        ref="schema:countryOfLastProcessing",
        text="""The place where the item (typically [[Product]]) was last processed and tested before importation.""",
    )

    OBSERVATION_DATE = Semantic(
        id="observationDate",
        ref="schema:observationDate",
        text="""The observationDate of an [[Observation]].""",
    )

    MISSION_COVERAGE_PRIORITIES_POLICY = Semantic(
        id="missionCoveragePrioritiesPolicy",
        ref="schema:missionCoveragePrioritiesPolicy",
        text="""For a [[NewsMediaOrganization]], a statement on coverage priorities, including any public agenda or stance on issues.""",
    )

    TOTAL_PAYMENT_DUE = Semantic(
        id="totalPaymentDue",
        ref="schema:totalPaymentDue",
        text="""The total amount due.""",
    )

    DESCRIPTION = Semantic(
        id="description",
        ref="schema:description",
        text="""A description of the item.""",
    )

    AGREE_ACTION = Semantic(
        id="AgreeAction",
        ref="schema:AgreeAction",
        text="""The act of expressing a consistency of opinion with the object. An agent agrees to/about an object (a proposition, topic or theme) with participants.""",
    )

    JEWELRY_STORE = Semantic(
        id="JewelryStore", ref="schema:JewelryStore", text="""A jewelry store."""
    )

    PRICE_TYPE = Semantic(
        id="priceType",
        ref="schema:priceType",
        text="""Defines the type of a price specified for an offered product, for example a list price, a (temporary) sale price or a manufacturer suggested retail price. If multiple prices are specified for an offer the [[priceType]] property can be used to identify the type of each such specified price. The value of priceType can be specified as a value from enumeration PriceTypeEnumeration or as a free form text string for price types that are not already predefined in PriceTypeEnumeration.""",
    )

    LIGAMENT = Semantic(
        id="Ligament",
        ref="schema:Ligament",
        text="""A short band of tough, flexible, fibrous connective tissue that functions to connect multiple bones, cartilages, and structurally support joints.""",
    )

    NUMBER_OF_FORWARD_GEARS = Semantic(
        id="numberOfForwardGears",
        ref="schema:numberOfForwardGears",
        text="""The total number of forward gears available for the transmission system of the vehicle.\\n\\nTypical unit code(s): C62""",
    )

    ANIMAL_SHELTER = Semantic(
        id="AnimalShelter", ref="schema:AnimalShelter", text="""Animal shelter."""
    )

    OVERDOSAGE = Semantic(
        id="overdosage",
        ref="schema:overdosage",
        text="""Any information related to overdose on a drug, including signs or symptoms, treatments, contact information for emergency response.""",
    )

    SPECIAL_ANNOUNCEMENT = Semantic(
        id="SpecialAnnouncement",
        ref="schema:SpecialAnnouncement",
        text="""A SpecialAnnouncement combines a simple date-stamped textual information update
      with contextualized Web links and other structured data.  It represents an information update made by a
      locally-oriented organization, for example schools, pharmacies, healthcare providers,  community groups, police,
      local government.

For work in progress guidelines on Coronavirus-related markup see [this doc](https://docs.google.com/document/d/14ikaGCKxo50rRM7nvKSlbUpjyIk2WMQd3IkB1lItlrM/edit#).

The motivating scenario for SpecialAnnouncement is the [Coronavirus pandemic](https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic), and the initial vocabulary is oriented to this urgent situation. Schema.org
expect to improve the markup iteratively as it is deployed and as feedback emerges from use. In addition to our
usual [Github entry](https://github.com/schemaorg/schemaorg/issues/2490), feedback comments can also be provided in [this document](https://docs.google.com/document/d/1fpdFFxk8s87CWwACs53SGkYv3aafSxz_DTtOQxMrBJQ/edit#).


While this schema is designed to communicate urgent crisis-related information, it is not the same as an emergency warning technology like [CAP](https://en.wikipedia.org/wiki/Common_Alerting_Protocol), although there may be overlaps. The intent is to cover
the kinds of everyday practical information being posted to existing websites during an emergency situation.

Several kinds of information can be provided:

We encourage the provision of "name", "text", "datePosted", "expires" (if appropriate), "category" and
"url" as a simple baseline. It is important to provide a value for "category" where possible, most ideally as a well known
URL from Wikipedia or Wikidata. In the case of the 2019-2020 Coronavirus pandemic, this should be "https://en.wikipedia.org/w/index.php?title=2019-20\\_coronavirus\\_pandemic" or "https://www.wikidata.org/wiki/Q81068910".

For many of the possible properties, values can either be simple links or an inline description, depending on whether a summary is available. For a link, provide just the URL of the appropriate page as the property\'s value. For an inline description, use a [[WebContent]] type, and provide the url as a property of that, alongside at least a simple "[[text]]" summary of the page. It is
unlikely that a single SpecialAnnouncement will need all of the possible properties simultaneously.

We expect that in many cases the page referenced might contain more specialized structured data, e.g. contact info, [[openingHours]], [[Event]], [[FAQPage]] etc. By linking to those pages from a [[SpecialAnnouncement]] you can help make it clearer that the events are related to the situation (e.g. Coronavirus) indicated by the [[category]] property of the [[SpecialAnnouncement]].

Many [[SpecialAnnouncement]]s will relate to particular regions and to identifiable local organizations. Use [[spatialCoverage]] for the region, and [[announcementLocation]] to indicate specific [[LocalBusiness]]es and [[CivicStructure]]s. If the announcement affects both a particular region and a specific location (for example, a library closure that serves an entire region), use both [[spatialCoverage]] and [[announcementLocation]].

The [[about]] property can be used to indicate entities that are the focus of the announcement. We now recommend using [[about]] only
for representing non-location entities (e.g. a [[Course]] or a [[RadioStation]]). For places, use [[announcementLocation]] and [[spatialCoverage]]. Consumers of this markup should be aware that the initial design encouraged the use of /about for locations too.

The basic content of [[SpecialAnnouncement]] is similar to that of an [RSS](https://en.wikipedia.org/wiki/RSS) or [Atom](https://en.wikipedia.org/wiki/Atom_(Web_standard)) feed. For publishers without such feeds, basic feed-like information can be shared by posting
[[SpecialAnnouncement]] updates in a page, e.g. using JSON-LD. For sites with Atom/RSS functionality, you can point to a feed
with the [[webFeed]] property. This can be a simple URL, or an inline [[DataFeed]] object, with [[encodingFormat]] providing
media type information e.g. "application/rss+xml" or "application/atom+xml".
""",
    )

    CVD_NUM_I_C_U_BEDS = Semantic(
        id="cvdNumICUBeds",
        ref="schema:cvdNumICUBeds",
        text="""numicubeds - ICU BEDS: Total number of staffed inpatient intensive care unit (ICU) beds.""",
    )

    FOUNDING_DATE = Semantic(
        id="foundingDate",
        ref="schema:foundingDate",
        text="""The date that this organization was founded.""",
    )

    TRANSIT_MAP = Semantic(
        id="TransitMap", ref="schema:TransitMap", text="""A transit map."""
    )

    RETURN_ACTION = Semantic(
        id="ReturnAction",
        ref="schema:ReturnAction",
        text="""The act of returning to the origin that which was previously received (concrete objects) or taken (ownership).""",
    )

    RETURN_POLICY_CATEGORY = Semantic(
        id="returnPolicyCategory",
        ref="schema:returnPolicyCategory",
        text="""Specifies an applicable return policy (from an enumeration).""",
    )

    SAMPLE_TYPE = Semantic(
        id="sampleType",
        ref="schema:sampleType",
        text="""What type of code sample: full (compile ready) solution, code snippet, inline code, scripts, template.""",
    )

    HARDCOVER = Semantic(
        id="Hardcover", ref="schema:Hardcover", text="""Book format: Hardcover."""
    )

    POST_OFFICE_BOX_NUMBER = Semantic(
        id="postOfficeBoxNumber",
        ref="schema:postOfficeBoxNumber",
        text="""The post office box number for PO box addresses.""",
    )

    ATLAS = Semantic(
        id="Atlas",
        ref="schema:Atlas",
        text="""A collection or bound volume of maps, charts, plates or tables, physical or in media form illustrating any subject.""",
    )

    PETS_ALLOWED = Semantic(
        id="petsAllowed",
        ref="schema:petsAllowed",
        text="""Indicates whether pets are allowed to enter the accommodation or lodging business. More detailed information can be put in a text value.""",
    )

    ACQUIRE_LICENSE_PAGE = Semantic(
        id="acquireLicensePage",
        ref="schema:acquireLicensePage",
        text="""Indicates a page documenting how licenses can be purchased or otherwise acquired, for the current item.""",
    )

    CONTENT_RATING = Semantic(
        id="contentRating",
        ref="schema:contentRating",
        text="""Official rating of a piece of content&#x2014;for example,\'MPAA PG-13\'.""",
    )

    MERCHANT_RETURN_ENUMERATION = Semantic(
        id="MerchantReturnEnumeration",
        ref="schema:MerchantReturnEnumeration",
        text="""Enumerates several kinds of product return policies.""",
    )

    DRAWING = Semantic(
        id="Drawing",
        ref="schema:Drawing",
        text="""A picture or diagram made with a pencil, pen, or crayon rather than paint.""",
    )

    PERMISSION_TYPE = Semantic(
        id="permissionType",
        ref="schema:permissionType",
        text="""The type of permission granted the person, organization, or audience.""",
    )

    F_D_ACATEGORY_A = Semantic(
        id="FDAcategoryA",
        ref="schema:FDAcategoryA",
        text="""A designation by the US FDA signifying that adequate and well-controlled studies have failed to demonstrate a risk to the fetus in the first trimester of pregnancy (and there is no evidence of risk in later trimesters).""",
    )

    NUMBER_OF_ITEMS = Semantic(
        id="numberOfItems",
        ref="schema:numberOfItems",
        text="""The number of items in an ItemList. Note that some descriptions might not fully describe all items in a list (e.g., multi-page pagination); in such cases, the numberOfItems would be for the entire list.""",
    )

    ART_MEDIUM = Semantic(
        id="artMedium",
        ref="schema:artMedium",
        text="""The material used. (e.g. Oil, Watercolour, Acrylic, Linoprint, Marble, Cyanotype, Digital, Lithograph, DryPoint, Intaglio, Pastel, Woodcut, Pencil, Mixed Media, etc.)""",
    )

    MIN_PRICE = Semantic(
        id="minPrice",
        ref="schema:minPrice",
        text="""The lowest price if the price is a range.""",
    )

    LEGISLATION_LEGAL_VALUE = Semantic(
        id="legislationLegalValue",
        ref="schema:legislationLegalValue",
        text="""The legal value of this legislation file. The same legislation can be written in multiple files with different legal values. Typically a digitally signed PDF have a "stronger" legal value than the HTML file of the same act.""",
    )

    AWARDS = Semantic(
        id="awards", ref="schema:awards", text="""Awards won by or for this item."""
    )

    WORKLOAD = Semantic(
        id="workload",
        ref="schema:workload",
        text="""Quantitative measure of the physiologic output of the exercise; also referred to as energy expenditure.""",
    )

    ENCODES_BIO_CHEM_ENTITY = Semantic(
        id="encodesBioChemEntity",
        ref="schema:encodesBioChemEntity",
        text="""Another BioChemEntity encoded by this one. """,
    )

    EVENT_POSTPONED = Semantic(
        id="EventPostponed",
        ref="schema:EventPostponed",
        text="""The event has been postponed and no new date has been set. The event\'s previousStartDate should be set.""",
    )

    AUTHENTICATOR = Semantic(
        id="authenticator",
        ref="schema:authenticator",
        text="""The Organization responsible for authenticating the user\'s subscription. For example, many media apps require a cable/satellite provider to authenticate your subscription before playing media.""",
    )

    CHEMICAL_SUBSTANCE = Semantic(
        id="ChemicalSubstance",
        ref="schema:ChemicalSubstance",
        text="""A chemical substance is \'a portion of matter of constant composition, composed of molecular entities of the same type or of different types\' (source: [ChEBI:59999](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=59999)).""",
    )

    NUM_ADULTS = Semantic(
        id="numAdults",
        ref="schema:numAdults",
        text="""The number of adults staying in the unit.""",
    )

    ORDER_ITEM_NUMBER = Semantic(
        id="orderItemNumber",
        ref="schema:orderItemNumber",
        text="""The identifier of the order item.""",
    )

    RESTAURANT = Semantic(
        id="Restaurant", ref="schema:Restaurant", text="""A restaurant."""
    )

    PRODUCT_GROUP = Semantic(
        id="ProductGroup",
        ref="schema:ProductGroup",
        text="""A ProductGroup represents a group of [[Product]]s that vary only in certain well-described ways, such as by [[size]], [[color]], [[material]] etc.

While a ProductGroup itself is not directly offered for sale, the various varying products that it represents can be. The ProductGroup serves as a prototype or template, standing in for all of the products who have an [[isVariantOf]] relationship to it. As such, properties (including additional types) can be applied to the ProductGroup to represent characteristics shared by each of the (possibly very many) variants. Properties that reference a ProductGroup are not included in this mechanism; neither are the following specific properties [[variesBy]], [[hasVariant]], [[url]]. """,
    )

    POSTAL_CODE_END = Semantic(
        id="postalCodeEnd",
        ref="schema:postalCodeEnd",
        text="""Last postal code in the range (included). Needs to be after [[postalCodeBegin]].""",
    )

    SHIPPING_DELIVERY_TIME = Semantic(
        id="ShippingDeliveryTime",
        ref="schema:ShippingDeliveryTime",
        text="""ShippingDeliveryTime provides various pieces of information about delivery times for shipping.""",
    )

    MAKES_OFFER = Semantic(
        id="makesOffer",
        ref="schema:makesOffer",
        text="""A pointer to products or services offered by the organization or person.""",
    )

    NUMBER_OF_AIRBAGS = Semantic(
        id="numberOfAirbags",
        ref="schema:numberOfAirbags",
        text="""The number or type of airbags in the vehicle.""",
    )

    IS_FAMILY_FRIENDLY = Semantic(
        id="isFamilyFriendly",
        ref="schema:isFamilyFriendly",
        text="""Indicates whether this content is family friendly.""",
    )

    ADVERSE_OUTCOME = Semantic(
        id="adverseOutcome",
        ref="schema:adverseOutcome",
        text="""A possible complication and/or side effect of this therapy. If it is known that an adverse outcome is serious (resulting in death, disability, or permanent damage; requiring hospitalization; or is otherwise life-threatening or requires immediate medical attention), tag it as a seriouseAdverseOutcome instead.""",
    )

    WEARABLE_SIZE_GROUP_SHORT = Semantic(
        id="WearableSizeGroupShort",
        ref="schema:WearableSizeGroupShort",
        text="""Size group "Short" for wearables.""",
    )

    TABLE = Semantic(id="Table", ref="schema:Table", text="""A table on a Web page.""")

    PART_OF_SERIES = Semantic(
        id="partOfSeries",
        ref="schema:partOfSeries",
        text="""The series to which this episode or season belongs.""",
    )

    ARTIST = Semantic(
        id="artist",
        ref="schema:artist",
        text="""The primary artist for a work
    	in a medium other than pencils or digital line art--for example, if the
    	primary artwork is done in watercolors or digital paints.""",
    )

    EDITOR = Semantic(
        id="editor",
        ref="schema:editor",
        text="""Specifies the Person who edited the CreativeWork.""",
    )

    ENCODES_CREATIVE_WORK = Semantic(
        id="encodesCreativeWork",
        ref="schema:encodesCreativeWork",
        text="""The CreativeWork encoded by this media object.""",
    )

    ACTIVE_NOT_RECRUITING = Semantic(
        id="ActiveNotRecruiting",
        ref="schema:ActiveNotRecruiting",
        text="""Active, but not recruiting new participants.""",
    )

    PART_OF_INVOICE = Semantic(
        id="partOfInvoice",
        ref="schema:partOfInvoice",
        text="""The order is being paid as part of the referenced Invoice.""",
    )

    DRUG_PRESCRIPTION_STATUS = Semantic(
        id="DrugPrescriptionStatus",
        ref="schema:DrugPrescriptionStatus",
        text="""Indicates whether this drug is available by prescription or over-the-counter.""",
    )

    DATE_PUBLISHED = Semantic(
        id="datePublished",
        ref="schema:datePublished",
        text="""Date of first broadcast/publication.""",
    )

    OWNED_THROUGH = Semantic(
        id="ownedThrough",
        ref="schema:ownedThrough",
        text="""The date and time of giving up ownership on the product.""",
    )

    CAR_USAGE_TYPE = Semantic(
        id="CarUsageType",
        ref="schema:CarUsageType",
        text="""A value indicating a special usage of a car, e.g. commercial rental, driving school, or as a taxi.""",
    )

    M_R_I = Semantic(id="MRI", ref="schema:MRI", text="""Magnetic resonance imaging.""")

    M_S_R_P = Semantic(
        id="MSRP",
        ref="schema:MSRP",
        text="""Represents the manufacturer suggested retail price ("MSRP") of an offered product.""",
    )

    SOUNDTRACK_ALBUM = Semantic(
        id="SoundtrackAlbum", ref="schema:SoundtrackAlbum", text="""SoundtrackAlbum."""
    )

    TAXONOMIC_RANGE = Semantic(
        id="taxonomicRange",
        ref="schema:taxonomicRange",
        text="""The taxonomic grouping of the organism that expresses, encodes, or in someway related to the BioChemEntity.""",
    )

    PAYMENT_DUE_DATE = Semantic(
        id="paymentDueDate",
        ref="schema:paymentDueDate",
        text="""The date that payment is due.""",
    )

    SPORTS_ACTIVITY_LOCATION = Semantic(
        id="sportsActivityLocation",
        ref="schema:sportsActivityLocation",
        text="""A sub property of location. The sports activity location where this action occurred.""",
    )

    INCLUDES_HEALTH_PLAN_NETWORK = Semantic(
        id="includesHealthPlanNetwork",
        ref="schema:includesHealthPlanNetwork",
        text="""Networks covered by this plan.""",
    )

    BORROW_ACTION = Semantic(
        id="BorrowAction",
        ref="schema:BorrowAction",
        text="""The act of obtaining an object under an agreement to return it at a later date. Reciprocal of LendAction.\\n\\nRelated actions:\\n\\n* [[LendAction]]: Reciprocal of BorrowAction.""",
    )

    INCLUDED_IN_HEALTH_INSURANCE_PLAN = Semantic(
        id="includedInHealthInsurancePlan",
        ref="schema:includedInHealthInsurancePlan",
        text="""The insurance plans that cover this drug.""",
    )

    GTIN12 = Semantic(
        id="gtin12",
        ref="schema:gtin12",
        text="""The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.""",
    )

    MODEL_DATE = Semantic(
        id="modelDate",
        ref="schema:modelDate",
        text="""The release date of a vehicle model (often used to differentiate versions of the same make and model).""",
    )

    CVD_NUM_C19_O_F_MECH_VENT_PATS = Semantic(
        id="cvdNumC19OFMechVentPats",
        ref="schema:cvdNumC19OFMechVentPats",
        text="""numc19ofmechventpats - ED/OVERFLOW and VENTILATED: Patients with suspected or confirmed COVID-19 who are in the ED or any overflow location awaiting an inpatient bed and on a mechanical ventilator.""",
    )

    REVIEW_NEWS_ARTICLE = Semantic(
        id="ReviewNewsArticle",
        ref="schema:ReviewNewsArticle",
        text="""A [[NewsArticle]] and [[CriticReview]] providing a professional critic\'s assessment of a service, product, performance, or artistic or literary work.""",
    )

    HOTEL_ROOM = Semantic(
        id="HotelRoom",
        ref="schema:HotelRoom",
        text="""A hotel room is a single room in a hotel.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
""",
    )

    WEARABLE_MEASUREMENT_WAIST = Semantic(
        id="WearableMeasurementWaist",
        ref="schema:WearableMeasurementWaist",
        text="""Measurement of the waist section, for example of pants""",
    )

    HAS_DELIVERY_METHOD = Semantic(
        id="hasDeliveryMethod",
        ref="schema:hasDeliveryMethod",
        text="""Method used for delivery or shipping.""",
    )

    DEPARTURE_BOAT_TERMINAL = Semantic(
        id="departureBoatTerminal",
        ref="schema:departureBoatTerminal",
        text="""The terminal or port from which the boat departs.""",
    )

    ISWC_CODE = Semantic(
        id="iswcCode",
        ref="schema:iswcCode",
        text="""The International Standard Musical Work Code for the composition.""",
    )

    ARCHIVE_ORGANIZATION = Semantic(
        id="ArchiveOrganization",
        ref="schema:ArchiveOrganization",
        text="""An organization with archival holdings. An organization which keeps and preserves archival material and typically makes it accessible to the public.""",
    )

    LIVE_BLOG_UPDATE = Semantic(
        id="liveBlogUpdate",
        ref="schema:liveBlogUpdate",
        text="""An update to the LiveBlog.""",
    )

    ASSOCIATED_ARTICLE = Semantic(
        id="associatedArticle",
        ref="schema:associatedArticle",
        text="""A NewsArticle associated with the Media Object.""",
    )

    CLAIM = Semantic(
        id="Claim",
        ref="schema:Claim",
        text="""A [[Claim]] in Schema.org represents a specific, factually-oriented claim that could be the [[itemReviewed]] in a [[ClaimReview]]. The content of a claim can be summarized with the [[text]] property. Variations on well known claims can have their common identity indicated via [[sameAs]] links, and summarized with a [[name]]. Ideally, a [[Claim]] description includes enough contextual information to minimize the risk of ambiguity or inclarity. In practice, many claims are better understood in the context in which they appear or the interpretations provided by claim reviews.

  Beyond [[ClaimReview]], the Claim type can be associated with related creative works - for example a [[ScholarlyArticle]] or [[Question]] might be [[about]] some [[Claim]].

  At this time, Schema.org does not define any types of relationship between claims. This is a natural area for future exploration.
  """,
    )

    PREVIOUS_ITEM = Semantic(
        id="previousItem",
        ref="schema:previousItem",
        text="""A link to the ListItem that preceeds the current one.""",
    )

    TYPE_OF_BED = Semantic(
        id="typeOfBed",
        ref="schema:typeOfBed",
        text="""The type of bed to which the BedDetail refers, i.e. the type of bed available in the quantity indicated by quantity.""",
    )

    PROGRAM_MEMBERSHIP = Semantic(
        id="ProgramMembership",
        ref="schema:ProgramMembership",
        text="""Used to describe membership in a loyalty programs (e.g. "StarAliance"), traveler clubs (e.g. "AAA"), purchase clubs ("Safeway Club"), etc.""",
    )

    EDUCATIONAL_LEVEL = Semantic(
        id="educationalLevel",
        ref="schema:educationalLevel",
        text="""The level in terms of progression through an educational or training context. Examples of educational levels include \'beginner\', \'intermediate\' or \'advanced\', and formal sets of level indicators.""",
    )

    AVAILABLE_AT_OR_FROM = Semantic(
        id="availableAtOrFrom",
        ref="schema:availableAtOrFrom",
        text="""The place(s) from which the offer can be obtained (e.g. store locations).""",
    )

    CSS_SELECTOR = Semantic(
        id="cssSelector",
        ref="schema:cssSelector",
        text="""A CSS selector, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".""",
    )

    PHYSICAL_ACTIVITY = Semantic(
        id="PhysicalActivity",
        ref="schema:PhysicalActivity",
        text="""Any bodily activity that enhances or maintains physical fitness and overall health and wellness. Includes activity that is part of daily living and routine, structured exercise, and exercise prescribed as part of a medical treatment or recovery plan.""",
    )

    ASSESSES = Semantic(
        id="assesses",
        ref="schema:assesses",
        text="""The item being described is intended to assess the competency or learning outcome defined by the referenced term.""",
    )

    WEB_FEED = Semantic(
        id="webFeed",
        ref="schema:webFeed",
        text="""The URL for a feed, e.g. associated with a podcast series, blog, or series of date-stamped updates. This is usually RSS or Atom.""",
    )

    CONTACT_POINT = Semantic(
        id="ContactPoint",
        ref="schema:ContactPoint",
        text="""A contact point&#x2014;for example, a Customer Complaints department.""",
    )

    BARCODE = Semantic(
        id="Barcode",
        ref="schema:Barcode",
        text="""An image of a visual machine-readable code such as a barcode or QR code.""",
    )

    CONTRAINDICATION = Semantic(
        id="contraindication",
        ref="schema:contraindication",
        text="""A contraindication for this therapy.""",
    )

    BROADCAST_SERVICE = Semantic(
        id="BroadcastService",
        ref="schema:BroadcastService",
        text="""A delivery service through which content is provided via broadcast over the air or online.""",
    )

    CHARACTER_ATTRIBUTE = Semantic(
        id="characterAttribute",
        ref="schema:characterAttribute",
        text="""A piece of data that represents a particular aspect of a fictional character (skill, power, character points, advantage, disadvantage).""",
    )

    NONPROFIT501A = Semantic(
        id="Nonprofit501a",
        ref="schema:Nonprofit501a",
        text="""Nonprofit501a: Non-profit type referring to Farmers’ Cooperative Associations.""",
    )

    LEGISLATION_JURISDICTION = Semantic(
        id="legislationJurisdiction",
        ref="schema:legislationJurisdiction",
        text="""The jurisdiction from which the legislation originates.""",
    )

    CARRIER_REQUIREMENTS = Semantic(
        id="carrierRequirements",
        ref="schema:carrierRequirements",
        text="""Specifies specific carrier(s) requirements for the application (e.g. an application may only work on a specific carrier network).""",
    )

    WEARABLE_SIZE_SYSTEM_J_P = Semantic(
        id="WearableSizeSystemJP",
        ref="schema:WearableSizeSystemJP",
        text="""Japanese size system for wearables.""",
    )

    DATED_MONEY_SPECIFICATION = Semantic(
        id="DatedMoneySpecification",
        ref="schema:DatedMoneySpecification",
        text="""A DatedMoneySpecification represents monetary values with optional start and end dates. For example, this could represent an employee\'s salary over a specific period of time. __Note:__ This type has been superseded by [[MonetaryAmount]] use of that type is recommended""",
    )

    REPORT_NUMBER = Semantic(
        id="reportNumber",
        ref="schema:reportNumber",
        text="""The number or other unique designator assigned to a Report by the publishing organization.""",
    )

    CHEAT_CODE = Semantic(
        id="cheatCode", ref="schema:cheatCode", text="""Cheat codes to the game."""
    )

    ON_DEMAND_EVENT = Semantic(
        id="OnDemandEvent",
        ref="schema:OnDemandEvent",
        text="""A publication event e.g. catch-up TV or radio podcast, during which a program is available on-demand.""",
    )

    ART_GALLERY = Semantic(
        id="ArtGallery", ref="schema:ArtGallery", text="""An art gallery."""
    )

    ORDER_ITEM = Semantic(
        id="OrderItem",
        ref="schema:OrderItem",
        text="""An order item is a line of an order. It includes the quantity and shipping details of a bought offer.""",
    )

    HOW_TO_SUPPLY = Semantic(
        id="HowToSupply",
        ref="schema:HowToSupply",
        text="""A supply consumed when performing the instructions for how to achieve a result.""",
    )

    SHOPPING_CENTER = Semantic(
        id="ShoppingCenter",
        ref="schema:ShoppingCenter",
        text="""A shopping center or mall.""",
    )

    SUNDAY = Semantic(
        id="Sunday",
        ref="schema:Sunday",
        text="""The day of the week between Saturday and Monday.""",
    )

    REPEAT_FREQUENCY = Semantic(
        id="repeatFrequency",
        ref="schema:repeatFrequency",
        text="""Defines the frequency at which [[Event]]s will occur according to a schedule [[Schedule]]. The intervals between
      events should be defined as a [[Duration]] of time.""",
    )

    PSYCHOLOGICAL_TREATMENT = Semantic(
        id="PsychologicalTreatment",
        ref="schema:PsychologicalTreatment",
        text="""A process of care relying upon counseling, dialogue and communication  aimed at improving a mental health condition without use of drugs.""",
    )

    GAME = Semantic(
        id="game",
        ref="schema:game",
        text="""Video game which is played on this server.""",
    )

    DOUBLE_BLINDED_TRIAL = Semantic(
        id="DoubleBlindedTrial",
        ref="schema:DoubleBlindedTrial",
        text="""A trial design in which neither the researcher nor the patient knows the details of the treatment the patient was randomly assigned to.""",
    )

    SUB_STRUCTURE = Semantic(
        id="subStructure",
        ref="schema:subStructure",
        text="""Component (sub-)structure(s) that comprise this anatomical structure.""",
    )

    BILLING_DURATION = Semantic(
        id="billingDuration",
        ref="schema:billingDuration",
        text="""Specifies for how long this price (or price component) will be billed. Can be used, for example, to model the contractual duration of a subscription or payment plan. Type can be either a Duration or a Number (in which case the unit of measurement, for example month, is specified by the unitCode property).""",
    )

    ATHLETE = Semantic(
        id="athlete",
        ref="schema:athlete",
        text="""A person that acts as performing member of a sports team; a player as opposed to a coach.""",
    )

    ORDER_STATUS = Semantic(
        id="OrderStatus",
        ref="schema:OrderStatus",
        text="""Enumerated status values for Order.""",
    )

    ALBUMS = Semantic(
        id="albums", ref="schema:albums", text="""A collection of music albums."""
    )

    SCHEDULED_PAYMENT_DATE = Semantic(
        id="scheduledPaymentDate",
        ref="schema:scheduledPaymentDate",
        text="""The date the invoice is scheduled to be paid.""",
    )

    MAIN_ENTITY = Semantic(
        id="mainEntity",
        ref="schema:mainEntity",
        text="""Indicates the primary entity described in some page or other CreativeWork.""",
    )

    PRINT_EDITION = Semantic(
        id="printEdition",
        ref="schema:printEdition",
        text="""The edition of the print product in which the NewsArticle appears.""",
    )

    CREDITED_TO = Semantic(
        id="creditedTo",
        ref="schema:creditedTo",
        text="""The group the release is credited to if different than the byArtist. For example, Red and Blue is credited to "Stefani Germanotta Band", but by Lady Gaga.""",
    )

    STUDY_SUBJECT = Semantic(
        id="studySubject",
        ref="schema:studySubject",
        text="""A subject of the study, i.e. one of the medical conditions, therapies, devices, drugs, etc. investigated by the study.""",
    )

    BROADCAST_TIMEZONE = Semantic(
        id="broadcastTimezone",
        ref="schema:broadcastTimezone",
        text="""The timezone in [ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601) for which the service bases its broadcasts""",
    )

    WIDTH = Semantic(id="width", ref="schema:width", text="""The width of the item.""")

    GIVE_ACTION = Semantic(
        id="GiveAction",
        ref="schema:GiveAction",
        text="""The act of transferring ownership of an object to a destination. Reciprocal of TakeAction.\\n\\nRelated actions:\\n\\n* [[TakeAction]]: Reciprocal of GiveAction.\\n* [[SendAction]]: Unlike SendAction, GiveAction implies that ownership is being transferred (e.g. I may send my laptop to you, but that doesn\'t mean I\'m giving it to you).""",
    )

    RESEARCH_ORGANIZATION = Semantic(
        id="ResearchOrganization",
        ref="schema:ResearchOrganization",
        text="""A Research Organization (e.g. scientific institute, research company).""",
    )

    C_T = Semantic(
        id="CT", ref="schema:CT", text="""X-ray computed tomography imaging."""
    )

    ENDORSEMENT_RATING = Semantic(
        id="EndorsementRating",
        ref="schema:EndorsementRating",
        text="""An EndorsementRating is a rating that expresses some level of endorsement, for example inclusion in a "critic\'s pick" blog, a
"Like" or "+1" on a social network. It can be considered the [[result]] of an [[EndorseAction]] in which the [[object]] of the action is rated positively by
some [[agent]]. As is common elsewhere in schema.org, it is sometimes more useful to describe the results of such an action without explicitly describing the [[Action]].

An [[EndorsementRating]] may be part of a numeric scale or organized system, but this is not required: having an explicit type for indicating a positive,
endorsement rating is particularly useful in the absence of numeric scales as it helps consumers understand that the rating is broadly positive.
""",
    )

    RIVER_BODY_OF_WATER = Semantic(
        id="RiverBodyOfWater",
        ref="schema:RiverBodyOfWater",
        text="""A river (for example, the broad majestic Shannon).""",
    )

    TOURIST_INFORMATION_CENTER = Semantic(
        id="TouristInformationCenter",
        ref="schema:TouristInformationCenter",
        text="""A tourist information center.""",
    )

    CIRCLE = Semantic(
        id="circle",
        ref="schema:circle",
        text="""A circle is the circular region of a specified radius centered at a specified latitude and longitude. A circle is expressed as a pair followed by a radius in meters.""",
    )

    CORRECTION = Semantic(
        id="correction",
        ref="schema:correction",
        text="""Indicates a correction to a [[CreativeWork]], either via a [[CorrectionComment]], textually or in another document.""",
    )

    ADDITIONAL_VARIABLE = Semantic(
        id="additionalVariable",
        ref="schema:additionalVariable",
        text="""Any additional component of the exercise prescription that may need to be articulated to the patient. This may include the order of exercises, the number of repetitions of movement, quantitative distance, progressions over time, etc.""",
    )

    BOOK_FORMAT_TYPE = Semantic(
        id="BookFormatType",
        ref="schema:BookFormatType",
        text="""The publication format of the book.""",
    )

    TIME_REQUIRED = Semantic(
        id="timeRequired",
        ref="schema:timeRequired",
        text="""Approximate or typical time it takes to work with or through this learning resource for the typical intended target audience, e.g. \'PT30M\', \'PT1H25M\'.""",
    )

    HAS_BROADCAST_CHANNEL = Semantic(
        id="hasBroadcastChannel",
        ref="schema:hasBroadcastChannel",
        text="""A broadcast channel of a broadcast service.""",
    )

    MUSIC_GROUP_MEMBER = Semantic(
        id="musicGroupMember",
        ref="schema:musicGroupMember",
        text="""A member of a music group&#x2014;for example, John, Paul, George, or Ringo.""",
    )

    HOUSE_PAINTER = Semantic(
        id="HousePainter",
        ref="schema:HousePainter",
        text="""A house painting service.""",
    )

    DATE_VEHICLE_FIRST_REGISTERED = Semantic(
        id="dateVehicleFirstRegistered",
        ref="schema:dateVehicleFirstRegistered",
        text="""The date of the first registration of the vehicle with the respective public authorities.""",
    )

    BODY_MEASUREMENT_ARM = Semantic(
        id="BodyMeasurementArm",
        ref="schema:BodyMeasurementArm",
        text="""Arm length (measured between arms/shoulder line intersection and the prominent wrist bone). Used, for example, to fit shirts.""",
    )

    GRACE_PERIOD = Semantic(
        id="gracePeriod",
        ref="schema:gracePeriod",
        text="""The period of time after any due date that the borrower has to fulfil its obligations before a default (failure to pay) is deemed to have occurred.""",
    )

    TEXT_DIGITAL_DOCUMENT = Semantic(
        id="TextDigitalDocument",
        ref="schema:TextDigitalDocument",
        text="""A file composed primarily of text.""",
    )

    DISLIKE_ACTION = Semantic(
        id="DislikeAction",
        ref="schema:DislikeAction",
        text="""The act of expressing a negative sentiment about the object. An agent dislikes an object (a proposition, topic or theme) with participants.""",
    )

    VOTE_ACTION = Semantic(
        id="VoteAction",
        ref="schema:VoteAction",
        text="""The act of expressing a preference from a fixed/finite/structured set of choices/options.""",
    )

    POSTAL_CODE_PREFIX = Semantic(
        id="postalCodePrefix",
        ref="schema:postalCodePrefix",
        text="""A defined range of postal codes indicated by a common textual prefix. Used for non-numeric systems such as UK.""",
    )

    PRE_ORDER = Semantic(
        id="PreOrder",
        ref="schema:PreOrder",
        text="""Indicates that the item is available for pre-order.""",
    )

    KEYWORDS = Semantic(
        id="keywords",
        ref="schema:keywords",
        text="""Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas.""",
    )

    NON_PROPRIETARY_NAME = Semantic(
        id="nonProprietaryName",
        ref="schema:nonProprietaryName",
        text="""The generic name of this drug or supplement.""",
    )

    HEALTH_PLAN_COINSURANCE_RATE = Semantic(
        id="healthPlanCoinsuranceRate",
        ref="schema:healthPlanCoinsuranceRate",
        text="""Whether The rate of coinsurance expressed as a number between 0.0 and 1.0.""",
    )

    INCENTIVE_COMPENSATION = Semantic(
        id="incentiveCompensation",
        ref="schema:incentiveCompensation",
        text="""Description of bonus and commission compensation aspects of the job.""",
    )

    LEGISLATION_TYPE = Semantic(
        id="legislationType",
        ref="schema:legislationType",
        text="""The type of the legislation. Examples of values are "law", "act", "directive", "decree", "regulation", "statutory instrument", "loi organique", "règlement grand-ducal", etc., depending on the country.""",
    )

    LOAN_TERM = Semantic(
        id="loanTerm",
        ref="schema:loanTerm",
        text="""The duration of the loan or credit agreement.""",
    )

    PAWN_SHOP = Semantic(
        id="PawnShop",
        ref="schema:PawnShop",
        text="""A shop that will buy, or lend money against the security of, personal possessions.""",
    )

    ORGANIZE_ACTION = Semantic(
        id="OrganizeAction",
        ref="schema:OrganizeAction",
        text="""The act of manipulating/administering/supervising/controlling one or more objects.""",
    )

    LEGISLATION_OBJECT = Semantic(
        id="LegislationObject",
        ref="schema:LegislationObject",
        text="""A specific object or file containing a Legislation. Note that the same Legislation can be published in multiple files. For example, a digitally signed PDF, a plain PDF and an HTML version.""",
    )

    WEARABLE_MEASUREMENT_WIDTH = Semantic(
        id="WearableMeasurementWidth",
        ref="schema:WearableMeasurementWidth",
        text="""Measurement of the width, for example of shoes""",
    )

    PRION = Semantic(
        id="Prion",
        ref="schema:Prion",
        text="""A prion is an infectious agent composed of protein in a misfolded form.""",
    )

    NAMED_POSITION = Semantic(
        id="namedPosition",
        ref="schema:namedPosition",
        text="""A position played, performed or filled by a person or organization, as part of an organization. For example, an athlete in a SportsTeam might play in the position named \'Quarterback\'.""",
    )

    TERM_CODE = Semantic(
        id="termCode",
        ref="schema:termCode",
        text="""A code that identifies this [[DefinedTerm]] within a [[DefinedTermSet]]""",
    )

    OFFERED_BY = Semantic(
        id="offeredBy",
        ref="schema:offeredBy",
        text="""A pointer to the organization or person making the offer.""",
    )

    CARRIER = Semantic(
        id="carrier",
        ref="schema:carrier",
        text="""\'carrier\' is an out-dated term indicating the \'provider\' for parcel delivery and flights.""",
    )

    OFFER_ITEM_CONDITION = Semantic(
        id="OfferItemCondition",
        ref="schema:OfferItemCondition",
        text="""A list of possible conditions for the item.""",
    )

    FAILED_ACTION_STATUS = Semantic(
        id="FailedActionStatus",
        ref="schema:FailedActionStatus",
        text="""An action that failed to complete. The action\'s error property and the HTTP return code contain more information about the failure.""",
    )

    POSSIBLE_TREATMENT = Semantic(
        id="possibleTreatment",
        ref="schema:possibleTreatment",
        text="""A possible treatment to address this condition, sign or symptom.""",
    )

    KOSHER_DIET = Semantic(
        id="KosherDiet",
        ref="schema:KosherDiet",
        text="""A diet conforming to Jewish dietary practices.""",
    )

    LATITUDE = Semantic(
        id="latitude",
        ref="schema:latitude",
        text="""The latitude of a location. For example ```37.42242``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).""",
    )

    ORIGINAL_MEDIA_CONTEXT_DESCRIPTION = Semantic(
        id="originalMediaContextDescription",
        ref="schema:originalMediaContextDescription",
        text="""Describes, in a [[MediaReview]] when dealing with [[DecontextualizedContent]], background information that can contribute to better interpretation of the [[MediaObject]].""",
    )

    BOOK_FORMAT = Semantic(
        id="bookFormat", ref="schema:bookFormat", text="""The format of the book."""
    )

    REAL_ESTATE_LISTING = Semantic(
        id="RealEstateListing",
        ref="schema:RealEstateListing",
        text="""A [[RealEstateListing]] is a listing that describes one or more real-estate [[Offer]]s (whose [[businessFunction]] is typically to lease out, or to sell).
  The [[RealEstateListing]] type itself represents the overall listing, as manifested in some [[WebPage]].
  """,
    )

    HOW_TO_ITEM = Semantic(
        id="HowToItem",
        ref="schema:HowToItem",
        text="""An item used as either a tool or supply when performing the instructions for how to to achieve a result.""",
    )

    ELEVATION = Semantic(
        id="elevation",
        ref="schema:elevation",
        text="""The elevation of a location ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)). Values may be of the form \'NUMBER UNIT_OF_MEASUREMENT\' (e.g., \'1,000 m\', \'3,200 ft\') while numbers alone should be assumed to be a value in meters.""",
    )

    MEDICAL_ORGANIZATION = Semantic(
        id="MedicalOrganization",
        ref="schema:MedicalOrganization",
        text="""A medical organization (physical or not), such as hospital, institution or clinic.""",
    )

    STATUS = Semantic(
        id="status",
        ref="schema:status",
        text="""The status of the study (enumerated).""",
    )

    ADDRESS = Semantic(
        id="address", ref="schema:address", text="""Physical address of the item."""
    )

    MEDICAL_THERAPY = Semantic(
        id="MedicalTherapy",
        ref="schema:MedicalTherapy",
        text="""Any medical intervention designed to prevent, treat, and cure human diseases and medical conditions, including both curative and palliative therapies. Medical therapies are typically processes of care relying upon pharmacotherapy, behavioral therapy, supportive therapy (with fluid or nutrition for example), or detoxification (e.g. hemodialysis) aimed at improving or preventing a health condition.""",
    )

    ACCOMMODATION_CATEGORY = Semantic(
        id="accommodationCategory",
        ref="schema:accommodationCategory",
        text="""Category of an [[Accommodation]], following real estate conventions e.g. RESO (see [PropertySubType](https://ddwiki.reso.org/display/DDW17/PropertySubType+Field), and [PropertyType](https://ddwiki.reso.org/display/DDW17/PropertyType+Field) fields  for suggested values).""",
    )

    EDUCATIONAL_AUDIENCE = Semantic(
        id="EducationalAudience",
        ref="schema:EducationalAudience",
        text="""An EducationalAudience.""",
    )

    DISSOLUTION_DATE = Semantic(
        id="dissolutionDate",
        ref="schema:dissolutionDate",
        text="""The date that this organization was dissolved.""",
    )

    CURRENCIES_ACCEPTED = Semantic(
        id="currenciesAccepted",
        ref="schema:currenciesAccepted",
        text="""The currency accepted.\\n\\nUse standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217) e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies e.g. "BTC"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types e.g. "Ithaca HOUR".""",
    )

    EQUAL = Semantic(
        id="equal",
        ref="schema:equal",
        text="""This ordering relation for qualitative values indicates that the subject is equal to the object.""",
    )

    PRICE_COMPONENT_TYPE_ENUMERATION = Semantic(
        id="PriceComponentTypeEnumeration",
        ref="schema:PriceComponentTypeEnumeration",
        text="""Enumerates different price components that together make up the total price for an offered product.""",
    )

    O_T_C = Semantic(
        id="OTC",
        ref="schema:OTC",
        text="""The character of a medical substance, typically a medicine, of being available over the counter or not.""",
    )

    SIZE_SPECIFICATION = Semantic(
        id="SizeSpecification",
        ref="schema:SizeSpecification",
        text="""Size related properties of a product, typically a size code ([[name]]) and optionally a [[sizeSystem]], [[sizeGroup]], and product measurements ([[hasMeasurement]]). In addition, the intended audience can be defined through [[suggestedAge]], [[suggestedGender]], and suggested body measurements ([[suggestedMeasurement]]).""",
    )

    CHAPTER = Semantic(
        id="Chapter",
        ref="schema:Chapter",
        text="""One of the sections into which a book is divided. A chapter usually has a section number or a name.""",
    )

    WEDNESDAY = Semantic(
        id="Wednesday",
        ref="schema:Wednesday",
        text="""The day of the week between Tuesday and Thursday.""",
    )

    RETURN_POLICY_COUNTRY = Semantic(
        id="returnPolicyCountry",
        ref="schema:returnPolicyCountry",
        text="""The country where the product has to be sent to for returns, for example "Ireland" using the [[name]] property of [[Country]]. You can also provide the two-letter [ISO 3166-1 alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1). Note that this can be different from the country where the product was originally shipped from or sent too.""",
    )

    AWAY_TEAM = Semantic(
        id="awayTeam",
        ref="schema:awayTeam",
        text="""The away team in a sports event.""",
    )

    MAPS = Semantic(
        id="maps", ref="schema:maps", text="""A URL to a map of the place."""
    )

    SERVICE_OPERATOR = Semantic(
        id="serviceOperator",
        ref="schema:serviceOperator",
        text="""The operating organization, if different from the provider.  This enables the representation of services that are provided by an organization, but operated by another organization like a subcontractor.""",
    )

    WARRANTY_SCOPE = Semantic(
        id="warrantyScope",
        ref="schema:warrantyScope",
        text="""The scope of the warranty promise.""",
    )

    PHYSIOLOGICAL_BENEFITS = Semantic(
        id="physiologicalBenefits",
        ref="schema:physiologicalBenefits",
        text="""Specific physiologic benefits associated to the plan.""",
    )

    EVENT_VENUE = Semantic(
        id="EventVenue", ref="schema:EventVenue", text="""An event venue."""
    )

    POTENTIAL_ACTION_STATUS = Semantic(
        id="PotentialActionStatus",
        ref="schema:PotentialActionStatus",
        text="""A description of an action that is supported.""",
    )

    BIRTH_DATE = Semantic(
        id="birthDate", ref="schema:birthDate", text="""Date of birth."""
    )

    PUBLIC_SWIMMING_POOL = Semantic(
        id="PublicSwimmingPool",
        ref="schema:PublicSwimmingPool",
        text="""A public swimming pool.""",
    )

    BY_MONTH_WEEK = Semantic(
        id="byMonthWeek",
        ref="schema:byMonthWeek",
        text="""Defines the week(s) of the month on which a recurring Event takes place. Specified as an Integer between 1-5. For clarity, byMonthWeek is best used in conjunction with byDay to indicate concepts like the first and third Mondays of a month.""",
    )

    ITEM = Semantic(
        id="item",
        ref="schema:item",
        text="""An entity represented by an entry in a list or data feed (e.g. an \'artist\' in a list of \'artists\')’.""",
    )

    VALID_FROM = Semantic(
        id="validFrom",
        ref="schema:validFrom",
        text="""The date when the item becomes valid.""",
    )

    BODY_MEASUREMENT_HAND = Semantic(
        id="BodyMeasurementHand",
        ref="schema:BodyMeasurementHand",
        text="""Maximum hand girth (measured over the knuckles of the open right hand excluding thumb, fingers together). Used, for example, to fit gloves.""",
    )

    EXERCISE_RELATED_DIET = Semantic(
        id="exerciseRelatedDiet",
        ref="schema:exerciseRelatedDiet",
        text="""A sub property of instrument. The diet used in this action.""",
    )

    INDUSTRY = Semantic(
        id="industry",
        ref="schema:industry",
        text="""The industry associated with the job position.""",
    )

    HAS_CATEGORY_CODE = Semantic(
        id="hasCategoryCode",
        ref="schema:hasCategoryCode",
        text="""A Category code contained in this code set.""",
    )

    WEARABLE_SIZE_SYSTEM_D_E = Semantic(
        id="WearableSizeSystemDE",
        ref="schema:WearableSizeSystemDE",
        text="""German size system for wearables.""",
    )

    CONTACT_PAGE = Semantic(
        id="ContactPage",
        ref="schema:ContactPage",
        text="""Web page type: Contact page.""",
    )

    VIDEO_OBJECT_SNAPSHOT = Semantic(
        id="VideoObjectSnapshot",
        ref="schema:VideoObjectSnapshot",
        text="""A specific and exact (byte-for-byte) version of a [[VideoObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren\'t represented in their actual content, do not affect this notion of identity.""",
    )

    VIRTUAL_LOCATION = Semantic(
        id="VirtualLocation",
        ref="schema:VirtualLocation",
        text="""An online or virtual location for attending events. For example, one may attend an online seminar or educational event. While a virtual location may be used as the location of an event, virtual locations should not be confused with physical locations in the real world.""",
    )

    POND = Semantic(id="Pond", ref="schema:Pond", text="""A pond.""")

    LIST_PRICE = Semantic(
        id="ListPrice",
        ref="schema:ListPrice",
        text="""Represents the list price (the price a product is actually advertised for) of an offered product.""",
    )

    AUDIENCE = Semantic(
        id="audience",
        ref="schema:audience",
        text="""An intended audience, i.e. a group for whom something was created.""",
    )

    CVD_NUM_C19_MECH_VENT_PATS = Semantic(
        id="cvdNumC19MechVentPats",
        ref="schema:cvdNumC19MechVentPats",
        text="""numc19mechventpats - HOSPITALIZED and VENTILATED: Patients hospitalized in an NHSN inpatient care location who have suspected or confirmed COVID-19 and are on a mechanical ventilator.""",
    )

    DISAMBIGUATING_DESCRIPTION = Semantic(
        id="disambiguatingDescription",
        ref="schema:disambiguatingDescription",
        text="""A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation.""",
    )

    ACTION_STATUS_TYPE = Semantic(
        id="ActionStatusType",
        ref="schema:ActionStatusType",
        text="""The status of an Action.""",
    )

    USER_CHECKINS = Semantic(
        id="UserCheckins",
        ref="schema:UserCheckins",
        text="""UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].""",
    )

    INGREDIENTS_HEALTH_ASPECT = Semantic(
        id="IngredientsHealthAspect",
        ref="schema:IngredientsHealthAspect",
        text="""Content discussing ingredients-related aspects of a health topic.""",
    )

    AVAILABLE_LANGUAGE = Semantic(
        id="availableLanguage",
        ref="schema:availableLanguage",
        text="""A language someone may use with or at the item, service or place. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[inLanguage]]""",
    )

    VALUE = Semantic(
        id="value",
        ref="schema:value",
        text="""The value of the quantitative value or property value node.\\n\\n* For [[QuantitativeValue]] and [[MonetaryAmount]], the recommended type for values is \'Number\'.\\n* For [[PropertyValue]], it can be \'Text;\', \'Number\', \'Boolean\', or \'StructuredValue\'.\\n* Use values from 0123456789 (Unicode \'DIGIT ZERO\' (U+0030) to \'DIGIT NINE\' (U+0039)) rather than superficially similiar Unicode symbols.\\n* Use \'.\' (Unicode \'FULL STOP\' (U+002E)) rather than \',\' to indicate a decimal point. Avoid using these symbols as a readability separator.""",
    )

    EMAIL_MESSAGE = Semantic(
        id="EmailMessage", ref="schema:EmailMessage", text="""An email message."""
    )

    PEOPLE_AUDIENCE = Semantic(
        id="PeopleAudience",
        ref="schema:PeopleAudience",
        text="""A set of characteristics belonging to people, e.g. who compose an item\'s target audience.""",
    )

    REFERENCES_ORDER = Semantic(
        id="referencesOrder",
        ref="schema:referencesOrder",
        text="""The Order(s) related to this Invoice. One or more Orders may be combined into a single Invoice.""",
    )

    AUDIENCE = Semantic(
        id="Audience",
        ref="schema:Audience",
        text="""Intended audience for an item, i.e. the group for whom the item was created.""",
    )

    CONFIRMATION_NUMBER = Semantic(
        id="confirmationNumber",
        ref="schema:confirmationNumber",
        text="""A number that confirms the given order or payment has been received.""",
    )

    LIFESTYLE_MODIFICATION = Semantic(
        id="LifestyleModification",
        ref="schema:LifestyleModification",
        text="""A process of care involving exercise, changes to diet, fitness routines, and other lifestyle changes aimed at improving a health condition.""",
    )

    ITEM_DEFECT_RETURN_FEES = Semantic(
        id="itemDefectReturnFees",
        ref="schema:itemDefectReturnFees",
        text="""The type of return fees for returns of defect products.""",
    )

    SEA_BODY_OF_WATER = Semantic(
        id="SeaBodyOfWater",
        ref="schema:SeaBodyOfWater",
        text="""A sea (for example, the Caspian sea).""",
    )

    HOW_IT_WORKS_HEALTH_ASPECT = Semantic(
        id="HowItWorksHealthAspect",
        ref="schema:HowItWorksHealthAspect",
        text="""Content that discusses and explains how a particular health-related topic works, e.g. in terms of mechanisms and underlying science.""",
    )

    ALUMNI = Semantic(
        id="alumni", ref="schema:alumni", text="""Alumni of an organization."""
    )

    AUTO_DEALER = Semantic(
        id="AutoDealer", ref="schema:AutoDealer", text="""An car dealership."""
    )

    LOAN_OR_CREDIT = Semantic(
        id="LoanOrCredit",
        ref="schema:LoanOrCredit",
        text="""A financial product for the loaning of an amount of money, or line of credit, under agreed terms and charges.""",
    )

    CVD_FACILITY_ID = Semantic(
        id="cvdFacilityId",
        ref="schema:cvdFacilityId",
        text="""Identifier of the NHSN facility that this data record applies to. Use [[cvdFacilityCounty]] to indicate the county. To provide other details, [[healthcareReportingData]] can be used on a [[Hospital]] entry.""",
    )

    HEALTH_INSURANCE_PLAN = Semantic(
        id="HealthInsurancePlan",
        ref="schema:HealthInsurancePlan",
        text="""A US-style health insurance plan, including PPOs, EPOs, and HMOs. """,
    )

    U_S_NONPROFIT_TYPE = Semantic(
        id="USNonprofitType",
        ref="schema:USNonprofitType",
        text="""USNonprofitType: Non-profit organization type originating from the United States.""",
    )

    FIRST_APPEARANCE = Semantic(
        id="firstAppearance",
        ref="schema:firstAppearance",
        text="""Indicates the first known occurence of a [[Claim]] in some [[CreativeWork]].""",
    )

    HOUSE = Semantic(
        id="House",
        ref="schema:House",
        text="""A house is a building or structure that has the ability to be occupied for habitation by humans or other creatures (Source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/House">http://en.wikipedia.org/wiki/House</a>).""",
    )

    SPONSOR = Semantic(
        id="sponsor",
        ref="schema:sponsor",
        text="""A person or organization that supports a thing through a pledge, promise, or financial contribution. e.g. a sponsor of a Medical Study or a corporate sponsor of an event.""",
    )

    ITEM_OFFERED = Semantic(
        id="itemOffered",
        ref="schema:itemOffered",
        text="""An item being offered (or demanded). The transactional nature of the offer or demand is documented using [[businessFunction]], e.g. sell, lease etc. While several common expected types are listed explicitly in this definition, others can be used. Using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.""",
    )

    TRAINING_SALARY = Semantic(
        id="trainingSalary",
        ref="schema:trainingSalary",
        text="""The estimated salary earned while in the program.""",
    )

    AFTER_MEDIA = Semantic(
        id="afterMedia",
        ref="schema:afterMedia",
        text="""A media object representing the circumstances after performing this direction.""",
    )

    ITEM_LIST_ORDER = Semantic(
        id="itemListOrder",
        ref="schema:itemListOrder",
        text="""Type of ordering (e.g. Ascending, Descending, Unordered).""",
    )

    COLLEGE_OR_UNIVERSITY = Semantic(
        id="CollegeOrUniversity",
        ref="schema:CollegeOrUniversity",
        text="""A college, university, or other third-level educational institution.""",
    )

    RESUME_ACTION = Semantic(
        id="ResumeAction",
        ref="schema:ResumeAction",
        text="""The act of resuming a device or application which was formerly paused (e.g. resume music playback or resume a timer).""",
    )

    MERCHANT_RETURN_UNSPECIFIED = Semantic(
        id="MerchantReturnUnspecified",
        ref="schema:MerchantReturnUnspecified",
        text="""Specifies that a product return policy is not provided.""",
    )

    CHECK_ACTION = Semantic(
        id="CheckAction",
        ref="schema:CheckAction",
        text="""An agent inspects, determines, investigates, inquires, or examines an object\'s accuracy, quality, condition, or state.""",
    )

    MONTHS_OF_EXPERIENCE = Semantic(
        id="monthsOfExperience",
        ref="schema:monthsOfExperience",
        text="""Indicates the minimal number of months of experience required for a position.""",
    )

    ARTICLE = Semantic(
        id="Article",
        ref="schema:Article",
        text="""An article, such as a news article or piece of investigative report. Newspapers and magazines have articles of many different types and this is intended to cover them all.\\n\\nSee also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).""",
    )

    STATISTICAL_POPULATION = Semantic(
        id="StatisticalPopulation",
        ref="schema:StatisticalPopulation",
        text="""A StatisticalPopulation is a set of instances of a certain given type that satisfy some set of constraints. The property [[populationType]] is used to specify the type. Any property that can be used on instances of that type can appear on the statistical population. For example, a [[StatisticalPopulation]] representing all [[Person]]s with a [[homeLocation]] of East Podunk California, would be described by applying the appropriate [[homeLocation]] and [[populationType]] properties to a [[StatisticalPopulation]] item that stands for that set of people.
The properties [[numConstraints]] and [[constrainingProperty]] are used to specify which of the populations properties are used to specify the population. Note that the sense of "population" used here is the general sense of a statistical
population, and does not imply that the population consists of people. For example, a [[populationType]] of [[Event]] or [[NewsArticle]] could be used. See also [[Observation]], and the [data and datasets](/docs/data-and-datasets.html) overview for more details.
  """,
    )

    WEARABLE_SIZE_SYSTEM_A_U = Semantic(
        id="WearableSizeSystemAU",
        ref="schema:WearableSizeSystemAU",
        text="""Australian size system for wearables.""",
    )

    LOW_CALORIE_DIET = Semantic(
        id="LowCalorieDiet",
        ref="schema:LowCalorieDiet",
        text="""A diet focused on reduced calorie intake.""",
    )

    STATE = Semantic(
        id="State", ref="schema:State", text="""A state or province of a country."""
    )

    STEERING_POSITION = Semantic(
        id="steeringPosition",
        ref="schema:steeringPosition",
        text="""The position of the steering wheel or similar device (mostly for cars).""",
    )

    RECOMMENDATION_STRENGTH = Semantic(
        id="recommendationStrength",
        ref="schema:recommendationStrength",
        text="""Strength of the guideline\'s recommendation (e.g. \'class I\').""",
    )

    PODCAST_EPISODE = Semantic(
        id="PodcastEpisode",
        ref="schema:PodcastEpisode",
        text="""A single episode of a podcast series.""",
    )

    USER_LIKES = Semantic(
        id="UserLikes",
        ref="schema:UserLikes",
        text="""UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].""",
    )

    MOLECULAR_FORMULA = Semantic(
        id="molecularFormula",
        ref="schema:molecularFormula",
        text="""The empirical formula is the simplest whole number ratio of all the atoms in a molecule.""",
    )

    GTIN14 = Semantic(
        id="gtin14",
        ref="schema:gtin14",
        text="""The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.""",
    )

    LESSER_OR_EQUAL = Semantic(
        id="lesserOrEqual",
        ref="schema:lesserOrEqual",
        text="""This ordering relation for qualitative values indicates that the subject is lesser than or equal to the object.""",
    )

    AVAILABILITY_ENDS = Semantic(
        id="availabilityEnds",
        ref="schema:availabilityEnds",
        text="""The end of the availability of the product or service included in the offer.""",
    )

    W_P_AD_BLOCK = Semantic(
        id="WPAdBlock",
        ref="schema:WPAdBlock",
        text="""An advertising section of the page.""",
    )

    TOURIST_DESTINATION = Semantic(
        id="TouristDestination",
        ref="schema:TouristDestination",
        text="""A tourist destination. In principle any [[Place]] can be a [[TouristDestination]] from a [[City]], Region or [[Country]] to an [[AmusementPark]] or [[Hotel]]. This Type can be used on its own to describe a general [[TouristDestination]], or be used as an [[additionalType]] to add tourist relevant properties to any other [[Place]].  A [[TouristDestination]] is defined as a [[Place]] that contains, or is colocated with, one or more [[TouristAttraction]]s, often linked by a similar theme or interest to a particular [[touristType]]. The [UNWTO](http://www2.unwto.org/) defines Destination (main destination of a tourism trip) as the place visited that is central to the decision to take the trip.
  (See examples below).""",
    )

    EDUCATIONAL_USE = Semantic(
        id="educationalUse",
        ref="schema:educationalUse",
        text="""The purpose of a work in the context of education; for example, \'assignment\', \'group work\'.""",
    )

    ACTION_PLATFORM = Semantic(
        id="actionPlatform",
        ref="schema:actionPlatform",
        text="""The high level platform(s) where the Action can be performed for the given URL. To specify a specific application or operating system instance, use actionApplication.""",
    )

    ORGANIZER = Semantic(
        id="organizer", ref="schema:organizer", text="""An organizer of an Event."""
    )

    BEACH = Semantic(id="Beach", ref="schema:Beach", text="""Beach.""")

    MEDICAL_TRIAL_DESIGN = Semantic(
        id="MedicalTrialDesign",
        ref="schema:MedicalTrialDesign",
        text="""Design models for medical trials. Enumerated type.""",
    )

    VIDEO_FRAME_SIZE = Semantic(
        id="videoFrameSize",
        ref="schema:videoFrameSize",
        text="""The frame size of the video.""",
    )

    TRAIN_STATION = Semantic(
        id="TrainStation", ref="schema:TrainStation", text="""A train station."""
    )

    CLAIM_INTERPRETER = Semantic(
        id="claimInterpreter",
        ref="schema:claimInterpreter",
        text="""For a [[Claim]] interpreted from [[MediaObject]] content
    sed to indicate a claim contained, implied or refined from the content of a [[MediaObject]].""",
    )

    GREATER_OR_EQUAL = Semantic(
        id="greaterOrEqual",
        ref="schema:greaterOrEqual",
        text="""This ordering relation for qualitative values indicates that the subject is greater than or equal to the object.""",
    )

    LAKE_BODY_OF_WATER = Semantic(
        id="LakeBodyOfWater",
        ref="schema:LakeBodyOfWater",
        text="""A lake (for example, Lake Pontrachain).""",
    )

    ACTOR = Semantic(
        id="actor",
        ref="schema:actor",
        text="""An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.""",
    )

    DECONTEXTUALIZED_CONTENT = Semantic(
        id="DecontextualizedContent",
        ref="schema:DecontextualizedContent",
        text="""Content coded \'missing context\' in a [[MediaReview]], considered in the context of how it was published or shared.

For a [[VideoObject]] to be \'missing context\': Presenting unaltered video in an inaccurate manner that misrepresents the footage. For example, using incorrect dates or locations, altering the transcript or sharing brief clips from a longer video to mislead viewers. (A video rated \'original\' can also be missing context.)

For an [[ImageObject]] to be \'missing context\': Presenting unaltered images in an inaccurate manner to misrepresent the image and mislead the viewer. For example, a common tactic is using an unaltered image but saying it came from a different time or place. (An image rated \'original\' can also be missing context.)

For an [[ImageObject]] with embedded text to be \'missing context\': An unaltered image presented in an inaccurate manner to misrepresent the image and mislead the viewer. For example, a common tactic is using an unaltered image but saying it came from a different time or place. (An \'original\' image with inaccurate text would generally fall in this category.)

For an [[AudioObject]] to be \'missing context\': Unaltered audio presented in an inaccurate manner that misrepresents it. For example, using incorrect dates or locations, or sharing brief clips from a longer recording to mislead viewers. (Audio rated “original” can also be missing context.)
""",
    )

    CHEMICAL_COMPOSITION = Semantic(
        id="chemicalComposition",
        ref="schema:chemicalComposition",
        text="""The chemical composition describes the identity and relative ratio of the chemical elements that make up the substance.""",
    )

    DEATH_PLACE = Semantic(
        id="deathPlace",
        ref="schema:deathPlace",
        text="""The place where the person died.""",
    )

    COMPILATION_ALBUM = Semantic(
        id="CompilationAlbum",
        ref="schema:CompilationAlbum",
        text="""CompilationAlbum.""",
    )

    HAS_HEALTH_ASPECT = Semantic(
        id="hasHealthAspect",
        ref="schema:hasHealthAspect",
        text="""Indicates the aspect or aspects specifically addressed in some [[HealthTopicContent]]. For example, that the content is an overview, or that it talks about treatment, self-care, treatments or their side-effects.""",
    )

    CAMPING_PITCH = Semantic(
        id="CampingPitch",
        ref="schema:CampingPitch",
        text="""A [[CampingPitch]] is an individual place for overnight stay in the outdoors, typically being part of a larger camping site, or [[Campground]].\\n\\n
In British English a campsite, or campground, is an area, usually divided into a number of pitches, where people can camp overnight using tents or camper vans or caravans; this British English use of the word is synonymous with the American English expression campground. In American English the term campsite generally means an area where an individual, family, group, or military unit can pitch a tent or park a camper; a campground may contain many campsites.
(Source: Wikipedia see [https://en.wikipedia.org/wiki/Campsite](https://en.wikipedia.org/wiki/Campsite)).\\n\\n
See also the dedicated [document on the use of schema.org for marking up hotels and other forms of accommodations](/docs/hotels.html).
""",
    )

    INTERACTION_SERVICE = Semantic(
        id="interactionService",
        ref="schema:interactionService",
        text="""The WebSite or SoftwareApplication where the interactions took place.""",
    )

    PLACE = Semantic(
        id="Place",
        ref="schema:Place",
        text="""Entities that have a somewhat fixed, physical extension.""",
    )

    TIE_ACTION = Semantic(
        id="TieAction",
        ref="schema:TieAction",
        text="""The act of reaching a draw in a competitive activity.""",
    )

    WORK_FEATURED = Semantic(
        id="workFeatured",
        ref="schema:workFeatured",
        text="""A work featured in some event, e.g. exhibited in an ExhibitionEvent.
       Specific subproperties are available for workPerformed (e.g. a play), or a workPresented (a Movie at a ScreeningEvent).""",
    )

    FLOOR_LEVEL = Semantic(
        id="floorLevel",
        ref="schema:floorLevel",
        text="""The floor level for an [[Accommodation]] in a multi-storey building. Since counting
  systems [vary internationally](https://en.wikipedia.org/wiki/Storey#Consecutive_number_floor_designations), the local system should be used where possible.""",
    )

    PAYMENT_ACCEPTED = Semantic(
        id="paymentAccepted",
        ref="schema:paymentAccepted",
        text="""Cash, Credit Card, Cryptocurrency, Local Exchange Tradings System, etc.""",
    )

    EVENTS = Semantic(
        id="events",
        ref="schema:events",
        text="""Upcoming or past events associated with this place or organization.""",
    )

    BOOKING_AGENT = Semantic(
        id="bookingAgent",
        ref="schema:bookingAgent",
        text="""\'bookingAgent\' is an out-dated term indicating a \'broker\' that serves as a booking agent.""",
    )

    SEAT_ROW = Semantic(
        id="seatRow",
        ref="schema:seatRow",
        text="""The row location of the reserved seat (e.g., B).""",
    )

    TOXICOLOGIC = Semantic(
        id="Toxicologic",
        ref="schema:Toxicologic",
        text="""A specific branch of medical science that is concerned with poisons, their nature, effects and detection and involved in the treatment of poisoning.""",
    )

    EVENT_ATTENDANCE_MODE = Semantic(
        id="eventAttendanceMode",
        ref="schema:eventAttendanceMode",
        text="""The eventAttendanceMode of an event indicates whether it occurs online, offline, or a mix.""",
    )

    BY_MONTH = Semantic(
        id="byMonth",
        ref="schema:byMonth",
        text="""Defines the month(s) of the year on which a recurring [[Event]] takes place. Specified as an [[Integer]] between 1-12. January is 1.""",
    )

    IS_UNLABELLED_FALLBACK = Semantic(
        id="isUnlabelledFallback",
        ref="schema:isUnlabelledFallback",
        text="""This can be marked \'true\' to indicate that some published [[DeliveryTimeSettings]] or [[ShippingRateSettings]] are intended to apply to all [[OfferShippingDetails]] published by the same merchant, when referenced by a [[shippingSettingsLink]] in those settings. It is not meaningful to use a \'true\' value for this property alongside a transitTimeLabel (for [[DeliveryTimeSettings]]) or shippingLabel (for [[ShippingRateSettings]]), since this property is for use with unlabelled settings.""",
    )

    GENERAL_CONTRACTOR = Semantic(
        id="GeneralContractor",
        ref="schema:GeneralContractor",
        text="""A general contractor.""",
    )

    DOSAGE_FORM = Semantic(
        id="dosageForm",
        ref="schema:dosageForm",
        text="""A dosage form in which this drug/supplement is available, e.g. \'tablet\', \'suspension\', \'injection\'.""",
    )

    MEDICAL_RISK_SCORE = Semantic(
        id="MedicalRiskScore",
        ref="schema:MedicalRiskScore",
        text="""A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score.""",
    )

    BUYER = Semantic(
        id="buyer",
        ref="schema:buyer",
        text="""A sub property of participant. The participant/person/organization that bought the object.""",
    )

    LAST_REVIEWED = Semantic(
        id="lastReviewed",
        ref="schema:lastReviewed",
        text="""Date on which the content on this web page was last reviewed for accuracy and/or completeness.""",
    )

    ONLINE_FULL = Semantic(
        id="OnlineFull",
        ref="schema:OnlineFull",
        text="""Game server status: OnlineFull. Server is online but unavailable. The maximum number of players has reached.""",
    )

    STEPS = Semantic(
        id="steps",
        ref="schema:steps",
        text="""A single step item (as HowToStep, text, document, video, etc.) or a HowToSection (originally misnamed \'steps\'; \'step\' is preferred).""",
    )

    SERVICE_AREA = Semantic(
        id="serviceArea",
        ref="schema:serviceArea",
        text="""The geographic area where the service is provided.""",
    )

    PRE_ORDER_ACTION = Semantic(
        id="PreOrderAction",
        ref="schema:PreOrderAction",
        text="""An agent orders a (not yet released) object/product/service to be delivered/sent.""",
    )

    ITEM_LIST_ORDER_ASCENDING = Semantic(
        id="ItemListOrderAscending",
        ref="schema:ItemListOrderAscending",
        text="""An ItemList ordered with lower values listed first.""",
    )

    INTERNATIONAL_TRIAL = Semantic(
        id="InternationalTrial",
        ref="schema:InternationalTrial",
        text="""An international trial.""",
    )

    MARGIN_OF_ERROR = Semantic(
        id="marginOfError",
        ref="schema:marginOfError",
        text="""A marginOfError for an [[Observation]].""",
    )

    NOTE_DIGITAL_DOCUMENT = Semantic(
        id="NoteDigitalDocument",
        ref="schema:NoteDigitalDocument",
        text="""A file containing a note, primarily for the author.""",
    )

    GETTING_TESTED_INFO = Semantic(
        id="gettingTestedInfo",
        ref="schema:gettingTestedInfo",
        text="""Information about getting tested (for a [[MedicalCondition]]), e.g. in the context of a pandemic.""",
    )

    CSS_SELECTOR_TYPE = Semantic(
        id="CssSelectorType",
        ref="schema:CssSelectorType",
        text="""Text representing a CSS selector.""",
    )

    EXERCISE_TYPE = Semantic(
        id="exerciseType",
        ref="schema:exerciseType",
        text="""Type(s) of exercise or activity, such as strength training, flexibility training, aerobics, cardiac rehabilitation, etc.""",
    )

    WARRANTY_SCOPE = Semantic(
        id="WarrantyScope",
        ref="schema:WarrantyScope",
        text="""A range of of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.\\n\\nCommonly used values:\\n\\n* http://purl.org/goodrelations/v1#Labor-BringIn\\n* http://purl.org/goodrelations/v1#PartsAndLabor-BringIn\\n* http://purl.org/goodrelations/v1#PartsAndLabor-PickUp
      """,
    )

    DROPOFF_LOCATION = Semantic(
        id="dropoffLocation",
        ref="schema:dropoffLocation",
        text="""Where a rental car can be dropped off.""",
    )

    IMAGING_TECHNIQUE = Semantic(
        id="imagingTechnique",
        ref="schema:imagingTechnique",
        text="""Imaging technique used.""",
    )

    MAIN_CONTENT_OF_PAGE = Semantic(
        id="mainContentOfPage",
        ref="schema:mainContentOfPage",
        text="""Indicates if this web page element is the main subject of the page.""",
    )

    SD_DATE_PUBLISHED = Semantic(
        id="sdDatePublished",
        ref="schema:sdDatePublished",
        text="""Indicates the date on which the current structured data was generated / published. Typically used alongside [[sdPublisher]]""",
    )

    NEUROLOGIC = Semantic(
        id="Neurologic",
        ref="schema:Neurologic",
        text="""A specific branch of medical science that studies the nerves and nervous system and its respective disease states.""",
    )

    BOARDING_POLICY_TYPE = Semantic(
        id="BoardingPolicyType",
        ref="schema:BoardingPolicyType",
        text="""A type of boarding policy used by an airline.""",
    )

    PODCAST_SERIES = Semantic(
        id="PodcastSeries",
        ref="schema:PodcastSeries",
        text="""A podcast is an episodic series of digital audio or video files which a user can download and listen to.""",
    )

    PROPERTY = Semantic(
        id="Property",
        ref="schema:Property",
        text="""A property, used to indicate attributes and relationships of some Thing; equivalent to rdf:Property.""",
    )

    PUBLIC_TOILET = Semantic(
        id="PublicToilet",
        ref="schema:PublicToilet",
        text="""A public toilet is a room or small building containing one or more toilets (and possibly also urinals) which is available for use by the general public, or by customers or employees of certain businesses.""",
    )

    MEDICAL_AUDIENCE = Semantic(
        id="MedicalAudience",
        ref="schema:MedicalAudience",
        text="""Target audiences for medical web pages.""",
    )

    CHEMICAL_ROLE = Semantic(
        id="chemicalRole",
        ref="schema:chemicalRole",
        text="""A role played by the BioChemEntity within a chemical context.""",
    )

    HIGH_PRICE = Semantic(
        id="highPrice",
        ref="schema:highPrice",
        text="""The highest price of all offers available.\\n\\nUsage guidelines:\\n\\n* Use values from 0123456789 (Unicode \'DIGIT ZERO\' (U+0030) to \'DIGIT NINE\' (U+0039)) rather than superficially similiar Unicode symbols.\\n* Use \'.\' (Unicode \'FULL STOP\' (U+002E)) rather than \',\' to indicate a decimal point. Avoid using these symbols as a readability separator.""",
    )

    LABEL_DETAILS = Semantic(
        id="labelDetails",
        ref="schema:labelDetails",
        text="""Link to the drug\'s label details.""",
    )

    CONSTRAINING_PROPERTY = Semantic(
        id="constrainingProperty",
        ref="schema:constrainingProperty",
        text="""Indicates a property used as a constraint to define a [[StatisticalPopulation]] with respect to the set of entities
  corresponding to an indicated type (via [[populationType]]).""",
    )

    NUMBER_OF_PREVIOUS_OWNERS = Semantic(
        id="numberOfPreviousOwners",
        ref="schema:numberOfPreviousOwners",
        text="""The number of owners of the vehicle, including the current one.\\n\\nTypical unit code(s): C62""",
    )

    ASSOCIATED_REVIEW = Semantic(
        id="associatedReview",
        ref="schema:associatedReview",
        text="""An associated [[Review]].""",
    )

    DIET_FEATURES = Semantic(
        id="dietFeatures",
        ref="schema:dietFeatures",
        text="""Nutritional information specific to the dietary plan. May include dietary recommendations on what foods to avoid, what foods to consume, and specific alterations/deviations from the USDA or other regulatory body\'s approved dietary guidelines.""",
    )

    PART_OF_EPISODE = Semantic(
        id="partOfEpisode",
        ref="schema:partOfEpisode",
        text="""The episode to which this clip belongs.""",
    )

    GAME_TIP = Semantic(
        id="gameTip", ref="schema:gameTip", text="""Links to tips, tactics, etc."""
    )

    EMPLOYMENT_UNIT = Semantic(
        id="employmentUnit",
        ref="schema:employmentUnit",
        text="""Indicates the department, unit and/or facility where the employee reports and/or in which the job is to be performed.""",
    )

    FLOOR_SIZE = Semantic(
        id="floorSize",
        ref="schema:floorSize",
        text="""The size of the accommodation, e.g. in square meter or squarefoot.
Typical unit code(s): MTK for square meter, FTK for square foot, or YDK for square yard """,
    )

    PRICE_COMPONENT = Semantic(
        id="priceComponent",
        ref="schema:priceComponent",
        text="""This property links to all [[UnitPriceSpecification]] nodes that apply in parallel for the [[CompoundPriceSpecification]] node.""",
    )

    EMAIL = Semantic(id="email", ref="schema:email", text="""Email address.""")

    RELATED_ANATOMY = Semantic(
        id="relatedAnatomy",
        ref="schema:relatedAnatomy",
        text="""Anatomical systems or structures that relate to the superficial anatomy.""",
    )

    HOLDING_ARCHIVE = Semantic(
        id="holdingArchive",
        ref="schema:holdingArchive",
        text="""[[ArchiveOrganization]] that holds, keeps or maintains the [[ArchiveComponent]].""",
    )

    TAX_I_D = Semantic(
        id="taxID",
        ref="schema:taxID",
        text="""The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain.""",
    )

    SUPPLY = Semantic(
        id="supply",
        ref="schema:supply",
        text="""A sub-property of instrument. A supply consumed when performing instructions or a direction.""",
    )

    STEP_VALUE = Semantic(
        id="stepValue",
        ref="schema:stepValue",
        text="""The stepValue attribute indicates the granularity that is expected (and required) of the value in a PropertyValueSpecification.""",
    )

    LABORATORY_SCIENCE = Semantic(
        id="LaboratoryScience",
        ref="schema:LaboratoryScience",
        text="""A medical science pertaining to chemical, hematological, immunologic, microscopic, or bacteriological diagnostic analyses or research.""",
    )

    SUPER_EVENT = Semantic(
        id="superEvent",
        ref="schema:superEvent",
        text="""An event that this event is a part of. For example, a collection of individual music performances might each have a music festival as their superEvent.""",
    )

    BROADCAST_CHANNEL = Semantic(
        id="BroadcastChannel",
        ref="schema:BroadcastChannel",
        text="""A unique instance of a BroadcastService on a CableOrSatelliteService lineup.""",
    )

    ALTERNATIVE_OF = Semantic(
        id="alternativeOf",
        ref="schema:alternativeOf",
        text="""Another gene which is a variation of this one.""",
    )

    HAS_ENERGY_EFFICIENCY_CATEGORY = Semantic(
        id="hasEnergyEfficiencyCategory",
        ref="schema:hasEnergyEfficiencyCategory",
        text="""Defines the energy efficiency Category (which could be either a rating out of range of values or a yes/no certification) for a product according to an international energy efficiency standard.""",
    )

    BASE_SALARY = Semantic(
        id="baseSalary",
        ref="schema:baseSalary",
        text="""The base salary of the job or of an employee in an EmployeeRole.""",
    )

    HAS_OCCUPATION = Semantic(
        id="hasOccupation",
        ref="schema:hasOccupation",
        text="""The Person\'s occupation. For past professions, use Role for expressing dates.""",
    )

    IS_PLAN_FOR_APARTMENT = Semantic(
        id="isPlanForApartment",
        ref="schema:isPlanForApartment",
        text="""Indicates some accommodation that this floor plan describes.""",
    )

    ALLERGIES_HEALTH_ASPECT = Semantic(
        id="AllergiesHealthAspect",
        ref="schema:AllergiesHealthAspect",
        text="""Content about the allergy-related aspects of a health topic.""",
    )

    SPATIAL_COVERAGE = Semantic(
        id="spatialCoverage",
        ref="schema:spatialCoverage",
        text="""The spatialCoverage of a CreativeWork indicates the place(s) which are the focus of the content. It is a subproperty of
      contentLocation intended primarily for more technical and detailed materials. For example with a Dataset, it indicates
      areas that the dataset describes: a dataset of New York weather would have spatialCoverage which was the place: the state of New York.""",
    )

    PROPERTY_I_D = Semantic(
        id="propertyID",
        ref="schema:propertyID",
        text="""A commonly used identifier for the characteristic represented by the property, e.g. a manufacturer or a standard code for a property. propertyID can be
(1) a prefixed string, mainly meant to be used with standards for product properties; (2) a site-specific, non-prefixed string (e.g. the primary key of the property or the vendor-specific id of the property), or (3)
a URL indicating the type of the property, either pointing to an external vocabulary, or a Web resource that describes the property (e.g. a glossary entry).
Standards bodies should promote a standard prefix for the identifiers of properties from their standards.""",
    )

    REPLY_ACTION = Semantic(
        id="ReplyAction",
        ref="schema:ReplyAction",
        text="""The act of responding to a question/message asked/sent by the object. Related to [[AskAction]]\\n\\nRelated actions:\\n\\n* [[AskAction]]: Appears generally as an origin of a ReplyAction.""",
    )

    VISUAL_ARTWORK = Semantic(
        id="VisualArtwork",
        ref="schema:VisualArtwork",
        text="""A work of art that is primarily visual in character.""",
    )

    CONVENIENCE_STORE = Semantic(
        id="ConvenienceStore",
        ref="schema:ConvenienceStore",
        text="""A convenience store.""",
    )

    USER_PAGE_VISITS = Semantic(
        id="UserPageVisits",
        ref="schema:UserPageVisits",
        text="""UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].""",
    )

    COST_PER_UNIT = Semantic(
        id="costPerUnit",
        ref="schema:costPerUnit",
        text="""The cost per unit of the drug.""",
    )

    QUEST = Semantic(
        id="quest",
        ref="schema:quest",
        text="""The task that a player-controlled character, or group of characters may complete in order to gain a reward.""",
    )

    TO_LOCATION = Semantic(
        id="toLocation",
        ref="schema:toLocation",
        text="""A sub property of location. The final location of the object or the agent after the action.""",
    )

    WORK_PERFORMED = Semantic(
        id="workPerformed",
        ref="schema:workPerformed",
        text="""A work performed in some event, for example a play performed in a TheaterEvent.""",
    )

    GEO_OVERLAPS = Semantic(
        id="geoOverlaps",
        ref="schema:geoOverlaps",
        text="""Represents a relationship between two geometries (or the places they represent), relating a geometry to another that geospatially overlaps it, i.e. they have some but not all points in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).""",
    )

    COUNTRIES_NOT_SUPPORTED = Semantic(
        id="countriesNotSupported",
        ref="schema:countriesNotSupported",
        text="""Countries for which the application is not supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.""",
    )

    BROADCAST_AFFILIATE_OF = Semantic(
        id="broadcastAffiliateOf",
        ref="schema:broadcastAffiliateOf",
        text="""The media network(s) whose content is broadcast on this station.""",
    )

    GOVERNMENT_BENEFITS_TYPE = Semantic(
        id="GovernmentBenefitsType",
        ref="schema:GovernmentBenefitsType",
        text="""GovernmentBenefitsType enumerates several kinds of government benefits to support the COVID-19 situation. Note that this structure may not capture all benefits offered.""",
    )

    HEALTH_PLAN_DRUG_TIER = Semantic(
        id="healthPlanDrugTier",
        ref="schema:healthPlanDrugTier",
        text="""The tier(s) of drugs offered by this formulary or insurance plan.""",
    )

    OUTLET_STORE = Semantic(
        id="OutletStore", ref="schema:OutletStore", text="""An outlet store."""
    )

    SUCCESSOR_OF = Semantic(
        id="successorOf",
        ref="schema:successorOf",
        text="""A pointer from a newer variant of a product  to its previous, often discontinued predecessor.""",
    )

    GAME_ITEM = Semantic(
        id="gameItem",
        ref="schema:gameItem",
        text="""An item is an object within the game world that can be collected by a player or, occasionally, a non-player character.""",
    )

    HAS_COURSE_INSTANCE = Semantic(
        id="hasCourseInstance",
        ref="schema:hasCourseInstance",
        text="""An offering of the course at a specific time and place or through specific media or mode of study or to a specific section of students.""",
    )

    VIDEO_OBJECT = Semantic(
        id="VideoObject", ref="schema:VideoObject", text="""A video file."""
    )

    REPLACE_ACTION = Semantic(
        id="ReplaceAction",
        ref="schema:ReplaceAction",
        text="""The act of editing a recipient by replacing an old object with a new object.""",
    )

    AUTOMATED_TELLER = Semantic(
        id="AutomatedTeller", ref="schema:AutomatedTeller", text="""ATM/cash machine."""
    )

    APPLY_ACTION = Semantic(
        id="ApplyAction",
        ref="schema:ApplyAction",
        text="""The act of registering to an organization/service without the guarantee to receive it.\\n\\nRelated actions:\\n\\n* [[RegisterAction]]: Unlike RegisterAction, ApplyAction has no guarantees that the application will be accepted.""",
    )

    APPEARANCE = Semantic(
        id="appearance",
        ref="schema:appearance",
        text="""Indicates an occurence of a [[Claim]] in some [[CreativeWork]].""",
    )

    MUSIC_GROUP = Semantic(
        id="MusicGroup",
        ref="schema:MusicGroup",
        text="""A musical group, such as a band, an orchestra, or a choir. Can also be a solo musician.""",
    )

    GUIDELINE_DATE = Semantic(
        id="guidelineDate",
        ref="schema:guidelineDate",
        text="""Date on which this guideline\'s recommendation was made.""",
    )

    LETTERER = Semantic(
        id="letterer",
        ref="schema:letterer",
        text="""The individual who adds lettering, including speech balloons and sound effects, to artwork.""",
    )

    ACCELERATION_TIME = Semantic(
        id="accelerationTime",
        ref="schema:accelerationTime",
        text="""The time needed to accelerate the vehicle from a given start velocity to a given target velocity.\\n\\nTypical unit code(s): SEC for seconds\\n\\n* Note: There are unfortunately no standard unit codes for seconds/0..100 km/h or seconds/0..60 mph. Simply use "SEC" for seconds and indicate the velocities in the [[name]] of the [[QuantitativeValue]], or use [[valueReference]] with a [[QuantitativeValue]] of 0..60 mph or 0..100 km/h to specify the reference speeds.""",
    )

    FOOD_EVENT = Semantic(
        id="foodEvent",
        ref="schema:foodEvent",
        text="""A sub property of location. The specific food event where the action occurred.""",
    )

    TOC_CONTINUATION = Semantic(
        id="tocContinuation",
        ref="schema:tocContinuation",
        text="""A [[HyperTocEntry]] can have a [[tocContinuation]] indicated, which is another [[HyperTocEntry]] that would be the default next item to play or render.""",
    )

    RECORD_LABEL = Semantic(
        id="recordLabel",
        ref="schema:recordLabel",
        text="""The label that issued the release.""",
    )

    ITEM_PAGE = Semantic(
        id="ItemPage",
        ref="schema:ItemPage",
        text="""A page devoted to a single item, such as a particular product or hotel.""",
    )

    DOSE_UNIT = Semantic(
        id="doseUnit",
        ref="schema:doseUnit",
        text="""The unit of the dose, e.g. \'mg\'.""",
    )

    SECURITY_SCREENING = Semantic(
        id="securityScreening",
        ref="schema:securityScreening",
        text="""The type of security screening the passenger is subject to.""",
    )

    MATERIAL = Semantic(
        id="material",
        ref="schema:material",
        text="""A material that something is made from, e.g. leather, wool, cotton, paper.""",
    )

    DOWN_PAYMENT = Semantic(
        id="downPayment",
        ref="schema:downPayment",
        text="""a type of payment made in cash during the onset of the purchase of an expensive good/service. The payment typically represents only a percentage of the full purchase price.""",
    )

    REAL_ESTATE_AGENT = Semantic(
        id="realEstateAgent",
        ref="schema:realEstateAgent",
        text="""A sub property of participant. The real estate agent involved in the action.""",
    )

    HARDWARE_STORE = Semantic(
        id="HardwareStore", ref="schema:HardwareStore", text="""A hardware store."""
    )

    END_OFFSET = Semantic(
        id="endOffset",
        ref="schema:endOffset",
        text="""The end time of the clip expressed as the number of seconds from the beginning of the work.""",
    )

    UNEMPLOYMENT_SUPPORT = Semantic(
        id="UnemploymentSupport",
        ref="schema:UnemploymentSupport",
        text="""UnemploymentSupport: this is a benefit for unemployment support.""",
    )

    ARTFORM = Semantic(
        id="artform",
        ref="schema:artform",
        text="""e.g. Painting, Drawing, Sculpture, Print, Photograph, Assemblage, Collage, etc.""",
    )

    IS_INVOLVED_IN_BIOLOGICAL_PROCESS = Semantic(
        id="isInvolvedInBiologicalProcess",
        ref="schema:isInvolvedInBiologicalProcess",
        text="""Biological process this BioChemEntity is involved in; please use PropertyValue if you want to include any evidence.""",
    )

    MEDICAL_RISK_CALCULATOR = Semantic(
        id="MedicalRiskCalculator",
        ref="schema:MedicalRiskCalculator",
        text="""A complex mathematical calculation requiring an online calculator, used to assess prognosis. Note: use the url property of Thing to record any URLs for online calculators.""",
    )

    HAS_OFFER_CATALOG = Semantic(
        id="hasOfferCatalog",
        ref="schema:hasOfferCatalog",
        text="""Indicates an OfferCatalog listing for this Organization, Person, or Service.""",
    )

    LOCKSMITH = Semantic(
        id="Locksmith", ref="schema:Locksmith", text="""A locksmith."""
    )

    NUMBER_OF_EMPLOYEES = Semantic(
        id="numberOfEmployees",
        ref="schema:numberOfEmployees",
        text="""The number of employees in an organization e.g. business.""",
    )

    RECORDED_IN = Semantic(
        id="recordedIn",
        ref="schema:recordedIn",
        text="""The CreativeWork that captured all or part of this Event.""",
    )

    ACTIVE_ACTION_STATUS = Semantic(
        id="ActiveActionStatus",
        ref="schema:ActiveActionStatus",
        text="""An in-progress action (e.g, while watching the movie, or driving to a location).""",
    )

    SUB_STAGE_SUFFIX = Semantic(
        id="subStageSuffix",
        ref="schema:subStageSuffix",
        text="""The substage, e.g. \'a\' for Stage IIIa.""",
    )

    RESERVATION_STATUS_TYPE = Semantic(
        id="ReservationStatusType",
        ref="schema:ReservationStatusType",
        text="""Enumerated status values for Reservation.""",
    )

    ARRIVAL_TERMINAL = Semantic(
        id="arrivalTerminal",
        ref="schema:arrivalTerminal",
        text="""Identifier of the flight\'s arrival terminal.""",
    )

    AUDIO_OBJECT_SNAPSHOT = Semantic(
        id="AudioObjectSnapshot",
        ref="schema:AudioObjectSnapshot",
        text="""A specific and exact (byte-for-byte) version of an [[AudioObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren\'t represented in their actual content, do not affect this notion of identity.""",
    )

    RETURN_IN_STORE = Semantic(
        id="ReturnInStore",
        ref="schema:ReturnInStore",
        text="""Specifies that product returns must be made in a store.""",
    )

    SEASON_NUMBER = Semantic(
        id="seasonNumber",
        ref="schema:seasonNumber",
        text="""Position of the season within an ordered group of seasons.""",
    )

    SEEK_TO_ACTION = Semantic(
        id="SeekToAction",
        ref="schema:SeekToAction",
        text="""This is the [[Action]] of navigating to a specific [[startOffset]] timestamp within a [[VideoObject]], typically represented with a URL template structure.""",
    )

    SUGGESTED_ANSWER = Semantic(
        id="suggestedAnswer",
        ref="schema:suggestedAnswer",
        text="""An answer (possibly one of several, possibly incorrect) to a Question, e.g. on a Question/Answer site.""",
    )

    MEDICAL_GUIDELINE_RECOMMENDATION = Semantic(
        id="MedicalGuidelineRecommendation",
        ref="schema:MedicalGuidelineRecommendation",
        text="""A guideline recommendation that is regarded as efficacious and where quality of the data supporting the recommendation is sound.""",
    )

    HEALTH_AND_BEAUTY_BUSINESS = Semantic(
        id="HealthAndBeautyBusiness",
        ref="schema:HealthAndBeautyBusiness",
        text="""Health and beauty.""",
    )

    TATTOO_PARLOR = Semantic(
        id="TattooParlor", ref="schema:TattooParlor", text="""A tattoo parlor."""
    )

    DONATE_ACTION = Semantic(
        id="DonateAction",
        ref="schema:DonateAction",
        text="""The act of providing goods, services, or money without compensation, often for philanthropic reasons.""",
    )

    USAGE_OR_SCHEDULE_HEALTH_ASPECT = Semantic(
        id="UsageOrScheduleHealthAspect",
        ref="schema:UsageOrScheduleHealthAspect",
        text="""Content about how, when, frequency and dosage of a topic.""",
    )

    SALARY_UPON_COMPLETION = Semantic(
        id="salaryUponCompletion",
        ref="schema:salaryUponCompletion",
        text="""The expected salary upon completing the training.""",
    )

    IN_CH_I_KEY = Semantic(
        id="inChIKey",
        ref="schema:inChIKey",
        text="""InChIKey is a hashed version of the full InChI (using the SHA-256 algorithm).""",
    )

    GUIDE = Semantic(
        id="Guide",
        ref="schema:Guide",
        text="""[[Guide]] is a page or article that recommend specific products or services, or aspects of a thing for a user to consider. A [[Guide]] may represent a Buying Guide and detail aspects of products or services for a user to consider. A [[Guide]] may represent a Product Guide and recommend specific products or services. A [[Guide]] may represent a Ranked List and recommend specific products or services with ranking.""",
    )

    ACTIVITY_DURATION = Semantic(
        id="activityDuration",
        ref="schema:activityDuration",
        text="""Length of time to engage in the activity.""",
    )

    SPORTS_EVENT = Semantic(
        id="sportsEvent",
        ref="schema:sportsEvent",
        text="""A sub property of location. The sports event where this action occurred.""",
    )

    ADD_ACTION = Semantic(
        id="AddAction",
        ref="schema:AddAction",
        text="""The act of editing by adding an object to a collection.""",
    )

    INFECTIOUS_AGENT = Semantic(
        id="infectiousAgent",
        ref="schema:infectiousAgent",
        text="""The actual infectious agent, such as a specific bacterium.""",
    )

    BOAT_TERMINAL = Semantic(
        id="BoatTerminal",
        ref="schema:BoatTerminal",
        text="""A terminal for boats, ships, and other water vessels.""",
    )

    VALID_THROUGH = Semantic(
        id="validThrough",
        ref="schema:validThrough",
        text="""The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.""",
    )

    MEDICAL_PROCEDURE = Semantic(
        id="MedicalProcedure",
        ref="schema:MedicalProcedure",
        text="""A process of care used in either a diagnostic, therapeutic, preventive or palliative capacity that relies on invasive (surgical), non-invasive, or other techniques.""",
    )

    VEGAN_DIET = Semantic(
        id="VeganDiet",
        ref="schema:VeganDiet",
        text="""A diet exclusive of all animal products.""",
    )

    DIGITAL_DOCUMENT = Semantic(
        id="DigitalDocument",
        ref="schema:DigitalDocument",
        text="""An electronic file or document.""",
    )

    NONPROFIT501C6 = Semantic(
        id="Nonprofit501c6",
        ref="schema:Nonprofit501c6",
        text="""Nonprofit501c6: Non-profit type referring to Business Leagues, Chambers of Commerce, Real Estate Boards.""",
    )

    ACCEPTS_RESERVATIONS = Semantic(
        id="acceptsReservations",
        ref="schema:acceptsReservations",
        text="""Indicates whether a FoodEstablishment accepts reservations. Values can be Boolean, an URL at which reservations can be made or (for backwards compatibility) the strings ```Yes``` or ```No```.""",
    )

    PUBLIC_HOLIDAYS = Semantic(
        id="PublicHolidays",
        ref="schema:PublicHolidays",
        text="""This stands for any day that is a public holiday; it is a placeholder for all official public holidays in some particular location. While not technically a "day of the week", it can be used with [[OpeningHoursSpecification]]. In the context of an opening hours specification it can be used to indicate opening hours on public holidays, overriding general opening hours for the day of the week on which a public holiday occurs.""",
    )

    VARIANT_COVER = Semantic(
        id="variantCover",
        ref="schema:variantCover",
        text="""A description of the variant cover
    	for the issue, if the issue is a variant printing. For example, "Bryan Hitch
    	Variant Cover" or "2nd Printing Variant".""",
    )

    CARDIOVASCULAR = Semantic(
        id="Cardiovascular",
        ref="schema:Cardiovascular",
        text="""A specific branch of medical science that pertains to diagnosis and treatment of disorders of heart and vasculature.""",
    )

    INTANGIBLE = Semantic(
        id="Intangible",
        ref="schema:Intangible",
        text="""A utility class that serves as the umbrella for a number of \'intangible\' things such as quantities, structured values, etc.""",
    )

    KNOWS = Semantic(
        id="knows",
        ref="schema:knows",
        text="""The most generic bi-directional social/work relation.""",
    )

    TIME_OF_DAY = Semantic(
        id="timeOfDay",
        ref="schema:timeOfDay",
        text="""The time of day the program normally runs. For example, "evenings".""",
    )

    MEDICAL_GUIDELINE = Semantic(
        id="MedicalGuideline",
        ref="schema:MedicalGuideline",
        text="""Any recommendation made by a standard society (e.g. ACC/AHA) or consensus statement that denotes how to diagnose and treat a particular condition. Note: this type should be used to tag the actual guideline recommendation; if the guideline recommendation occurs in a larger scholarly article, use MedicalScholarlyArticle to tag the overall article, not this type. Note also: the organization making the recommendation should be captured in the recognizingAuthority base property of MedicalEntity.""",
    )

    WORK_HOURS = Semantic(
        id="workHours",
        ref="schema:workHours",
        text="""The typical working hours for this job (e.g. 1st shift, night shift, 8am-5pm).""",
    )

    IS_RELATED_TO = Semantic(
        id="isRelatedTo",
        ref="schema:isRelatedTo",
        text="""A pointer to another, somehow related product (or multiple products).""",
    )

    AUDIO_OBJECT = Semantic(
        id="AudioObject", ref="schema:AudioObject", text="""An audio file."""
    )

    INDIVIDUAL_PRODUCT = Semantic(
        id="IndividualProduct",
        ref="schema:IndividualProduct",
        text="""A single, identifiable product instance (e.g. a laptop with a particular serial number).""",
    )

    MUSCULOSKELETAL_EXAM = Semantic(
        id="MusculoskeletalExam",
        ref="schema:MusculoskeletalExam",
        text="""Musculoskeletal system clinical examination.""",
    )

    REVIEW_BODY = Semantic(
        id="reviewBody",
        ref="schema:reviewBody",
        text="""The actual body of the review.""",
    )

    YEARLY_REVENUE = Semantic(
        id="yearlyRevenue",
        ref="schema:yearlyRevenue",
        text="""The size of the business in annual revenue.""",
    )

    MOTORIZED_BICYCLE = Semantic(
        id="MotorizedBicycle",
        ref="schema:MotorizedBicycle",
        text="""A motorized bicycle is a bicycle with an attached motor used to power the vehicle, or to assist with pedaling.""",
    )

    ITEM_AVAILABILITY = Semantic(
        id="ItemAvailability",
        ref="schema:ItemAvailability",
        text="""A list of possible product availability options.""",
    )

    IN_PRODUCT_GROUP_WITH_I_D = Semantic(
        id="inProductGroupWithID",
        ref="schema:inProductGroupWithID",
        text="""Indicates the [[productGroupID]] for a [[ProductGroup]] that this product [[isVariantOf]]. """,
    )

    SOCIAL_MEDIA_POSTING = Semantic(
        id="SocialMediaPosting",
        ref="schema:SocialMediaPosting",
        text="""A post to a social media platform, including blog posts, tweets, Facebook posts, etc.""",
    )

    NUMBER_OF_PLAYERS = Semantic(
        id="numberOfPlayers",
        ref="schema:numberOfPlayers",
        text="""Indicate how many people can play this game (minimum, maximum, or range).""",
    )

    OFFLINE_PERMANENTLY = Semantic(
        id="OfflinePermanently",
        ref="schema:OfflinePermanently",
        text="""Game server status: OfflinePermanently. Server is offline and not available.""",
    )

    COURSE_PREREQUISITES = Semantic(
        id="coursePrerequisites",
        ref="schema:coursePrerequisites",
        text="""Requirements for taking the Course. May be completion of another [[Course]] or a textual description like "permission of instructor". Requirements may be a pre-requisite competency, referenced using [[AlignmentObject]].""",
    )

    AGGREGATE_OFFER = Semantic(
        id="AggregateOffer",
        ref="schema:AggregateOffer",
        text="""When a single product is associated with multiple offers (for example, the same pair of shoes is offered by different merchants), then AggregateOffer can be used.\\n\\nNote: AggregateOffers are normally expected to associate multiple offers that all share the same defined [[businessFunction]] value, or default to http://purl.org/goodrelations/v1#Sell if businessFunction is not explicitly defined.""",
    )

    POSTER = Semantic(
        id="Poster",
        ref="schema:Poster",
        text="""A large, usually printed placard, bill, or announcement, often illustrated, that is posted to advertise or publicize something.""",
    )

    EMBED_URL = Semantic(
        id="embedUrl",
        ref="schema:embedUrl",
        text="""A URL pointing to a player for a specific video. In general, this is the information in the ```src``` element of an ```embed``` tag and should not be the same as the content of the ```loc``` tag.""",
    )

    COURSE_INSTANCE = Semantic(
        id="CourseInstance",
        ref="schema:CourseInstance",
        text="""An instance of a [[Course]] which is distinct from other instances because it is offered at a different time or location or through different media or modes of study or to a specific section of students.""",
    )

    EXPERIENCE_IN_PLACE_OF_EDUCATION = Semantic(
        id="experienceInPlaceOfEducation",
        ref="schema:experienceInPlaceOfEducation",
        text="""Indicates whether a [[JobPosting]] will accept experience (as indicated by [[OccupationalExperienceRequirements]]) in place of its formal educational qualifications (as indicated by [[educationRequirements]]). If true, indicates that satisfying one of these requirements is sufficient.""",
    )

    ARTERIAL_BRANCH = Semantic(
        id="arterialBranch",
        ref="schema:arterialBranch",
        text="""The branches that comprise the arterial structure.""",
    )

    F_D_ACATEGORY_C = Semantic(
        id="FDAcategoryC",
        ref="schema:FDAcategoryC",
        text="""A designation by the US FDA signifying that animal reproduction studies have shown an adverse effect on the fetus and there are no adequate and well-controlled studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.""",
    )

    WEIGHT_TOTAL = Semantic(
        id="weightTotal",
        ref="schema:weightTotal",
        text="""The permitted total weight of the loaded vehicle, including passengers and cargo and the weight of the empty vehicle.\\n\\nTypical unit code(s): KGM for kilogram, LBR for pound\\n\\n* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.\\n* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].\\n* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.""",
    )

    ORDER_NUMBER = Semantic(
        id="orderNumber",
        ref="schema:orderNumber",
        text="""The identifier of the transaction.""",
    )

    FOUR_WHEEL_DRIVE_CONFIGURATION = Semantic(
        id="FourWheelDriveConfiguration",
        ref="schema:FourWheelDriveConfiguration",
        text="""Four-wheel drive is a transmission layout where the engine primarily drives two wheels with a part-time four-wheel drive capability.""",
    )

    LEGISLATION_APPLIES = Semantic(
        id="legislationApplies",
        ref="schema:legislationApplies",
        text="""Indicates that this legislation (or part of a legislation) somehow transfers another legislation in a different legislative context. This is an informative link, and it has no legal value. For legally-binding links of transposition, use the <a href="/legislationTransposes">legislationTransposes</a> property. For example an informative consolidated law of a European Union\'s member state "applies" the consolidated version of the European Directive implemented in it.""",
    )

    ACCOMMODATION_FLOOR_PLAN = Semantic(
        id="accommodationFloorPlan",
        ref="schema:accommodationFloorPlan",
        text="""A floorplan of some [[Accommodation]].""",
    )

    RETURN_BY_MAIL = Semantic(
        id="ReturnByMail",
        ref="schema:ReturnByMail",
        text="""Specifies that product returns must to be done by mail.""",
    )

    INTERACTION_COUNT = Semantic(
        id="interactionCount",
        ref="schema:interactionCount",
        text="""This property is deprecated, alongside the UserInteraction types on which it depended.""",
    )

    EDUCATION_EVENT = Semantic(
        id="EducationEvent",
        ref="schema:EducationEvent",
        text="""Event type: Education event.""",
    )

    PICKUP_TIME = Semantic(
        id="pickupTime",
        ref="schema:pickupTime",
        text="""When a taxi will pickup a passenger or a rental car can be picked up.""",
    )

    ACCOUNT_OVERDRAFT_LIMIT = Semantic(
        id="accountOverdraftLimit",
        ref="schema:accountOverdraftLimit",
        text="""An overdraft is an extension of credit from a lending institution when an account reaches zero. An overdraft allows the individual to continue withdrawing money even if the account has no funds in it. Basically the bank allows people to borrow a set amount of money.""",
    )

    ENDORSEE = Semantic(
        id="endorsee",
        ref="schema:endorsee",
        text="""A sub property of participant. The person/organization being supported.""",
    )

    MISCONCEPTIONS_HEALTH_ASPECT = Semantic(
        id="MisconceptionsHealthAspect",
        ref="schema:MisconceptionsHealthAspect",
        text="""Content about common misconceptions and myths that are related to a topic.""",
    )

    OWNERSHIP_FUNDING_INFO = Semantic(
        id="ownershipFundingInfo",
        ref="schema:ownershipFundingInfo",
        text="""For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]), a description of organizational ownership structure; funding and grants. In a news/media setting, this is with particular reference to editorial independence.   Note that the [[funder]] is also available and can be used to make basic funder information machine-readable.""",
    )

    BED_TYPE = Semantic(
        id="BedType",
        ref="schema:BedType",
        text="""A type of bed. This is used for indicating the bed or beds available in an accommodation.""",
    )

    ENCODING_TYPE = Semantic(
        id="encodingType",
        ref="schema:encodingType",
        text="""The supported encoding type(s) for an EntryPoint request.""",
    )

    COVID_TESTING_FACILITY = Semantic(
        id="CovidTestingFacility",
        ref="schema:CovidTestingFacility",
        text="""A CovidTestingFacility is a [[MedicalClinic]] where testing for the COVID-19 Coronavirus
      disease is available. If the facility is being made available from an established [[Pharmacy]], [[Hotel]], or other
      non-medical organization, multiple types can be listed. This makes it easier to re-use existing schema.org information
      about that place e.g. contact info, address, opening hours. Note that in an emergency, such information may not always be reliable.
      """,
    )

    SIZE_SYSTEM_ENUMERATION = Semantic(
        id="SizeSystemEnumeration",
        ref="schema:SizeSystemEnumeration",
        text="""Enumerates common size systems for different categories of products, for example "EN-13402" or "UK" for wearables or "Imperial" for screws.""",
    )

    PUBLICATION = Semantic(
        id="publication",
        ref="schema:publication",
        text="""A publication event associated with the item.""",
    )

    WEARABLE_SIZE_GROUP_EXTRA_SHORT = Semantic(
        id="WearableSizeGroupExtraShort",
        ref="schema:WearableSizeGroupExtraShort",
        text="""Size group "Extra Short" for wearables.""",
    )

    FURNITURE_STORE = Semantic(
        id="FurnitureStore", ref="schema:FurnitureStore", text="""A furniture store."""
    )

    COST_ORIGIN = Semantic(
        id="costOrigin",
        ref="schema:costOrigin",
        text="""Additional details to capture the origin of the cost data. For example, \'Medicare Part B\'.""",
    )

    PODCAST_SEASON = Semantic(
        id="PodcastSeason",
        ref="schema:PodcastSeason",
        text="""A single season of a podcast. Many podcasts do not break down into separate seasons. In that case, PodcastSeries should be used.""",
    )

    NO_BYLINES_POLICY = Semantic(
        id="noBylinesPolicy",
        ref="schema:noBylinesPolicy",
        text="""For a [[NewsMediaOrganization]] or other news-related [[Organization]], a statement explaining when authors of articles are not named in bylines.""",
    )

    TRAIN_NAME = Semantic(
        id="trainName",
        ref="schema:trainName",
        text="""The name of the train (e.g. The Orient Express).""",
    )

    FIRST_PERFORMANCE = Semantic(
        id="firstPerformance",
        ref="schema:firstPerformance",
        text="""The date and place the work was first performed.""",
    )

    MEDICAL_OBSERVATIONAL_STUDY_DESIGN = Semantic(
        id="MedicalObservationalStudyDesign",
        ref="schema:MedicalObservationalStudyDesign",
        text="""Design models for observational medical studies. Enumerated type.""",
    )

    BOX = Semantic(
        id="box",
        ref="schema:box",
        text="""A box is the area enclosed by the rectangle formed by two points. The first point is the lower corner, the second point is the upper corner. A box is expressed as two points separated by a space character.""",
    )

    FEATURE_LIST = Semantic(
        id="featureList",
        ref="schema:featureList",
        text="""Features or modules provided by this application (and possibly required by other applications).""",
    )

    C_D_C_P_M_D_RECORD = Semantic(
        id="CDCPMDRecord",
        ref="schema:CDCPMDRecord",
        text="""A CDCPMDRecord is a data structure representing a record in a CDC tabular data format
      used for hospital data reporting. See [documentation](/docs/cdc-covid.html) for details, and the linked CDC materials for authoritative
      definitions used as the source here.
      """,
    )

    DELIVERY_TIME = Semantic(
        id="deliveryTime",
        ref="schema:deliveryTime",
        text="""The total delay between the receipt of the order and the goods reaching the final customer.""",
    )

    HOBBY_SHOP = Semantic(
        id="HobbyShop",
        ref="schema:HobbyShop",
        text="""A store that sells materials useful or necessary for various hobbies.""",
    )

    SHARED_CONTENT = Semantic(
        id="sharedContent",
        ref="schema:sharedContent",
        text="""A CreativeWork such as an image, video, or audio clip shared as part of this posting.""",
    )

    DATE_ISSUED = Semantic(
        id="dateIssued",
        ref="schema:dateIssued",
        text="""The date the ticket was issued.""",
    )

    BIOLOGICAL_ROLE = Semantic(
        id="biologicalRole",
        ref="schema:biologicalRole",
        text="""A role played by the BioChemEntity within a biological context.""",
    )

    MAP_TYPE = Semantic(
        id="mapType",
        ref="schema:mapType",
        text="""Indicates the kind of Map, from the MapCategoryType Enumeration.""",
    )

    WEARABLE_SIZE_SYSTEM_EUROPE = Semantic(
        id="WearableSizeSystemEurope",
        ref="schema:WearableSizeSystemEurope",
        text="""European size system for wearables.""",
    )

    MOSQUE = Semantic(id="Mosque", ref="schema:Mosque", text="""A mosque.""")

    RADIOGRAPHY = Semantic(
        id="Radiography",
        ref="schema:Radiography",
        text="""Radiography is an imaging technique that uses electromagnetic radiation other than visible light, especially X-rays, to view the internal structure of a non-uniformly composed and opaque object such as the human body.""",
    )

    TAXON_RANK = Semantic(
        id="taxonRank",
        ref="schema:taxonRank",
        text="""The taxonomic rank of this taxon given preferably as a URI from a controlled vocabulary – (typically the ranks from TDWG TaxonRank ontology or equivalent Wikidata URIs).""",
    )

    HOME_TEAM = Semantic(
        id="homeTeam",
        ref="schema:homeTeam",
        text="""The home team in a sports event.""",
    )

    ORDER_RETURNED = Semantic(
        id="OrderReturned",
        ref="schema:OrderReturned",
        text="""OrderStatus representing that an order has been returned.""",
    )

    RETURN_METHOD = Semantic(
        id="returnMethod",
        ref="schema:returnMethod",
        text="""The type of return method offered, specified from an enumeration.""",
    )

    SPEECH_TO_TEXT_MARKUP = Semantic(
        id="speechToTextMarkup",
        ref="schema:speechToTextMarkup",
        text="""Form of markup used. eg. [SSML](https://www.w3.org/TR/speech-synthesis11) or [IPA](https://www.wikidata.org/wiki/Property:P898).""",
    )

    PAINT_ACTION = Semantic(
        id="PaintAction",
        ref="schema:PaintAction",
        text="""The act of producing a painting, typically with paint and canvas as instruments.""",
    )

    MIDWIFERY = Semantic(
        id="Midwifery",
        ref="schema:Midwifery",
        text="""A nurse-like health profession that deals with pregnancy, childbirth, and the postpartum period (including care of the newborn), besides sexual and reproductive health of women throughout their lives.""",
    )

    TRANSIT_TIME_LABEL = Semantic(
        id="transitTimeLabel",
        ref="schema:transitTimeLabel",
        text="""Label to match an [[OfferShippingDetails]] with a [[DeliveryTimeSettings]] (within the context of a [[shippingSettingsLink]] cross-reference).""",
    )

    CLOSES = Semantic(
        id="closes",
        ref="schema:closes",
        text="""The closing hour of the place or service on the given day(s) of the week.""",
    )

    HEALTH_PLAN_COST_SHARING = Semantic(
        id="healthPlanCostSharing",
        ref="schema:healthPlanCostSharing",
        text="""Whether The costs to the patient for services under this network or formulary.""",
    )

    WEARABLE_MEASUREMENT_INSEAM = Semantic(
        id="WearableMeasurementInseam",
        ref="schema:WearableMeasurementInseam",
        text="""Measurement of the inseam, for example of pants""",
    )

    TARGET_DESCRIPTION = Semantic(
        id="targetDescription",
        ref="schema:targetDescription",
        text="""The description of a node in an established educational framework.""",
    )

    ON_SITE_PICKUP = Semantic(
        id="OnSitePickup",
        ref="schema:OnSitePickup",
        text="""A DeliveryMethod in which an item is collected on site, e.g. in a store or at a box office.""",
    )

    PERCENTILE90 = Semantic(
        id="percentile90",
        ref="schema:percentile90",
        text="""The 90th percentile value.""",
    )

    COMPLETED = Semantic(id="Completed", ref="schema:Completed", text="""Completed.""")

    REVIEW = Semantic(
        id="Review",
        ref="schema:Review",
        text="""A review of an item - for example, of a restaurant, movie, or store.""",
    )

    HAS_MENU = Semantic(
        id="hasMenu",
        ref="schema:hasMenu",
        text="""Either the actual menu as a structured representation, as text, or a URL of the menu.""",
    )

    SINGLE_PLAYER = Semantic(
        id="SinglePlayer",
        ref="schema:SinglePlayer",
        text="""Play mode: SinglePlayer. Which is played by a lone player.""",
    )

    ONLINE_EVENT_ATTENDANCE_MODE = Semantic(
        id="OnlineEventAttendanceMode",
        ref="schema:OnlineEventAttendanceMode",
        text="""OnlineEventAttendanceMode - an event that is primarily conducted online. """,
    )

    REPORTED_DOSE_SCHEDULE = Semantic(
        id="ReportedDoseSchedule",
        ref="schema:ReportedDoseSchedule",
        text="""A patient-reported or observed dosing schedule for a drug or supplement.""",
    )

    TERMS_PER_YEAR = Semantic(
        id="termsPerYear",
        ref="schema:termsPerYear",
        text="""The number of times terms of study are offered per year. Semesters and quarters are common units for term. For example, if the student can only take 2 semesters for the program in one year, then termsPerYear should be 2.""",
    )

    PATHOPHYSIOLOGY = Semantic(
        id="pathophysiology",
        ref="schema:pathophysiology",
        text="""Changes in the normal mechanical, physical, and biochemical functions that are associated with this activity or condition.""",
    )

    ENCODING_FORMAT = Semantic(
        id="encodingFormat",
        ref="schema:encodingFormat",
        text="""Media type typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml) and [MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)) e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc.).

In cases where a [[CreativeWork]] has several media type representations, [[encoding]] can be used to indicate each [[MediaObject]] alongside particular [[encodingFormat]] information.

Unregistered or niche encoding and file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry.""",
    )

    COMPRISED_OF = Semantic(
        id="comprisedOf",
        ref="schema:comprisedOf",
        text="""Specifying something physically contained by something else. Typically used here for the underlying anatomical structures, such as organs, that comprise the anatomical system.""",
    )

    OFFER_COUNT = Semantic(
        id="offerCount",
        ref="schema:offerCount",
        text="""The number of offers for the product.""",
    )

    MUSIC_ALBUM_RELEASE_TYPE = Semantic(
        id="MusicAlbumReleaseType",
        ref="schema:MusicAlbumReleaseType",
        text="""The kind of release which this album is: single, EP or album.""",
    )

    FULL_REFUND = Semantic(
        id="FullRefund",
        ref="schema:FullRefund",
        text="""Specifies that a refund can be done in the full amount the customer paid for the product""",
    )

    PROPERTY_VALUE_SPECIFICATION = Semantic(
        id="PropertyValueSpecification",
        ref="schema:PropertyValueSpecification",
        text="""A Property value specification.""",
    )

    FALSE = Semantic(
        id="False", ref="schema:False", text="""The boolean value false."""
    )

    OWNED_FROM = Semantic(
        id="ownedFrom",
        ref="schema:ownedFrom",
        text="""The date and time of obtaining the product.""",
    )

    ELECTRONICS_STORE = Semantic(
        id="ElectronicsStore",
        ref="schema:ElectronicsStore",
        text="""An electronics store.""",
    )

    LANGUAGE = Semantic(
        id="Language",
        ref="schema:Language",
        text="""Natural languages such as Spanish, Tamil, Hindi, English, etc. Formal language code tags expressed in [BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag) can be used via the [[alternateName]] property. The Language type previously also covered programming languages such as Scheme and Lisp, which are now best represented using [[ComputerLanguage]].""",
    )

    IN_STOCK = Semantic(
        id="InStock",
        ref="schema:InStock",
        text="""Indicates that the item is in stock.""",
    )

    REACT_ACTION = Semantic(
        id="ReactAction",
        ref="schema:ReactAction",
        text="""The act of responding instinctively and emotionally to an object, expressing a sentiment.""",
    )

    ENGINE_DISPLACEMENT = Semantic(
        id="engineDisplacement",
        ref="schema:engineDisplacement",
        text="""The volume swept by all of the pistons inside the cylinders of an internal combustion engine in a single movement. \\n\\nTypical unit code(s): CMQ for cubic centimeter, LTR for liters, INQ for cubic inches\\n* Note 1: You can link to information about how the given value has been determined using the [[valueReference]] property.\\n* Note 2: You can use [[minValue]] and [[maxValue]] to indicate ranges.""",
    )

    ACCOUNTING_SERVICE = Semantic(
        id="AccountingService",
        ref="schema:AccountingService",
        text="""Accountancy business.\\n\\nAs a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]\\(s).
      """,
    )

    HOURS_AVAILABLE = Semantic(
        id="hoursAvailable",
        ref="schema:hoursAvailable",
        text="""The hours during which this service or contact is available.""",
    )

    FOUNDER = Semantic(
        id="founder",
        ref="schema:founder",
        text="""A person who founded this organization.""",
    )

    WEARABLE_SIZE_GROUP_BIG = Semantic(
        id="WearableSizeGroupBig",
        ref="schema:WearableSizeGroupBig",
        text="""Size group "Big" for wearables.""",
    )

    PERFORMERS = Semantic(
        id="performers",
        ref="schema:performers",
        text="""The main performer or performers of the event&#x2014;for example, a presenter, musician, or actor.""",
    )

    PARCEL_SERVICE = Semantic(
        id="ParcelService",
        ref="schema:ParcelService",
        text="""A private parcel service as the delivery mode available for a certain offer.\\n\\nCommonly used values:\\n\\n* http://purl.org/goodrelations/v1#DHL\\n* http://purl.org/goodrelations/v1#FederalExpress\\n* http://purl.org/goodrelations/v1#UPS
      """,
    )

    MERCHANT_RETURN_UNLIMITED_WINDOW = Semantic(
        id="MerchantReturnUnlimitedWindow",
        ref="schema:MerchantReturnUnlimitedWindow",
        text="""Specifies that there is an unlimited window for product returns.""",
    )

    EXCHANGE_RATE_SPECIFICATION = Semantic(
        id="ExchangeRateSpecification",
        ref="schema:ExchangeRateSpecification",
        text="""A structured value representing exchange rate.""",
    )

    RESULTS_NOT_AVAILABLE = Semantic(
        id="ResultsNotAvailable",
        ref="schema:ResultsNotAvailable",
        text="""Results are not available.""",
    )

    POLICE_STATION = Semantic(
        id="PoliceStation", ref="schema:PoliceStation", text="""A police station."""
    )

    OTOLARYNGOLOGIC = Semantic(
        id="Otolaryngologic",
        ref="schema:Otolaryngologic",
        text="""A specific branch of medical science that is concerned with the ear, nose and throat and their respective disease states.""",
    )

    PART_OF_T_V_SERIES = Semantic(
        id="partOfTVSeries",
        ref="schema:partOfTVSeries",
        text="""The TV series to which this episode or season belongs.""",
    )

    OBSERVED_NODE = Semantic(
        id="observedNode",
        ref="schema:observedNode",
        text="""The observedNode of an [[Observation]], often a [[StatisticalPopulation]].""",
    )

    LONGITUDINAL = Semantic(
        id="Longitudinal",
        ref="schema:Longitudinal",
        text="""Unlike cross-sectional studies, longitudinal studies track the same people, and therefore the differences observed in those people are less likely to be the result of cultural differences across generations. Longitudinal studies are also used in medicine to uncover predictors of certain diseases.""",
    )

    COMPUTER_LANGUAGE = Semantic(
        id="ComputerLanguage",
        ref="schema:ComputerLanguage",
        text="""This type covers computer programming languages such as Scheme and Lisp, as well as other language-like computer representations. Natural languages are best represented with the [[Language]] type.""",
    )

    DEPART_ACTION = Semantic(
        id="DepartAction",
        ref="schema:DepartAction",
        text="""The act of  departing from a place. An agent departs from an fromLocation for a destination, optionally with participants.""",
    )

    P_E_T = Semantic(
        id="PET", ref="schema:PET", text="""Positron emission tomography imaging."""
    )

    NEURO = Semantic(
        id="Neuro",
        ref="schema:Neuro",
        text="""Neurological system clinical examination.""",
    )

    SURFACE = Semantic(
        id="surface",
        ref="schema:surface",
        text="""A material used as a surface in some artwork, e.g. Canvas, Paper, Wood, Board, etc.""",
    )

    MEDICAL_RESEARCHER = Semantic(
        id="MedicalResearcher",
        ref="schema:MedicalResearcher",
        text="""Medical researchers.""",
    )

    CVD_COLLECTION_DATE = Semantic(
        id="cvdCollectionDate",
        ref="schema:cvdCollectionDate",
        text="""collectiondate - Date for which patient counts are reported.""",
    )

    WEB_SITE = Semantic(
        id="WebSite",
        ref="schema:WebSite",
        text="""A WebSite is a set of related web pages and other items typically served from a single web domain and accessible via URLs.""",
    )

    NUMBER_OF_FULL_BATHROOMS = Semantic(
        id="numberOfFullBathrooms",
        ref="schema:numberOfFullBathrooms",
        text="""Number of full bathrooms - The total number of full and ¾ bathrooms in an [[Accommodation]]. This corresponds to the [BathroomsFull field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsFull+Field).""",
    )

    SHIPPING_RATE_SETTINGS = Semantic(
        id="ShippingRateSettings",
        ref="schema:ShippingRateSettings",
        text="""A ShippingRateSettings represents re-usable pieces of shipping information. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished and matched (i.e. identified/referenced) by their different values for [[shippingLabel]].""",
    )

    ENDORSE_ACTION = Semantic(
        id="EndorseAction",
        ref="schema:EndorseAction",
        text="""An agent approves/certifies/likes/supports/sanction an object.""",
    )

    ACTION_STATUS = Semantic(
        id="actionStatus",
        ref="schema:actionStatus",
        text="""Indicates the current disposition of the Action.""",
    )

    TUESDAY = Semantic(
        id="Tuesday",
        ref="schema:Tuesday",
        text="""The day of the week between Monday and Wednesday.""",
    )

    W_P_FOOTER = Semantic(
        id="WPFooter", ref="schema:WPFooter", text="""The footer section of the page."""
    )

    MEDIA_ITEM_APPEARANCE = Semantic(
        id="mediaItemAppearance",
        ref="schema:mediaItemAppearance",
        text="""In the context of a [[MediaReview]], indicates specific media item(s) that are grouped using a [[MediaReviewItem]].""",
    )

    BUS_NAME = Semantic(
        id="busName",
        ref="schema:busName",
        text="""The name of the bus (e.g. Bolt Express).""",
    )

    PATIENT = Semantic(
        id="Patient",
        ref="schema:Patient",
        text="""A patient is any person recipient of health care services.""",
    )

    F_M_RADIO_CHANNEL = Semantic(
        id="FMRadioChannel",
        ref="schema:FMRadioChannel",
        text="""A radio channel that uses FM.""",
    )

    HEALTH_CARE = Semantic(
        id="HealthCare",
        ref="schema:HealthCare",
        text="""HealthCare: this is a benefit for health care.""",
    )

    FEMALE = Semantic(id="Female", ref="schema:Female", text="""The female gender.""")

    VERIFICATION_FACT_CHECKING_POLICY = Semantic(
        id="verificationFactCheckingPolicy",
        ref="schema:verificationFactCheckingPolicy",
        text="""Disclosure about verification and fact-checking processes for a [[NewsMediaOrganization]] or other fact-checking [[Organization]].""",
    )

    INVESTMENT_OR_DEPOSIT = Semantic(
        id="InvestmentOrDeposit",
        ref="schema:InvestmentOrDeposit",
        text="""A type of financial product that typically requires the client to transfer funds to a financial service in return for potential beneficial financial return.""",
    )

    AFFECTED_BY = Semantic(
        id="affectedBy",
        ref="schema:affectedBy",
        text="""Drugs that affect the test\'s results.""",
    )

    INSURANCE_AGENCY = Semantic(
        id="InsuranceAgency",
        ref="schema:InsuranceAgency",
        text="""An Insurance agency.""",
    )

    RETURN_LABEL_CUSTOMER_RESPONSIBILITY = Semantic(
        id="ReturnLabelCustomerResponsibility",
        ref="schema:ReturnLabelCustomerResponsibility",
        text="""Indicated that creating a return label is the responsibility of the customer.""",
    )

    ACCEPTED_OFFER = Semantic(
        id="acceptedOffer",
        ref="schema:acceptedOffer",
        text="""The offer(s) -- e.g., product, quantity and price combinations -- included in the order.""",
    )

    RECORDING_OF = Semantic(
        id="recordingOf",
        ref="schema:recordingOf",
        text="""The composition this track is a recording of.""",
    )

    IMAGE = Semantic(
        id="image",
        ref="schema:image",
        text="""An image of the item. This can be a [[URL]] or a fully described [[ImageObject]].""",
    )

    DANCE_GROUP = Semantic(
        id="DanceGroup",
        ref="schema:DanceGroup",
        text="""A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance.""",
    )

    AUTOMOTIVE_BUSINESS = Semantic(
        id="AutomotiveBusiness",
        ref="schema:AutomotiveBusiness",
        text="""Car repair, sales, or parts.""",
    )

    VEHICLE_TRANSMISSION = Semantic(
        id="vehicleTransmission",
        ref="schema:vehicleTransmission",
        text="""The type of component used for transmitting the power from a rotating power source to the wheels or other relevant component(s) ("gearbox" for cars).""",
    )

    MEDICAL_DEVICE = Semantic(
        id="MedicalDevice",
        ref="schema:MedicalDevice",
        text="""Any object used in a medical capacity, such as to diagnose or treat a patient.""",
    )

    OCCUPATIONAL_CREDENTIAL_AWARDED = Semantic(
        id="occupationalCredentialAwarded",
        ref="schema:occupationalCredentialAwarded",
        text="""A description of the qualification, award, certificate, diploma or other occupational credential awarded as a consequence of successful completion of this course or program.""",
    )

    BODY_MEASUREMENT_FOOT = Semantic(
        id="BodyMeasurementFoot",
        ref="schema:BodyMeasurementFoot",
        text="""Foot length (measured between end of the most prominent toe and the most prominent part of the heel). Used, for example, to measure socks.""",
    )

    MAXIMUM_VIRTUAL_ATTENDEE_CAPACITY = Semantic(
        id="maximumVirtualAttendeeCapacity",
        ref="schema:maximumVirtualAttendeeCapacity",
        text="""The maximum physical attendee capacity of an [[Event]] whose [[eventAttendanceMode]] is [[OnlineEventAttendanceMode]] (or the online aspects, in the case of a [[MixedEventAttendanceMode]]). """,
    )

    D_DX_ELEMENT = Semantic(
        id="DDxElement",
        ref="schema:DDxElement",
        text="""An alternative, closely-related condition typically considered later in the differential diagnosis process along with the signs that are used to distinguish it.""",
    )

    ADD_ON = Semantic(
        id="addOn",
        ref="schema:addOn",
        text="""An additional offer that can only be obtained in combination with the first base offer (e.g. supplements and extensions that are available for a surcharge).""",
    )

    TAXI_STAND = Semantic(
        id="TaxiStand", ref="schema:TaxiStand", text="""A taxi stand."""
    )

    FLOOR_PLAN = Semantic(
        id="FloorPlan",
        ref="schema:FloorPlan",
        text="""A FloorPlan is an explicit representation of a collection of similar accommodations, allowing the provision of common information (room counts, sizes, layout diagrams) and offers for rental or sale. In typical use, some [[ApartmentComplex]] has an [[accommodationFloorPlan]] which is a [[FloorPlan]].  A FloorPlan is always in the context of a particular place, either a larger [[ApartmentComplex]] or a single [[Apartment]]. The visual/spatial aspects of a floor plan (i.e. room layout, [see wikipedia](https://en.wikipedia.org/wiki/Floor_plan)) can be indicated using [[image]]. """,
    )

    REGION_DRAINED = Semantic(
        id="regionDrained",
        ref="schema:regionDrained",
        text="""The anatomical or organ system drained by this vessel; generally refers to a specific part of an organ.""",
    )

    INVITE_ACTION = Semantic(
        id="InviteAction",
        ref="schema:InviteAction",
        text="""The act of asking someone to attend an event. Reciprocal of RsvpAction.""",
    )

    GENITOURINARY = Semantic(
        id="Genitourinary",
        ref="schema:Genitourinary",
        text="""Genitourinary system function assessment with clinical examination.""",
    )

    START_DATE = Semantic(
        id="startDate",
        ref="schema:startDate",
        text="""The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).""",
    )

    EMPLOYEE_ROLE = Semantic(
        id="EmployeeRole",
        ref="schema:EmployeeRole",
        text="""A subclass of OrganizationRole used to describe employee relationships.""",
    )

    PREGNANCY_HEALTH_ASPECT = Semantic(
        id="PregnancyHealthAspect",
        ref="schema:PregnancyHealthAspect",
        text="""Content discussing pregnancy-related aspects of a health topic.""",
    )

    REPLACER = Semantic(
        id="replacer",
        ref="schema:replacer",
        text="""A sub property of object. The object that replaces.""",
    )

    APPLICATION_CATEGORY = Semantic(
        id="applicationCategory",
        ref="schema:applicationCategory",
        text="""Type of software application, e.g. \'Game, Multimedia\'.""",
    )

    HEALTH_PLAN_COST_SHARING_SPECIFICATION = Semantic(
        id="HealthPlanCostSharingSpecification",
        ref="schema:HealthPlanCostSharingSpecification",
        text="""A description of costs to the patient under a given network or formulary.""",
    )

    SERVES_CUISINE = Semantic(
        id="servesCuisine",
        ref="schema:servesCuisine",
        text="""The cuisine of the restaurant.""",
    )

    WORKS_FOR = Semantic(
        id="worksFor",
        ref="schema:worksFor",
        text="""Organizations that the person works for.""",
    )

    HTTP_METHOD = Semantic(
        id="httpMethod",
        ref="schema:httpMethod",
        text="""An HTTP method that specifies the appropriate HTTP method for a request to an HTTP EntryPoint. Values are capitalized strings as used in HTTP.""",
    )

    EYE = Semantic(
        id="Eye",
        ref="schema:Eye",
        text="""Eye or ophtalmological function assessment with clinical examination.""",
    )

    INTERACTING_DRUG = Semantic(
        id="interactingDrug",
        ref="schema:interactingDrug",
        text="""Another drug that is known to interact with this drug in a way that impacts the effect of this drug or causes a risk to the patient. Note: disease interactions are typically captured as contraindications.""",
    )

    MONTHLY_MINIMUM_REPAYMENT_AMOUNT = Semantic(
        id="monthlyMinimumRepaymentAmount",
        ref="schema:monthlyMinimumRepaymentAmount",
        text="""The minimum payment is the lowest amount of money that one is required to pay on a credit card statement each month.""",
    )

    MERCHANT_RETURN_POLICY_SEASONAL_OVERRIDE = Semantic(
        id="MerchantReturnPolicySeasonalOverride",
        ref="schema:MerchantReturnPolicySeasonalOverride",
        text="""A seasonal override of a return policy, for example used for holidays.""",
    )

    HOMEOPATHIC = Semantic(
        id="Homeopathic",
        ref="schema:Homeopathic",
        text="""A system of medicine based on the principle that a disease can be cured by a substance that produces similar symptoms in healthy people.""",
    )

    HOME_AND_CONSTRUCTION_BUSINESS = Semantic(
        id="HomeAndConstructionBusiness",
        ref="schema:HomeAndConstructionBusiness",
        text="""A construction business.\\n\\nA HomeAndConstructionBusiness is a [[LocalBusiness]] that provides services around homes and buildings.\\n\\nAs a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]\\(s).""",
    )

    DROPOFF_TIME = Semantic(
        id="dropoffTime",
        ref="schema:dropoffTime",
        text="""When a rental car can be dropped off.""",
    )

    DELETE_ACTION = Semantic(
        id="DeleteAction",
        ref="schema:DeleteAction",
        text="""The act of editing a recipient by removing one of its objects.""",
    )

    ATTORNEY = Semantic(
        id="Attorney",
        ref="schema:Attorney",
        text="""Professional service: Attorney. \\n\\nThis type is deprecated - [[LegalService]] is more inclusive and less ambiguous.""",
    )

    MENS_CLOTHING_STORE = Semantic(
        id="MensClothingStore",
        ref="schema:MensClothingStore",
        text="""A men\'s clothing store.""",
    )

    PROGRAM_NAME = Semantic(
        id="programName",
        ref="schema:programName",
        text="""The program providing the membership.""",
    )

    ADDRESS_COUNTRY = Semantic(
        id="addressCountry",
        ref="schema:addressCountry",
        text="""The country. For example, USA. You can also provide the two-letter [ISO 3166-1 alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1).""",
    )

    CONNECTED_TO = Semantic(
        id="connectedTo",
        ref="schema:connectedTo",
        text="""Other anatomical structures to which this structure is connected.""",
    )

    IN_LANGUAGE = Semantic(
        id="inLanguage",
        ref="schema:inLanguage",
        text="""The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]].""",
    )

    AUTO_WASH = Semantic(
        id="AutoWash", ref="schema:AutoWash", text="""A car wash business."""
    )

    TARGET_COLLECTION = Semantic(
        id="targetCollection",
        ref="schema:targetCollection",
        text="""A sub property of object. The collection target of the action.""",
    )

    DATE_MODIFIED = Semantic(
        id="dateModified",
        ref="schema:dateModified",
        text="""The date on which the CreativeWork was most recently modified or when the item\'s entry was modified within a DataFeed.""",
    )

    RECEIVE_ACTION = Semantic(
        id="ReceiveAction",
        ref="schema:ReceiveAction",
        text="""The act of physically/electronically taking delivery of an object that has been transferred from an origin to a destination. Reciprocal of SendAction.\\n\\nRelated actions:\\n\\n* [[SendAction]]: The reciprocal of ReceiveAction.\\n* [[TakeAction]]: Unlike TakeAction, ReceiveAction does not imply that the ownership has been transfered (e.g. I can receive a package, but it does not mean the package is now mine).""",
    )

    REVIEWS = Semantic(
        id="reviews", ref="schema:reviews", text="""Review of the item."""
    )

    E_U_ENERGY_EFFICIENCY_CATEGORY_F = Semantic(
        id="EUEnergyEfficiencyCategoryF",
        ref="schema:EUEnergyEfficiencyCategoryF",
        text="""Represents EU Energy Efficiency Class F as defined in EU energy labeling regulations.""",
    )

    PERMIT_AUDIENCE = Semantic(
        id="permitAudience",
        ref="schema:permitAudience",
        text="""The target audience for this permit.""",
    )

    DURATION_OF_WARRANTY = Semantic(
        id="durationOfWarranty",
        ref="schema:durationOfWarranty",
        text="""The duration of the warranty promise. Common unitCode values are ANN for year, MON for months, or DAY for days.""",
    )

    NOT_IN_FORCE = Semantic(
        id="NotInForce",
        ref="schema:NotInForce",
        text="""Indicates that a legislation is currently not in force.""",
    )

    DATE_CREATED = Semantic(
        id="dateCreated",
        ref="schema:dateCreated",
        text="""The date on which the CreativeWork was created or the item was added to a DataFeed.""",
    )

    BOOLEAN = Semantic(
        id="Boolean", ref="schema:Boolean", text="""Boolean: True or False."""
    )

    MOVIE_SERIES = Semantic(
        id="MovieSeries",
        ref="schema:MovieSeries",
        text="""A series of movies. Included movies can be indicated with the hasPart property.""",
    )

    PERFORMER = Semantic(
        id="performer",
        ref="schema:performer",
        text="""A performer at the event&#x2014;for example, a presenter, musician, musical group or actor.""",
    )

    SODIUM_CONTENT = Semantic(
        id="sodiumContent",
        ref="schema:sodiumContent",
        text="""The number of milligrams of sodium.""",
    )

    SKU = Semantic(
        id="sku",
        ref="schema:sku",
        text="""The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.""",
    )

    DISCONTINUED = Semantic(
        id="Discontinued",
        ref="schema:Discontinued",
        text="""Indicates that the item has been discontinued.""",
    )

    TELEPHONE = Semantic(
        id="telephone", ref="schema:telephone", text="""The telephone number."""
    )

    PARENT_SERVICE = Semantic(
        id="parentService",
        ref="schema:parentService",
        text="""A broadcast service to which the broadcast service may belong to such as regional variations of a national channel.""",
    )

    GREATER = Semantic(
        id="greater",
        ref="schema:greater",
        text="""This ordering relation for qualitative values indicates that the subject is greater than the object.""",
    )

    OPENING_HOURS_SPECIFICATION = Semantic(
        id="openingHoursSpecification",
        ref="schema:openingHoursSpecification",
        text="""The opening hours of a certain place.""",
    )

    LODGING_RESERVATION = Semantic(
        id="LodgingReservation",
        ref="schema:LodgingReservation",
        text="""A reservation for lodging at a hotel, motel, inn, etc.\\n\\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.""",
    )

    WEB_CHECKIN_TIME = Semantic(
        id="webCheckinTime",
        ref="schema:webCheckinTime",
        text="""The time when a passenger can check into the flight online.""",
    )

    ORIGIN_ADDRESS = Semantic(
        id="originAddress", ref="schema:originAddress", text="""Shipper\'s address."""
    )

    LIVE_ALBUM = Semantic(id="LiveAlbum", ref="schema:LiveAlbum", text="""LiveAlbum.""")

    REFERENCE_QUANTITY = Semantic(
        id="referenceQuantity",
        ref="schema:referenceQuantity",
        text="""The reference quantity for which a certain price applies, e.g. 1 EUR per 4 kWh of electricity. This property is a replacement for unitOfMeasurement for the advanced cases where the price does not relate to a standard unit.""",
    )

    INVOICE = Semantic(
        id="Invoice",
        ref="schema:Invoice",
        text="""A statement of the money due for goods or services; a bill.""",
    )

    SPORTING_GOODS_STORE = Semantic(
        id="SportingGoodsStore",
        ref="schema:SportingGoodsStore",
        text="""A sporting goods store.""",
    )

    HAS_P_O_S = Semantic(
        id="hasPOS",
        ref="schema:hasPOS",
        text="""Points-of-Sales operated by the organization or person.""",
    )

    ASSOCIATED_MEDIA = Semantic(
        id="associatedMedia",
        ref="schema:associatedMedia",
        text="""A media object that encodes this CreativeWork. This property is a synonym for encoding.""",
    )

    JOB_BENEFITS = Semantic(
        id="jobBenefits",
        ref="schema:jobBenefits",
        text="""Description of benefits associated with the job.""",
    )

    CAFE_OR_COFFEE_SHOP = Semantic(
        id="CafeOrCoffeeShop",
        ref="schema:CafeOrCoffeeShop",
        text="""A cafe or coffee shop.""",
    )

    IS_CONSUMABLE_FOR = Semantic(
        id="isConsumableFor",
        ref="schema:isConsumableFor",
        text="""A pointer to another product (or multiple products) for which this product is a consumable.""",
    )

    WEARABLE_SIZE_SYSTEM_I_T = Semantic(
        id="WearableSizeSystemIT",
        ref="schema:WearableSizeSystemIT",
        text="""Italian size system for wearables.""",
    )

    ALBUM_RELEASE = Semantic(
        id="AlbumRelease", ref="schema:AlbumRelease", text="""AlbumRelease."""
    )

    DATA_FEED_ELEMENT = Semantic(
        id="dataFeedElement",
        ref="schema:dataFeedElement",
        text="""An item within in a data feed. Data feeds may have many elements.""",
    )

    EDUCATIONAL_FRAMEWORK = Semantic(
        id="educationalFramework",
        ref="schema:educationalFramework",
        text="""The framework to which the resource being described is aligned.""",
    )

    ENERGY_STAR_CERTIFIED = Semantic(
        id="EnergyStarCertified",
        ref="schema:EnergyStarCertified",
        text="""Represents EnergyStar certification.""",
    )

    RESERVATION_PACKAGE = Semantic(
        id="ReservationPackage",
        ref="schema:ReservationPackage",
        text="""A group of multiple reservations with common values for all sub-reservations.""",
    )

    DEPARTURE_TERMINAL = Semantic(
        id="departureTerminal",
        ref="schema:departureTerminal",
        text="""Identifier of the flight\'s departure terminal.""",
    )

    BODY_MEASUREMENT_NECK = Semantic(
        id="BodyMeasurementNeck",
        ref="schema:BodyMeasurementNeck",
        text="""Girth of neck. Used, for example, to fit shirts.""",
    )

    GEO_CIRCLE = Semantic(
        id="GeoCircle",
        ref="schema:GeoCircle",
        text="""A GeoCircle is a GeoShape representing a circular geographic area. As it is a GeoShape
          it provides the simple textual property \'circle\', but also allows the combination of postalCode alongside geoRadius.
          The center of the circle can be indicated via the \'geoMidpoint\' property, or more approximately using \'address\', \'postalCode\'.
       """,
    )

    CONSORTIUM = Semantic(
        id="Consortium",
        ref="schema:Consortium",
        text="""A Consortium is a membership [[Organization]] whose members are typically Organizations.""",
    )

    WARRANTY_PROMISE = Semantic(
        id="WarrantyPromise",
        ref="schema:WarrantyPromise",
        text="""A structured value representing the duration and scope of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.""",
    )

    CURRENT_EXCHANGE_RATE = Semantic(
        id="currentExchangeRate",
        ref="schema:currentExchangeRate",
        text="""The current price of a currency.""",
    )

    NEWS_UPDATES_AND_GUIDELINES = Semantic(
        id="newsUpdatesAndGuidelines",
        ref="schema:newsUpdatesAndGuidelines",
        text="""Indicates a page with news updates and guidelines. This could often be (but is not required to be) the main page containing [[SpecialAnnouncement]] markup on a site.""",
    )

    SOCIAL_EVENT = Semantic(
        id="SocialEvent", ref="schema:SocialEvent", text="""Event type: Social event."""
    )

    RELATED_DRUG = Semantic(
        id="relatedDrug",
        ref="schema:relatedDrug",
        text="""Any other drug related to this one, for example commonly-prescribed alternatives.""",
    )

    INCLUDES_ATTRACTION = Semantic(
        id="includesAttraction",
        ref="schema:includesAttraction",
        text="""Attraction located at destination.""",
    )

    HIGH_SCHOOL = Semantic(
        id="HighSchool", ref="schema:HighSchool", text="""A high school."""
    )

    COLLEAGUE = Semantic(
        id="colleague", ref="schema:colleague", text="""A colleague of the person."""
    )

    GTIN = Semantic(
        id="gtin",
        ref="schema:gtin",
        text="""A Global Trade Item Number ([GTIN](https://www.gs1.org/standards/id-keys/gtin)). GTINs identify trade items, including products and services, using numeric identification codes. The [[gtin]] property generalizes the earlier [[gtin8]], [[gtin12]], [[gtin13]], and [[gtin14]] properties. The GS1 [digital link specifications](https://www.gs1.org/standards/Digital-Link/) express GTINs as URLs. A correct [[gtin]] value should be a valid GTIN, which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a "GS1 Digital Link" URL based on such a string. The numeric component should also have a [valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator) and meet the other rules for valid GTINs. See also [GS1\'s GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) and [Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number) for more details. Left-padding of the gtin values is not required or encouraged.
   """,
    )

    UNIT_CODE = Semantic(
        id="unitCode",
        ref="schema:unitCode",
        text="""The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.""",
    )

    MUSEUM = Semantic(id="Museum", ref="schema:Museum", text="""A museum.""")

    GEO_SHAPE = Semantic(
        id="GeoShape",
        ref="schema:GeoShape",
        text="""The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points.""",
    )

    DATE = Semantic(
        id="Date",
        ref="schema:Date",
        text="""A date value in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).""",
    )

    GEOGRAPHIC_AREA = Semantic(
        id="geographicArea",
        ref="schema:geographicArea",
        text="""The geographic area associated with the audience.""",
    )

    INTERPRETED_AS_CLAIM = Semantic(
        id="interpretedAsClaim",
        ref="schema:interpretedAsClaim",
        text="""Used to indicate a specific claim contained, implied, translated or refined from the content of a [[MediaObject]] or other [[CreativeWork]]. The interpreting party can be indicated using [[claimInterpreter]].""",
    )

    DOSE_SCHEDULE = Semantic(
        id="DoseSchedule",
        ref="schema:DoseSchedule",
        text="""A specific dosing schedule for a drug or supplement.""",
    )

    BROKERAGE_ACCOUNT = Semantic(
        id="BrokerageAccount",
        ref="schema:BrokerageAccount",
        text="""An account that allows an investor to deposit funds and place investment orders with a licensed broker or brokerage firm.""",
    )

    CHECKOUT_PAGE = Semantic(
        id="CheckoutPage",
        ref="schema:CheckoutPage",
        text="""Web page type: Checkout page.""",
    )

    PUBLICATION_ISSUE = Semantic(
        id="PublicationIssue",
        ref="schema:PublicationIssue",
        text="""A part of a successively published publication such as a periodical or publication volume, often numbered, usually containing a grouping of works such as articles.\\n\\nSee also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).""",
    )

    LOSE_ACTION = Semantic(
        id="LoseAction",
        ref="schema:LoseAction",
        text="""The act of being defeated in a competitive activity.""",
    )

    DEPARTURE_AIRPORT = Semantic(
        id="departureAirport",
        ref="schema:departureAirport",
        text="""The airport where the flight originates.""",
    )

    TARGET_NAME = Semantic(
        id="targetName",
        ref="schema:targetName",
        text="""The name of a node in an established educational framework.""",
    )

    COMMENT = Semantic(
        id="Comment",
        ref="schema:Comment",
        text="""A comment on an item - for example, a comment on a blog post. The comment\'s content is expressed via the [[text]] property, and its topic via [[about]], properties shared with all CreativeWorks.""",
    )

    IDENTIFYING_TEST = Semantic(
        id="identifyingTest",
        ref="schema:identifyingTest",
        text="""A diagnostic test that can identify this sign.""",
    )

    ANATOMICAL_SYSTEM = Semantic(
        id="AnatomicalSystem",
        ref="schema:AnatomicalSystem",
        text="""An anatomical system is a group of anatomical structures that work together to perform a certain task. Anatomical systems, such as organ systems, are one organizing principle of anatomy, and can includes circulatory, digestive, endocrine, integumentary, immune, lymphatic, muscular, nervous, reproductive, respiratory, skeletal, urinary, vestibular, and other systems.""",
    )

    LOW_FAT_DIET = Semantic(
        id="LowFatDiet",
        ref="schema:LowFatDiet",
        text="""A diet focused on reduced fat and cholesterol intake.""",
    )

    SPREADSHEET_DIGITAL_DOCUMENT = Semantic(
        id="SpreadsheetDigitalDocument",
        ref="schema:SpreadsheetDigitalDocument",
        text="""A spreadsheet file.""",
    )

    REVIEW = Semantic(
        id="review", ref="schema:review", text="""A review of the item."""
    )

    ZONE_BOARDING_POLICY = Semantic(
        id="ZoneBoardingPolicy",
        ref="schema:ZoneBoardingPolicy",
        text="""The airline boards by zones of the plane.""",
    )

    RESERVATION_STATUS = Semantic(
        id="reservationStatus",
        ref="schema:reservationStatus",
        text="""The current status of the reservation.""",
    )

    MEASURED_VALUE = Semantic(
        id="measuredValue",
        ref="schema:measuredValue",
        text="""The measuredValue of an [[Observation]].""",
    )

    PERFORMER_IN = Semantic(
        id="performerIn",
        ref="schema:performerIn",
        text="""Event that this person is a performer or participant in.""",
    )

    NONPROFIT501E = Semantic(
        id="Nonprofit501e",
        ref="schema:Nonprofit501e",
        text="""Nonprofit501e: Non-profit type referring to Cooperative Hospital Service Organizations.""",
    )

    VEHICLE_ENGINE = Semantic(
        id="vehicleEngine",
        ref="schema:vehicleEngine",
        text="""Information about the engine or engines of the vehicle.""",
    )

    MAX_VALUE = Semantic(
        id="maxValue",
        ref="schema:maxValue",
        text="""The upper value of some characteristic or property.""",
    )

    IN_DEFINED_TERM_SET = Semantic(
        id="inDefinedTermSet",
        ref="schema:inDefinedTermSet",
        text="""A [[DefinedTermSet]] that contains this term.""",
    )

    SCREEN_COUNT = Semantic(
        id="screenCount",
        ref="schema:screenCount",
        text="""The number of screens in the movie theater.""",
    )

    SUB_EVENTS = Semantic(
        id="subEvents",
        ref="schema:subEvents",
        text="""Events that are a part of this event. For example, a conference event includes many presentations, each subEvents of the conference.""",
    )

    TOY_STORE = Semantic(id="ToyStore", ref="schema:ToyStore", text="""A toy store.""")

    FIBER_CONTENT = Semantic(
        id="fiberContent",
        ref="schema:fiberContent",
        text="""The number of grams of fiber.""",
    )

    IGNORE_ACTION = Semantic(
        id="IgnoreAction",
        ref="schema:IgnoreAction",
        text="""The act of intentionally disregarding the object. An agent ignores an object.""",
    )

    REQUIRED_GENDER = Semantic(
        id="requiredGender",
        ref="schema:requiredGender",
        text="""Audiences defined by a person\'s gender.""",
    )

    HOW_OR_WHERE_HEALTH_ASPECT = Semantic(
        id="HowOrWhereHealthAspect",
        ref="schema:HowOrWhereHealthAspect",
        text="""Information about how or where to find a topic. Also may contain location data that can be used for where to look for help if the topic is observed.""",
    )

    OFFER_CATALOG = Semantic(
        id="OfferCatalog",
        ref="schema:OfferCatalog",
        text="""An OfferCatalog is an ItemList that contains related Offers and/or further OfferCatalogs that are offeredBy the same provider.""",
    )

    PENCILER = Semantic(
        id="penciler",
        ref="schema:penciler",
        text="""The individual who draws the primary narrative artwork.""",
    )

    E_U_ENERGY_EFFICIENCY_CATEGORY_C = Semantic(
        id="EUEnergyEfficiencyCategoryC",
        ref="schema:EUEnergyEfficiencyCategoryC",
        text="""Represents EU Energy Efficiency Class C as defined in EU energy labeling regulations.""",
    )

    SUBSCRIBE_ACTION = Semantic(
        id="SubscribeAction",
        ref="schema:SubscribeAction",
        text="""The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates pushed to.\\n\\nRelated actions:\\n\\n* [[FollowAction]]: Unlike FollowAction, SubscribeAction implies that the subscriber acts as a passive agent being constantly/actively pushed for updates.\\n* [[RegisterAction]]: Unlike RegisterAction, SubscribeAction implies that the agent is interested in continuing receiving updates from the object.\\n* [[JoinAction]]: Unlike JoinAction, SubscribeAction implies that the agent is interested in continuing receiving updates from the object.""",
    )

    CROSS_SECTIONAL = Semantic(
        id="CrossSectional",
        ref="schema:CrossSectional",
        text="""Studies carried out on pre-existing data (usually from \'snapshot\' surveys), such as that collected by the Census Bureau. Sometimes called Prevalence Studies.""",
    )

    EPISODE = Semantic(
        id="episode",
        ref="schema:episode",
        text="""An episode of a tv, radio or game media within a series or season.""",
    )

    PATHOLOGY_TEST = Semantic(
        id="PathologyTest",
        ref="schema:PathologyTest",
        text="""A medical test performed by a laboratory that typically involves examination of a tissue sample by a pathologist.""",
    )

    READ_BY = Semantic(
        id="readBy",
        ref="schema:readBy",
        text="""A person who reads (performs) the audiobook.""",
    )

    BOOK_EDITION = Semantic(
        id="bookEdition", ref="schema:bookEdition", text="""The edition of the book."""
    )

    BODY_OF_WATER = Semantic(
        id="BodyOfWater",
        ref="schema:BodyOfWater",
        text="""A body of water, such as a sea, ocean, or lake.""",
    )

    ANTAGONIST = Semantic(
        id="antagonist",
        ref="schema:antagonist",
        text="""The muscle whose action counteracts the specified muscle.""",
    )

    HEALTH_CONDITION = Semantic(
        id="healthCondition",
        ref="schema:healthCondition",
        text="""Specifying the health condition(s) of a patient, medical study, or other target audience.""",
    )

    WEARABLE_SIZE_SYSTEM_F_R = Semantic(
        id="WearableSizeSystemFR",
        ref="schema:WearableSizeSystemFR",
        text="""French size system for wearables.""",
    )

    WEARABLE_SIZE_GROUP_PETITE = Semantic(
        id="WearableSizeGroupPetite",
        ref="schema:WearableSizeGroupPetite",
        text="""Size group "Petite" for wearables.""",
    )

    WEARABLE_SIZE_GROUP_MISSES = Semantic(
        id="WearableSizeGroupMisses",
        ref="schema:WearableSizeGroupMisses",
        text="""Size group "Misses" (also known as "Missy") for wearables.""",
    )

    MOUNTAIN = Semantic(
        id="Mountain",
        ref="schema:Mountain",
        text="""A mountain, like Mount Whitney or Mount Everest.""",
    )

    RENTAL_VEHICLE_USAGE = Semantic(
        id="RentalVehicleUsage",
        ref="schema:RentalVehicleUsage",
        text="""Indicates the usage of the vehicle as a rental car.""",
    )

    INCLUDES_HEALTH_PLAN_FORMULARY = Semantic(
        id="includesHealthPlanFormulary",
        ref="schema:includesHealthPlanFormulary",
        text="""Formularies covered by this plan.""",
    )

    MERCHANT = Semantic(
        id="merchant",
        ref="schema:merchant",
        text="""\'merchant\' is an out-dated term for \'seller\'.""",
    )

    PUBLISHER_IMPRINT = Semantic(
        id="publisherImprint",
        ref="schema:publisherImprint",
        text="""The publishing division which published the comic.""",
    )

    A_P_I_REFERENCE = Semantic(
        id="APIReference",
        ref="schema:APIReference",
        text="""Reference documentation for application programming interfaces (APIs).""",
    )

    NONPROFIT501C7 = Semantic(
        id="Nonprofit501c7",
        ref="schema:Nonprofit501c7",
        text="""Nonprofit501c7: Non-profit type referring to Social and Recreational Clubs.""",
    )

    LANDMARKS_OR_HISTORICAL_BUILDINGS = Semantic(
        id="LandmarksOrHistoricalBuildings",
        ref="schema:LandmarksOrHistoricalBuildings",
        text="""An historical landmark or building.""",
    )

    DIET = Semantic(
        id="Diet",
        ref="schema:Diet",
        text="""A strategy of regulating the intake of food to achieve or maintain a specific health-related goal.""",
    )

    BIO_CHEM_INTERACTION = Semantic(
        id="bioChemInteraction",
        ref="schema:bioChemInteraction",
        text="""A BioChemEntity that is known to interact with this item.""",
    )

    SECONDARY_PREVENTION = Semantic(
        id="secondaryPrevention",
        ref="schema:secondaryPrevention",
        text="""A preventative therapy used to prevent reoccurrence of the medical condition after an initial episode of the condition.""",
    )

    DAY_OF_WEEK = Semantic(
        id="dayOfWeek",
        ref="schema:dayOfWeek",
        text="""The day of the week for which these opening hours are valid.""",
    )

    CABLE_OR_SATELLITE_SERVICE = Semantic(
        id="CableOrSatelliteService",
        ref="schema:CableOrSatelliteService",
        text="""A service which provides access to media programming like TV or radio. Access may be via cable or satellite.""",
    )

    ITEM_CONDITION = Semantic(
        id="itemCondition",
        ref="schema:itemCondition",
        text="""A predefined value from OfferItemCondition specifying the condition of the product or service, or the products or services included in the offer. Also used for product return policies to specify the condition of products accepted for returns.""",
    )

    MEDICAL_CONDITION = Semantic(
        id="MedicalCondition",
        ref="schema:MedicalCondition",
        text="""Any condition of the human body that affects the normal functioning of a person, whether physically or mentally. Includes diseases, injuries, disabilities, disorders, syndromes, etc.""",
    )

    BUS_STOP = Semantic(id="BusStop", ref="schema:BusStop", text="""A bus stop.""")

    OFFER = Semantic(
        id="Offer",
        ref="schema:Offer",
        text="""An offer to transfer some rights to an item or to provide a service — for example, an offer to sell tickets to an event, to rent the DVD of a movie, to stream a TV show over the internet, to repair a motorcycle, or to loan a book.\\n\\nNote: As the [[businessFunction]] property, which identifies the form of offer (e.g. sell, lease, repair, dispose), defaults to http://purl.org/goodrelations/v1#Sell; an Offer without a defined businessFunction value can be assumed to be an offer to sell.\\n\\nFor [GTIN](http://www.gs1.org/barcodes/technical/idkeys/gtin)-related fields, see [Check Digit calculator](http://www.gs1.org/barcodes/support/check_digit_calculator) and [validation guide](http://www.gs1us.org/resources/standards/gtin-validation-guide) from [GS1](http://www.gs1.org/).""",
    )

    SEEKS = Semantic(
        id="seeks",
        ref="schema:seeks",
        text="""A pointer to products or services sought by the organization or person (demand).""",
    )

    CEMETERY = Semantic(id="Cemetery", ref="schema:Cemetery", text="""A graveyard.""")

    BUSINESS_EVENT = Semantic(
        id="BusinessEvent",
        ref="schema:BusinessEvent",
        text="""Event type: Business event.""",
    )

    RELATED_CONDITION = Semantic(
        id="relatedCondition",
        ref="schema:relatedCondition",
        text="""A medical condition associated with this anatomy.""",
    )

    COOK_ACTION = Semantic(
        id="CookAction",
        ref="schema:CookAction",
        text="""The act of producing/preparing food.""",
    )

    REMIX_ALBUM = Semantic(
        id="RemixAlbum", ref="schema:RemixAlbum", text="""RemixAlbum."""
    )

    PAYMENT_URL = Semantic(
        id="paymentUrl",
        ref="schema:paymentUrl",
        text="""The URL for sending a payment.""",
    )

    TARGET_PLATFORM = Semantic(
        id="targetPlatform",
        ref="schema:targetPlatform",
        text="""Type of app development: phone, Metro style, desktop, XBox, etc.""",
    )

    SOURCED_FROM = Semantic(
        id="sourcedFrom",
        ref="schema:sourcedFrom",
        text="""The neurological pathway that originates the neurons.""",
    )

    NONPROFIT501C21 = Semantic(
        id="Nonprofit501c21",
        ref="schema:Nonprofit501c21",
        text="""Nonprofit501c21: Non-profit type referring to Black Lung Benefit Trusts.""",
    )

    INKER = Semantic(
        id="inker",
        ref="schema:inker",
        text="""The individual who traces over the pencil drawings in ink after pencils are complete.""",
    )

    RECIPE = Semantic(
        id="Recipe",
        ref="schema:Recipe",
        text="""A recipe. For dietary restrictions covered by the recipe, a few common restrictions are enumerated via [[suitableForDiet]]. The [[keywords]] property can also be used to add more detail.""",
    )

    ALLOCATE_ACTION = Semantic(
        id="AllocateAction",
        ref="schema:AllocateAction",
        text="""The act of organizing tasks/objects/events by associating resources to it.""",
    )

    CONTACT_POINTS = Semantic(
        id="contactPoints",
        ref="schema:contactPoints",
        text="""A contact point for a person or organization.""",
    )

    TICKETED_SEAT = Semantic(
        id="ticketedSeat",
        ref="schema:ticketedSeat",
        text="""The seat associated with the ticket.""",
    )

    ACCESSIBILITY_A_P_I = Semantic(
        id="accessibilityAPI",
        ref="schema:accessibilityAPI",
        text="""Indicates that the resource is compatible with the referenced accessibility API ([WebSchemas wiki lists possible values](http://www.w3.org/wiki/WebSchemas/Accessibility)).""",
    )

    DEPARTURE_STATION = Semantic(
        id="departureStation",
        ref="schema:departureStation",
        text="""The station from which the train departs.""",
    )

    MAP = Semantic(id="map", ref="schema:map", text="""A URL to a map of the place.""")

    MEDICAL_GUIDELINE_CONTRAINDICATION = Semantic(
        id="MedicalGuidelineContraindication",
        ref="schema:MedicalGuidelineContraindication",
        text="""A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound.""",
    )

    LEGAL_NAME = Semantic(
        id="legalName",
        ref="schema:legalName",
        text="""The official name of the organization, e.g. the registered company name.""",
    )

    ORIGINAL_SHIPPING_FEES = Semantic(
        id="OriginalShippingFees",
        ref="schema:OriginalShippingFees",
        text="""Specifies that the customer must pay the original shipping costs when returning a product.""",
    )

    NONPROFIT501C27 = Semantic(
        id="Nonprofit501c27",
        ref="schema:Nonprofit501c27",
        text="""Nonprofit501c27: Non-profit type referring to State-Sponsored Workers\' Compensation Reinsurance Organizations.""",
    )

    TARGET_PRODUCT = Semantic(
        id="targetProduct",
        ref="schema:targetProduct",
        text="""Target Operating System / Product to which the code applies.  If applies to several versions, just the product name can be used.""",
    )

    RELATED_STRUCTURE = Semantic(
        id="relatedStructure",
        ref="schema:relatedStructure",
        text="""Related anatomical structure(s) that are not part of the system but relate or connect to it, such as vascular bundles associated with an organ system.""",
    )

    MENU = Semantic(
        id="Menu",
        ref="schema:Menu",
        text="""A structured representation of food or drink items available from a FoodEstablishment.""",
    )

    INVENTORY_LEVEL = Semantic(
        id="inventoryLevel",
        ref="schema:inventoryLevel",
        text="""The current approximate inventory level for the item or items.""",
    )

    LOW_SALT_DIET = Semantic(
        id="LowSaltDiet",
        ref="schema:LowSaltDiet",
        text="""A diet focused on reduced sodium intake.""",
    )

    ELEMENTARY_SCHOOL = Semantic(
        id="ElementarySchool",
        ref="schema:ElementarySchool",
        text="""An elementary school.""",
    )

    VERSION = Semantic(
        id="version",
        ref="schema:version",
        text="""The version of the CreativeWork embodied by a specified resource.""",
    )

    PARENT_AUDIENCE = Semantic(
        id="ParentAudience",
        ref="schema:ParentAudience",
        text="""A set of characteristics describing parents, who can be interested in viewing some content.""",
    )

    EDUCATIONAL_ROLE = Semantic(
        id="educationalRole",
        ref="schema:educationalRole",
        text="""An educationalRole of an EducationalAudience.""",
    )

    EVENT_SCHEDULE = Semantic(
        id="eventSchedule",
        ref="schema:eventSchedule",
        text="""Associates an [[Event]] with a [[Schedule]]. There are circumstances where it is preferable to share a schedule for a series of
      repeating events rather than data on the individual events themselves. For example, a website or application might prefer to publish a schedule for a weekly
      gym class rather than provide data on every event. A schedule could be processed by applications to add forthcoming events to a calendar. An [[Event]] that
      is associated with a [[Schedule]] using this property should not have [[startDate]] or [[endDate]] properties. These are instead defined within the associated
      [[Schedule]], this avoids any ambiguity for clients using the data. The property might have repeated values to specify different schedules, e.g. for different months
      or seasons.""",
    )

    DATASET = Semantic(
        id="Dataset",
        ref="schema:Dataset",
        text="""A body of structured information describing some topic(s) of interest.""",
    )

    FUNGUS = Semantic(id="Fungus", ref="schema:Fungus", text="""Pathogenic fungus.""")

    COURSE = Semantic(
        id="course",
        ref="schema:course",
        text="""A sub property of location. The course where this action was taken.""",
    )

    COURTHOUSE = Semantic(
        id="Courthouse", ref="schema:Courthouse", text="""A courthouse."""
    )

    REAR_WHEEL_DRIVE_CONFIGURATION = Semantic(
        id="RearWheelDriveConfiguration",
        ref="schema:RearWheelDriveConfiguration",
        text="""Real-wheel drive is a transmission layout where the engine drives the rear wheels.""",
    )

    RESTOCKING_FEE = Semantic(
        id="restockingFee",
        ref="schema:restockingFee",
        text="""Use [[MonetaryAmount]] to specify a fixed restocking fee for product returns, or use [[Number]] to specify a percentage of the product price paid by the customer.""",
    )

    RADIO_SEASON = Semantic(
        id="RadioSeason",
        ref="schema:RadioSeason",
        text="""Season dedicated to radio broadcast and associated online delivery.""",
    )

    ICAO_CODE = Semantic(
        id="icaoCode", ref="schema:icaoCode", text="""ICAO identifier for an airport."""
    )

    COOKING_METHOD = Semantic(
        id="cookingMethod",
        ref="schema:cookingMethod",
        text="""The method of cooking, such as Frying, Steaming, ...""",
    )

    NONPROFIT501C24 = Semantic(
        id="Nonprofit501c24",
        ref="schema:Nonprofit501c24",
        text="""Nonprofit501c24: Non-profit type referring to Section 4049 ERISA Trusts.""",
    )

    N_L_NONPROFIT_TYPE = Semantic(
        id="NLNonprofitType",
        ref="schema:NLNonprofitType",
        text="""NLNonprofitType: Non-profit organization type originating from the Netherlands.""",
    )

    ORDER_DELIVERED = Semantic(
        id="OrderDelivered",
        ref="schema:OrderDelivered",
        text="""OrderStatus representing successful delivery of an order.""",
    )

    FINANCIAL_AID_ELIGIBLE = Semantic(
        id="financialAidEligible",
        ref="schema:financialAidEligible",
        text="""A financial aid type or program which students may use to pay for tuition or fees associated with the program.""",
    )

    ABOUT_PAGE = Semantic(
        id="AboutPage", ref="schema:AboutPage", text="""Web page type: About page."""
    )

    DRUG_STRENGTH = Semantic(
        id="DrugStrength",
        ref="schema:DrugStrength",
        text="""A specific strength in which a medical drug is available in a specific country.""",
    )

    AQUARIUM = Semantic(id="Aquarium", ref="schema:Aquarium", text="""Aquarium.""")

    LIBRARY = Semantic(id="Library", ref="schema:Library", text="""A library.""")

    TAXI = Semantic(id="Taxi", ref="schema:Taxi", text="""A taxi.""")

    APPLICANT_LOCATION_REQUIREMENTS = Semantic(
        id="applicantLocationRequirements",
        ref="schema:applicantLocationRequirements",
        text="""The location(s) applicants can apply from. This is usually used for telecommuting jobs where the applicant does not need to be in a physical office. Note: This should not be used for citizenship or work visa requirements.""",
    )

    BODY_LOCATION = Semantic(
        id="bodyLocation",
        ref="schema:bodyLocation",
        text="""Location in the body of the anatomical structure.""",
    )

    BEST_RATING = Semantic(
        id="bestRating",
        ref="schema:bestRating",
        text="""The highest value allowed in this rating system. If bestRating is omitted, 5 is assumed.""",
    )

    CHECK_IN_ACTION = Semantic(
        id="CheckInAction",
        ref="schema:CheckInAction",
        text="""The act of an agent communicating (service provider, social media, etc) their arrival by registering/confirming for a previously reserved service (e.g. flight check in) or at a place (e.g. hotel), possibly resulting in a result (boarding pass, etc).\\n\\nRelated actions:\\n\\n* [[CheckOutAction]]: The antonym of CheckInAction.\\n* [[ArriveAction]]: Unlike ArriveAction, CheckInAction implies that the agent is informing/confirming the start of a previously reserved service.\\n* [[ConfirmAction]]: Unlike ConfirmAction, CheckInAction implies that the agent is informing/confirming the *start* of a previously reserved service rather than its validity/existence.""",
    )

    INSTRUMENT = Semantic(
        id="instrument",
        ref="schema:instrument",
        text="""The object that helped the agent perform the action. e.g. John wrote a book with *a pen*.""",
    )

    LEARNING_RESOURCE_TYPE = Semantic(
        id="learningResourceType",
        ref="schema:learningResourceType",
        text="""The predominant type or kind characterizing the learning resource. For example, \'presentation\', \'handout\'.""",
    )

    POSTAL_CODE_RANGE = Semantic(
        id="postalCodeRange",
        ref="schema:postalCodeRange",
        text="""A defined range of postal codes.""",
    )

    MEDICAL_CLINIC = Semantic(
        id="MedicalClinic",
        ref="schema:MedicalClinic",
        text="""A facility, often associated with a hospital or medical school, that is devoted to the specific diagnosis and/or healthcare. Previously limited to outpatients but with evolution it may be open to inpatients as well.""",
    )

    ISSUED_BY = Semantic(
        id="issuedBy",
        ref="schema:issuedBy",
        text="""The organization issuing the ticket or permit.""",
    )

    PASSENGER_PRIORITY_STATUS = Semantic(
        id="passengerPriorityStatus",
        ref="schema:passengerPriorityStatus",
        text="""The priority status assigned to a passenger for security or boarding (e.g. FastTrack or Priority).""",
    )

    DATE_RECEIVED = Semantic(
        id="dateReceived",
        ref="schema:dateReceived",
        text="""The date/time the message was received if a single recipient exists.""",
    )

    ARTERY = Semantic(
        id="Artery",
        ref="schema:Artery",
        text="""A type of blood vessel that specifically carries blood away from the heart.""",
    )

    ADDITIONAL_PROPERTY = Semantic(
        id="additionalProperty",
        ref="schema:additionalProperty",
        text="""A property-value pair representing an additional characteristics of the entitity, e.g. a product feature or another characteristic for which there is no matching property in schema.org.\\n\\nNote: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.
""",
    )

    COMPETITOR = Semantic(
        id="competitor",
        ref="schema:competitor",
        text="""A competitor in a sports event.""",
    )

    INTERACT_ACTION = Semantic(
        id="InteractAction",
        ref="schema:InteractAction",
        text="""The act of interacting with another person or organization.""",
    )

    DIVERSITY_STAFFING_REPORT = Semantic(
        id="diversityStaffingReport",
        ref="schema:diversityStaffingReport",
        text="""For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]), a report on staffing diversity issues. In a news context this might be for example ASNE or RTDNA (US) reports, or self-reported.""",
    )

    MINIMUM_PAYMENT_DUE = Semantic(
        id="minimumPaymentDue",
        ref="schema:minimumPaymentDue",
        text="""The minimum payment required at this time.""",
    )

    CONVERSATION = Semantic(
        id="Conversation",
        ref="schema:Conversation",
        text="""One or more messages between organizations or people on a particular topic. Individual messages can be linked to the conversation with isPartOf or hasPart properties.""",
    )

    DRUG_CLASS = Semantic(
        id="drugClass",
        ref="schema:drugClass",
        text="""The class of drug this belongs to (e.g., statins).""",
    )

    INVESTMENT_FUND = Semantic(
        id="InvestmentFund",
        ref="schema:InvestmentFund",
        text="""A company or fund that gathers capital from a number of investors to create a pool of money that is then re-invested into stocks, bonds and other assets.""",
    )

    URL_TEMPLATE = Semantic(
        id="urlTemplate",
        ref="schema:urlTemplate",
        text="""An url template (RFC6570) that will be used to construct the target of the execution of the action.""",
    )

    ADVERTISER_CONTENT_ARTICLE = Semantic(
        id="AdvertiserContentArticle",
        ref="schema:AdvertiserContentArticle",
        text="""An [[Article]] that an external entity has paid to place or to produce to its specifications. Includes [advertorials](https://en.wikipedia.org/wiki/Advertorial), sponsored content, native advertising and other paid content.""",
    )

    TRANSFORMED_CONTENT = Semantic(
        id="TransformedContent",
        ref="schema:TransformedContent",
        text="""Content coded \'transformed content\' in a [[MediaReview]], considered in the context of how it was published or shared.

For a [[VideoObject]] to be \'transformed content\':  or all of the video has been manipulated to transform the footage itself. This category includes using tools like the Adobe Suite to change the speed of the video, add or remove visual elements or dub audio. Deepfakes are also a subset of transformation.

For an [[ImageObject]] to be transformed content\': Adding or deleting visual elements to give the image a different meaning with the intention to mislead.

For an [[ImageObject]] with embedded text to be \'transformed content\': Adding or deleting visual elements to give the image a different meaning with the intention to mislead.

For an [[AudioObject]] to be \'transformed content\': Part or all of the audio has been manipulated to alter the words or sounds, or the audio has been synthetically generated, such as to create a sound-alike voice.
""",
    )

    ANSWER = Semantic(
        id="Answer",
        ref="schema:Answer",
        text="""An answer offered to a question; perhaps correct, perhaps opinionated or wrong.""",
    )

    MEDICAL_EVIDENCE_LEVEL = Semantic(
        id="MedicalEvidenceLevel",
        ref="schema:MedicalEvidenceLevel",
        text="""Level of evidence for a medical guideline. Enumerated type.""",
    )

    RETURN_SHIPPING_FEES_AMOUNT = Semantic(
        id="returnShippingFeesAmount",
        ref="schema:returnShippingFeesAmount",
        text="""Amount of shipping costs for product returns (for any reason). Applicable when property [[returnFees]] equals [[ReturnShippingFees]].""",
    )

    DIETARY_SUPPLEMENT = Semantic(
        id="DietarySupplement",
        ref="schema:DietarySupplement",
        text="""A product taken by mouth that contains a dietary ingredient intended to supplement the diet. Dietary ingredients may include vitamins, minerals, herbs or other botanicals, amino acids, and substances such as enzymes, organ tissues, glandulars and metabolites.""",
    )

    START_TIME = Semantic(
        id="startTime",
        ref="schema:startTime",
        text="""The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from *January* to December. For media, including audio and video, it\'s the time offset of the start of a clip within a larger file.\\n\\nNote that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.""",
    )

    ORDER_PAYMENT_DUE = Semantic(
        id="OrderPaymentDue",
        ref="schema:OrderPaymentDue",
        text="""OrderStatus representing that payment is due on an order.""",
    )

    FRIDAY = Semantic(
        id="Friday",
        ref="schema:Friday",
        text="""The day of the week between Thursday and Saturday.""",
    )

    ROLE = Semantic(
        id="Role",
        ref="schema:Role",
        text="""Represents additional information about a relationship or property. For example a Role can be used to say that a \'member\' role linking some SportsTeam to a player occurred during a particular time period. Or that a Person\'s \'actor\' role in a Movie was for some particular characterName. Such properties can be attached to a Role entity, which is then associated with the main entities using ordinary properties like \'member\' or \'actor\'.\\n\\nSee also [blog post](http://blog.schema.org/2014/06/introducing-role.html).""",
    )

    TECH_ARTICLE = Semantic(
        id="TechArticle",
        ref="schema:TechArticle",
        text="""A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc.""",
    )

    GENETIC = Semantic(
        id="Genetic",
        ref="schema:Genetic",
        text="""A specific branch of medical science that pertains to hereditary transmission and the variation of inherited characteristics and disorders.""",
    )

    CORPORATION = Semantic(
        id="Corporation",
        ref="schema:Corporation",
        text="""Organization: A business corporation.""",
    )

    COMMENT_PERMISSION = Semantic(
        id="CommentPermission",
        ref="schema:CommentPermission",
        text="""Permission to add comments to the document.""",
    )

    GOVERNMENT_ORGANIZATION = Semantic(
        id="GovernmentOrganization",
        ref="schema:GovernmentOrganization",
        text="""A governmental organization or agency.""",
    )

    DISCUSSION_URL = Semantic(
        id="discussionUrl",
        ref="schema:discussionUrl",
        text="""A link to the page containing the comments of the CreativeWork.""",
    )

    BROADCAST_EVENT = Semantic(
        id="BroadcastEvent",
        ref="schema:BroadcastEvent",
        text="""An over the air or online broadcast event.""",
    )

    STAGED_CONTENT = Semantic(
        id="StagedContent",
        ref="schema:StagedContent",
        text="""Content coded \'staged content\' in a [[MediaReview]], considered in the context of how it was published or shared.

For a [[VideoObject]] to be \'staged content\': A video that has been created using actors or similarly contrived.

For an [[ImageObject]] to be \'staged content\': An image that was created using actors or similarly contrived, such as a screenshot of a fake tweet.

For an [[ImageObject]] with embedded text to be \'staged content\': An image that was created using actors or similarly contrived, such as a screenshot of a fake tweet.

For an [[AudioObject]] to be \'staged content\': Audio that has been created using actors or similarly contrived.
""",
    )

    TOLL_FREE = Semantic(
        id="TollFree",
        ref="schema:TollFree",
        text="""The associated telephone number is toll free.""",
    )

    PAYMENT_AUTOMATICALLY_APPLIED = Semantic(
        id="PaymentAutomaticallyApplied",
        ref="schema:PaymentAutomaticallyApplied",
        text="""An automatic payment system is in place and will be used.""",
    )

    BUSINESS_DAYS = Semantic(
        id="businessDays",
        ref="schema:businessDays",
        text="""Days of the week when the merchant typically operates, indicated via opening hours markup.""",
    )

    SERVICE = Semantic(
        id="Service",
        ref="schema:Service",
        text="""A service provided by an organization, e.g. delivery service, print services, etc.""",
    )

    CANAL = Semantic(
        id="Canal", ref="schema:Canal", text="""A canal, like the Panama Canal."""
    )

    PROVIDER = Semantic(
        id="provider",
        ref="schema:provider",
        text="""The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.""",
    )

    AVAILABLE_CHANNEL = Semantic(
        id="availableChannel",
        ref="schema:availableChannel",
        text="""A means of accessing the service (e.g. a phone bank, a web site, a location, etc.).""",
    )

    POPULATION_TYPE = Semantic(
        id="populationType",
        ref="schema:populationType",
        text="""Indicates the populationType common to all members of a [[StatisticalPopulation]].""",
    )

    EXERCISE_COURSE = Semantic(
        id="exerciseCourse",
        ref="schema:exerciseCourse",
        text="""A sub property of location. The course where this action was taken.""",
    )

    OPENING_HOURS_SPECIFICATION = Semantic(
        id="OpeningHoursSpecification",
        ref="schema:OpeningHoursSpecification",
        text="""A structured value providing information about the opening hours of a place or a certain service inside a place.\\n\\n
The place is __open__ if the [[opens]] property is specified, and __closed__ otherwise.\\n\\nIf the value for the [[closes]] property is less than the value for the [[opens]] property then the hour range is assumed to span over the next day.
      """,
    )

    LINK_ROLE = Semantic(
        id="LinkRole",
        ref="schema:LinkRole",
        text="""A Role that represents a Web link e.g. as expressed via the \'url\' property. Its linkRelationship property can indicate URL-based and plain textual link types e.g. those in IANA link registry or others such as \'amphtml\'. This structure provides a placeholder where details from HTML\'s link element can be represented outside of HTML, e.g. in JSON-LD feeds.""",
    )

    PLACEBO_CONTROLLED_TRIAL = Semantic(
        id="PlaceboControlledTrial",
        ref="schema:PlaceboControlledTrial",
        text="""A placebo-controlled trial design.""",
    )

    APPEARANCE = Semantic(
        id="Appearance",
        ref="schema:Appearance",
        text="""Appearance assessment with clinical examination.""",
    )

    E_U_ENERGY_EFFICIENCY_CATEGORY_G = Semantic(
        id="EUEnergyEfficiencyCategoryG",
        ref="schema:EUEnergyEfficiencyCategoryG",
        text="""Represents EU Energy Efficiency Class G as defined in EU energy labeling regulations.""",
    )

    RECOGNIZED_BY = Semantic(
        id="recognizedBy",
        ref="schema:recognizedBy",
        text="""An organization that acknowledges the validity, value or utility of a credential. Note: recognition may include a process of quality assurance or accreditation.""",
    )

    LOSER = Semantic(
        id="loser",
        ref="schema:loser",
        text="""A sub property of participant. The loser of the action.""",
    )

    INSTALL_ACTION = Semantic(
        id="InstallAction",
        ref="schema:InstallAction",
        text="""The act of installing an application.""",
    )

    RELATED_THERAPY = Semantic(
        id="relatedTherapy",
        ref="schema:relatedTherapy",
        text="""A medical therapy related to this anatomy.""",
    )

    BUY_ACTION = Semantic(
        id="BuyAction",
        ref="schema:BuyAction",
        text="""The act of giving money to a seller in exchange for goods or services rendered. An agent buys an object, product, or service from a seller for a price. Reciprocal of SellAction.""",
    )

    DRIVE_WHEEL_CONFIGURATION_VALUE = Semantic(
        id="DriveWheelConfigurationValue",
        ref="schema:DriveWheelConfigurationValue",
        text="""A value indicating which roadwheels will receive torque.""",
    )

    DELIVERY_METHOD = Semantic(
        id="deliveryMethod",
        ref="schema:deliveryMethod",
        text="""A sub property of instrument. The method of delivery.""",
    )

    OCEAN_BODY_OF_WATER = Semantic(
        id="OceanBodyOfWater",
        ref="schema:OceanBodyOfWater",
        text="""An ocean (for example, the Pacific).""",
    )

    BONE = Semantic(
        id="Bone",
        ref="schema:Bone",
        text="""Rigid connective tissue that comprises up the skeletal structure of the human body.""",
    )

    SIZE_GROUP_ENUMERATION = Semantic(
        id="SizeGroupEnumeration",
        ref="schema:SizeGroupEnumeration",
        text="""Enumerates common size groups for various product categories.""",
    )

    PAYMENT_METHOD = Semantic(
        id="paymentMethod",
        ref="schema:paymentMethod",
        text="""The name of the credit card or other method of payment for the order.""",
    )

    VIEW_ACTION = Semantic(
        id="ViewAction",
        ref="schema:ViewAction",
        text="""The act of consuming static visual content.""",
    )

    HOME_LOCATION = Semantic(
        id="homeLocation",
        ref="schema:homeLocation",
        text="""A contact location for a person\'s residence.""",
    )

    ACCEPTED_ANSWER = Semantic(
        id="acceptedAnswer",
        ref="schema:acceptedAnswer",
        text="""The answer(s) that has been accepted as best, typically on a Question/Answer site. Sites vary in their selection mechanisms, e.g. drawing on community opinion and/or the view of the Question author.""",
    )

    PERCUTANEOUS_PROCEDURE = Semantic(
        id="PercutaneousProcedure",
        ref="schema:PercutaneousProcedure",
        text="""A type of medical procedure that involves percutaneous techniques, where access to organs or tissue is achieved via needle-puncture of the skin. For example, catheter-based procedures like stent delivery.""",
    )

    SIGN_DETECTED = Semantic(
        id="signDetected",
        ref="schema:signDetected",
        text="""A sign detected by the test.""",
    )

    BOOKING_TIME = Semantic(
        id="bookingTime",
        ref="schema:bookingTime",
        text="""The date and time the reservation was booked.""",
    )

    PUBLIC_TRANSPORT_CLOSURES_INFO = Semantic(
        id="publicTransportClosuresInfo",
        ref="schema:publicTransportClosuresInfo",
        text="""Information about public transport closures.""",
    )

    DIGITAL_DOCUMENT_PERMISSION = Semantic(
        id="DigitalDocumentPermission",
        ref="schema:DigitalDocumentPermission",
        text="""A permission for a particular person or group to access a particular file.""",
    )

    WEARABLE_SIZE_GROUP_TALL = Semantic(
        id="WearableSizeGroupTall",
        ref="schema:WearableSizeGroupTall",
        text="""Size group "Tall" for wearables.""",
    )

    CLAIM_REVIEW = Semantic(
        id="ClaimReview",
        ref="schema:ClaimReview",
        text="""A fact-checking review of claims made (or reported) in some creative work (referenced via itemReviewed).""",
    )

    PERFORMANCE_ROLE = Semantic(
        id="PerformanceRole",
        ref="schema:PerformanceRole",
        text="""A PerformanceRole is a Role that some entity places with regard to a theatrical performance, e.g. in a Movie, TVSeries etc.""",
    )

    INVOICE_PRICE = Semantic(
        id="InvoicePrice",
        ref="schema:InvoicePrice",
        text="""Represents the invoice price of an offered product.""",
    )

    S_R_P = Semantic(
        id="SRP",
        ref="schema:SRP",
        text="""Represents the suggested retail price ("SRP") of an offered product.""",
    )

    LYRICIST = Semantic(
        id="lyricist", ref="schema:lyricist", text="""The person who wrote the words."""
    )

    UN_REGISTER_ACTION = Semantic(
        id="UnRegisterAction",
        ref="schema:UnRegisterAction",
        text="""The act of un-registering from a service.\\n\\nRelated actions:\\n\\n* [[RegisterAction]]: antonym of UnRegisterAction.\\n* [[LeaveAction]]: Unlike LeaveAction, UnRegisterAction implies that you are unregistering from a service you werer previously registered, rather than leaving a team/group of people.""",
    )

    IN_FORCE = Semantic(
        id="InForce",
        ref="schema:InForce",
        text="""Indicates that a legislation is in force.""",
    )

    F_D_ANOT_EVALUATED = Semantic(
        id="FDAnotEvaluated",
        ref="schema:FDAnotEvaluated",
        text="""A designation that the drug in question has not been assigned a pregnancy category designation by the US FDA.""",
    )

    AMOUNT_OF_THIS_GOOD = Semantic(
        id="amountOfThisGood",
        ref="schema:amountOfThisGood",
        text="""The quantity of the goods included in the offer.""",
    )

    PROVIDES_BROADCAST_SERVICE = Semantic(
        id="providesBroadcastService",
        ref="schema:providesBroadcastService",
        text="""The BroadcastService offered on this channel.""",
    )

    FREQUENCY = Semantic(
        id="frequency",
        ref="schema:frequency",
        text="""How often the dose is taken, e.g. \'daily\'.""",
    )

    F_D_ACATEGORY_B = Semantic(
        id="FDAcategoryB",
        ref="schema:FDAcategoryB",
        text="""A designation by the US FDA signifying that animal reproduction studies have failed to demonstrate a risk to the fetus and there are no adequate and well-controlled studies in pregnant women.""",
    )

    BIOMECHNICAL_CLASS = Semantic(
        id="biomechnicalClass",
        ref="schema:biomechnicalClass",
        text="""The biomechanical properties of the bone.""",
    )

    HEALTH_TOPIC_CONTENT = Semantic(
        id="HealthTopicContent",
        ref="schema:HealthTopicContent",
        text="""[[HealthTopicContent]] is [[WebContent]] that is about some aspect of a health topic, e.g. a condition, its symptoms or treatments. Such content may be comprised of several parts or sections and use different types of media. Multiple instances of [[WebContent]] (and hence [[HealthTopicContent]]) can be related using [[hasPart]] / [[isPartOf]] where there is some kind of content hierarchy, and their content described with [[about]] and [[mentions]] e.g. building upon the existing [[MedicalCondition]] vocabulary.
  """,
    )

    ORDER_ACTION = Semantic(
        id="OrderAction",
        ref="schema:OrderAction",
        text="""An agent orders an object/product/service to be delivered/sent.""",
    )

    NONPROFIT501D = Semantic(
        id="Nonprofit501d",
        ref="schema:Nonprofit501d",
        text="""Nonprofit501d: Non-profit type referring to Religious and Apostolic Associations.""",
    )

    INSTRUCTOR = Semantic(
        id="instructor",
        ref="schema:instructor",
        text="""A person assigned to instruct or provide instructional assistance for the [[CourseInstance]].""",
    )

    WEARABLE_SIZE_GROUP_WOMENS = Semantic(
        id="WearableSizeGroupWomens",
        ref="schema:WearableSizeGroupWomens",
        text="""Size group "Womens" for wearables.""",
    )

    INFECTIOUS = Semantic(
        id="Infectious",
        ref="schema:Infectious",
        text="""Something in medical science that pertains to infectious diseases i.e caused by bacterial, viral, fungal or parasitic infections.""",
    )

    CLASS = Semantic(
        id="Class",
        ref="schema:Class",
        text="""A class, also often called a \'Type\'; equivalent to rdfs:Class.""",
    )

    E_U_ENERGY_EFFICIENCY_CATEGORY_D = Semantic(
        id="EUEnergyEfficiencyCategoryD",
        ref="schema:EUEnergyEfficiencyCategoryD",
        text="""Represents EU Energy Efficiency Class D as defined in EU energy labeling regulations.""",
    )

    INTEGER = Semantic(
        id="Integer", ref="schema:Integer", text="""Data type: Integer."""
    )

    OCCUPATIONAL_CATEGORY = Semantic(
        id="occupationalCategory",
        ref="schema:occupationalCategory",
        text="""A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html), [ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.\\n
Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.""",
    )

    IS_VARIANT_OF = Semantic(
        id="isVariantOf",
        ref="schema:isVariantOf",
        text="""Indicates the kind of product that this is a variant of. In the case of [[ProductModel]], this is a pointer (from a ProductModel) to a base product from which this product is a variant. It is safe to infer that the variant inherits all product features from the base model, unless defined locally. This is not transitive. In the case of a [[ProductGroup]], the group description also serves as a template, representing a set of Products that vary on explicitly defined, specific dimensions only (so it defines both a set of variants, as well as which values distinguish amongst those variants). When used with [[ProductGroup]], this property can apply to any [[Product]] included in the group.""",
    )

    ONE_TIME_PAYMENTS = Semantic(
        id="OneTimePayments",
        ref="schema:OneTimePayments",
        text="""OneTimePayments: this is a benefit for one-time payments for individuals.""",
    )

    FLOAT = Semantic(
        id="Float", ref="schema:Float", text="""Data type: Floating number."""
    )

    DRUG = Semantic(
        id="drug",
        ref="schema:drug",
        text="""Specifying a drug or medicine used in a medication procedure.""",
    )

    PUBLISHED_ON = Semantic(
        id="publishedOn",
        ref="schema:publishedOn",
        text="""A broadcast service associated with the publication event.""",
    )

    CALL_SIGN = Semantic(
        id="callSign",
        ref="schema:callSign",
        text="""A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting and radio communications to identify people, radio and TV stations, or vehicles.""",
    )

    QUALITATIVE_VALUE = Semantic(
        id="QualitativeValue",
        ref="schema:QualitativeValue",
        text="""A predefined value for a product characteristic, e.g. the power cord plug type \'US\' or the garment sizes \'S\', \'M\', \'L\', and \'XL\'.""",
    )

    MUSIC_COMPOSITION_FORM = Semantic(
        id="musicCompositionForm",
        ref="schema:musicCompositionForm",
        text="""The type of composition (e.g. overture, sonata, symphony, etc.).""",
    )

    MEAL_SERVICE = Semantic(
        id="mealService",
        ref="schema:mealService",
        text="""Description of the meals that will be provided or available for purchase.""",
    )

    READ_ACTION = Semantic(
        id="ReadAction",
        ref="schema:ReadAction",
        text="""The act of consuming written content.""",
    )

    RELATED_TOPICS_HEALTH_ASPECT = Semantic(
        id="RelatedTopicsHealthAspect",
        ref="schema:RelatedTopicsHealthAspect",
        text="""Other prominent or relevant topics tied to the main topic.""",
    )

    SPORTS_TEAM = Semantic(
        id="SportsTeam", ref="schema:SportsTeam", text="""Organization: Sports team."""
    )

    UNNAMED_SOURCES_POLICY = Semantic(
        id="unnamedSourcesPolicy",
        ref="schema:unnamedSourcesPolicy",
        text="""For an [[Organization]] (typically a [[NewsMediaOrganization]]), a statement about policy on use of unnamed sources and the decision process required.""",
    )

    MEMORY_REQUIREMENTS = Semantic(
        id="memoryRequirements",
        ref="schema:memoryRequirements",
        text="""Minimum memory requirements.""",
    )

    GRANTEE = Semantic(
        id="grantee",
        ref="schema:grantee",
        text="""The person, organization, contact point, or audience that has been granted this permission.""",
    )

    PRODUCT_GROUP_I_D = Semantic(
        id="productGroupID",
        ref="schema:productGroupID",
        text="""Indicates a textual identifier for a ProductGroup.""",
    )

    USED_TO_DIAGNOSE = Semantic(
        id="usedToDiagnose",
        ref="schema:usedToDiagnose",
        text="""A condition the test is used to diagnose.""",
    )

    CODE = Semantic(
        id="code",
        ref="schema:code",
        text="""A medical code for the entity, taken from a controlled vocabulary or ontology such as ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.""",
    )

    GAME_SERVER = Semantic(
        id="gameServer",
        ref="schema:gameServer",
        text="""The server on which  it is possible to play the game.""",
    )

    BOARDING_GROUP = Semantic(
        id="boardingGroup",
        ref="schema:boardingGroup",
        text="""The airline-specific indicator of boarding order / preference.""",
    )

    SEARCH_RESULTS_PAGE = Semantic(
        id="SearchResultsPage",
        ref="schema:SearchResultsPage",
        text="""Web page type: Search results page.""",
    )

    NUMBER_OF_AVAILABLE_ACCOMMODATION_UNITS = Semantic(
        id="numberOfAvailableAccommodationUnits",
        ref="schema:numberOfAvailableAccommodationUnits",
        text="""Indicates the number of available accommodation units in an [[ApartmentComplex]], or the number of accommodation units for a specific [[FloorPlan]] (within its specific [[ApartmentComplex]]). See also [[numberOfAccommodationUnits]].""",
    )

    REGISTRY = Semantic(
        id="Registry", ref="schema:Registry", text="""A registry-based study design."""
    )

    PERIODICAL = Semantic(
        id="Periodical",
        ref="schema:Periodical",
        text="""A publication in any medium issued in successive parts bearing numerical or chronological designations and intended, such as a magazine, scholarly journal, or newspaper to continue indefinitely.\\n\\nSee also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).""",
    )

    CASSETTE_FORMAT = Semantic(
        id="CassetteFormat", ref="schema:CassetteFormat", text="""CassetteFormat."""
    )

    AVAILABLE_FROM = Semantic(
        id="availableFrom",
        ref="schema:availableFrom",
        text="""When the item is available for pickup from the store, locker, etc.""",
    )

    DISEASE_PREVENTION_INFO = Semantic(
        id="diseasePreventionInfo",
        ref="schema:diseasePreventionInfo",
        text="""Information about disease prevention.""",
    )

    MECHANISM_OF_ACTION = Semantic(
        id="mechanismOfAction",
        ref="schema:mechanismOfAction",
        text="""The specific biochemical interaction through which this drug or supplement produces its pharmacological effect.""",
    )

    CATEGORY_CODE = Semantic(
        id="CategoryCode", ref="schema:CategoryCode", text="""A Category Code."""
    )

    FOLLOWUP = Semantic(
        id="followup",
        ref="schema:followup",
        text="""Typical or recommended followup care after the procedure is performed.""",
    )

    COACH = Semantic(
        id="coach",
        ref="schema:coach",
        text="""A person that acts in a coaching role for a sports team.""",
    )

    WRITE_ACTION = Semantic(
        id="WriteAction",
        ref="schema:WriteAction",
        text="""The act of authoring written creative content.""",
    )

    COVERAGE_START_TIME = Semantic(
        id="coverageStartTime",
        ref="schema:coverageStartTime",
        text="""The time when the live blog will begin covering the Event. Note that coverage may begin before the Event\'s start time. The LiveBlogPosting may also be created before coverage begins.""",
    )

    PERFORM_ACTION = Semantic(
        id="PerformAction",
        ref="schema:PerformAction",
        text="""The act of participating in performance arts.""",
    )

    CHECKOUT_TIME = Semantic(
        id="checkoutTime",
        ref="schema:checkoutTime",
        text="""The latest someone may check out of a lodging establishment.""",
    )

    BLOOD_SUPPLY = Semantic(
        id="bloodSupply",
        ref="schema:bloodSupply",
        text="""The blood vessel that carries blood from the heart to the muscle.""",
    )

    DERMATOLOGY = Semantic(
        id="Dermatology",
        ref="schema:Dermatology",
        text="""A specific branch of medical science that pertains to diagnosis and treatment of disorders of skin.""",
    )

    CONTENT_SIZE = Semantic(
        id="contentSize",
        ref="schema:contentSize",
        text="""File size in (mega/kilo) bytes.""",
    )

    TRIP = Semantic(
        id="Trip",
        ref="schema:Trip",
        text="""A trip or journey. An itinerary of visits to one or more places.""",
    )

    FILE_FORMAT = Semantic(
        id="fileFormat",
        ref="schema:fileFormat",
        text="""Media type, typically MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml)) of the content e.g. application/zip of a SoftwareApplication binary. In cases where a CreativeWork has several media type representations, \'encoding\' can be used to indicate each MediaObject alongside particular fileFormat information. Unregistered or niche file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia entry.""",
    )

    SPORTS_CLUB = Semantic(
        id="SportsClub", ref="schema:SportsClub", text="""A sports club."""
    )

    PART_OF_TRIP = Semantic(
        id="partOfTrip",
        ref="schema:partOfTrip",
        text="""Identifies that this [[Trip]] is a subTrip of another Trip.  For example Day 1, Day 2, etc. of a multi-day trip.""",
    )

    REQUIRED_MIN_AGE = Semantic(
        id="requiredMinAge",
        ref="schema:requiredMinAge",
        text="""Audiences defined by a person\'s minimum age.""",
    )

    PERCENTILE10 = Semantic(
        id="percentile10",
        ref="schema:percentile10",
        text="""The 10th percentile value.""",
    )

    HOSTING_ORGANIZATION = Semantic(
        id="hostingOrganization",
        ref="schema:hostingOrganization",
        text="""The organization (airline, travelers\' club, etc.) the membership is made with.""",
    )

    WEB_A_P_I = Semantic(
        id="WebAPI",
        ref="schema:WebAPI",
        text="""An application programming interface accessible over Web/Internet technologies.""",
    )

    PRODUCER = Semantic(
        id="producer",
        ref="schema:producer",
        text="""The person or organization who produced the work (e.g. music album, movie, tv/radio series etc.).""",
    )

    RSVP_RESPONSE = Semantic(
        id="rsvpResponse",
        ref="schema:rsvpResponse",
        text="""The response (yes, no, maybe) to the RSVP.""",
    )

    VALID_IN = Semantic(
        id="validIn",
        ref="schema:validIn",
        text="""The geographic area where a permit or similar thing is valid.""",
    )

    NEGATIVE_NOTES = Semantic(
        id="negativeNotes",
        ref="schema:negativeNotes",
        text="""Indicates, in the context of a [[Review]] (e.g. framed as \'pro\' vs \'con\' considerations), negative considerations - either as unstructured text, or a list.""",
    )

    FREE_RETURN = Semantic(
        id="FreeReturn",
        ref="schema:FreeReturn",
        text="""Specifies that product returns are free of charge for the customer.""",
    )

    CITATION = Semantic(
        id="citation",
        ref="schema:citation",
        text="""A citation or reference to another creative work, such as another publication, web page, scholarly article, etc.""",
    )

    NONINVASIVE_PROCEDURE = Semantic(
        id="NoninvasiveProcedure",
        ref="schema:NoninvasiveProcedure",
        text="""A type of medical procedure that involves noninvasive techniques.""",
    )

    HOME_GOODS_STORE = Semantic(
        id="HomeGoodsStore", ref="schema:HomeGoodsStore", text="""A home goods store."""
    )

    SUB_RESERVATION = Semantic(
        id="subReservation",
        ref="schema:subReservation",
        text="""The individual reservations included in the package. Typically a repeated property.""",
    )

    EAT_ACTION = Semantic(
        id="EatAction",
        ref="schema:EatAction",
        text="""The act of swallowing solid objects.""",
    )

    CLAIM_REVIEWED = Semantic(
        id="claimReviewed",
        ref="schema:claimReviewed",
        text="""A short summary of the specific claims reviewed in a ClaimReview.""",
    )

    ARRIVAL_GATE = Semantic(
        id="arrivalGate",
        ref="schema:arrivalGate",
        text="""Identifier of the flight\'s arrival gate.""",
    )

    HOTEL = Semantic(
        id="Hotel",
        ref="schema:Hotel",
        text="""A hotel is an establishment that provides lodging paid on a short-term basis (Source: Wikipedia, the free encyclopedia, see http://en.wikipedia.org/wiki/Hotel).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
""",
    )

    MONEY_TRANSFER = Semantic(
        id="MoneyTransfer",
        ref="schema:MoneyTransfer",
        text="""The act of transferring money from one place to another place. This may occur electronically or physically.""",
    )

    CODE = Semantic(
        id="Code",
        ref="schema:Code",
        text="""Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates.""",
    )

    IMAGING_TEST = Semantic(
        id="ImagingTest",
        ref="schema:ImagingTest",
        text="""Any medical imaging modality typically used for diagnostic purposes.""",
    )

    MAP = Semantic(id="Map", ref="schema:Map", text="""A map.""")

    DIRECTORS = Semantic(
        id="directors",
        ref="schema:directors",
        text="""A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.""",
    )

    MASTHEAD = Semantic(
        id="masthead",
        ref="schema:masthead",
        text="""For a [[NewsMediaOrganization]], a link to the masthead page or a page listing top editorial management.""",
    )

    PLAY = Semantic(
        id="Play",
        ref="schema:Play",
        text="""A play is a form of literature, usually consisting of dialogue between characters, intended for theatrical performance rather than just reading. Note: A performance of a Play would be a [[TheaterEvent]] or [[BroadcastEvent]] - the *Play* being the [[workPerformed]].""",
    )

    BROADCAST_SERVICE_TIER = Semantic(
        id="broadcastServiceTier",
        ref="schema:broadcastServiceTier",
        text="""The type of service required to have access to the channel (e.g. Standard or Premium).""",
    )

    BROADCAST_FREQUENCY_VALUE = Semantic(
        id="broadcastFrequencyValue",
        ref="schema:broadcastFrequencyValue",
        text="""The frequency in MHz for a particular broadcast.""",
    )

    WEARABLE_SIZE_SYSTEM_M_X = Semantic(
        id="WearableSizeSystemMX",
        ref="schema:WearableSizeSystemMX",
        text="""Mexican size system for wearables.""",
    )

    TYPES_HEALTH_ASPECT = Semantic(
        id="TypesHealthAspect",
        ref="schema:TypesHealthAspect",
        text="""Categorization and other types related to a topic.""",
    )

    FOOD_SERVICE = Semantic(
        id="FoodService",
        ref="schema:FoodService",
        text="""A food service, like breakfast, lunch, or dinner.""",
    )

    TONGUE_WEIGHT = Semantic(
        id="tongueWeight",
        ref="schema:tongueWeight",
        text="""The permitted vertical load (TWR) of a trailer attached to the vehicle. Also referred to as Tongue Load Rating (TLR) or Vertical Load Rating (VLR)\\n\\nTypical unit code(s): KGM for kilogram, LBR for pound\\n\\n* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.\\n* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].\\n* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.""",
    )

    GOVERNMENT_PERMIT = Semantic(
        id="GovernmentPermit",
        ref="schema:GovernmentPermit",
        text="""A permit issued by a government agency.""",
    )

    VEHICLE_SEATING_CAPACITY = Semantic(
        id="vehicleSeatingCapacity",
        ref="schema:vehicleSeatingCapacity",
        text="""The number of passengers that can be seated in the vehicle, both in terms of the physical space available, and in terms of limitations set by law.\\n\\nTypical unit code(s): C62 for persons.""",
    )

    OFFER_FOR_PURCHASE = Semantic(
        id="OfferForPurchase",
        ref="schema:OfferForPurchase",
        text="""An [[OfferForPurchase]] in Schema.org represents an [[Offer]] to sell something, i.e. an [[Offer]] whose
  [[businessFunction]] is [sell](http://purl.org/goodrelations/v1#Sell.). See [Good Relations](https://en.wikipedia.org/wiki/GoodRelations) for
  background on the underlying concepts.
  """,
    )

    WEARABLE_SIZE_SYSTEM_G_S1 = Semantic(
        id="WearableSizeSystemGS1",
        ref="schema:WearableSizeSystemGS1",
        text="""GS1 (formerly NRF) size system for wearables.""",
    )

    CRITIC_REVIEW = Semantic(
        id="CriticReview",
        ref="schema:CriticReview",
        text="""A [[CriticReview]] is a more specialized form of Review written or published by a source that is recognized for its reviewing activities. These can include online columns, travel and food guides, TV and radio shows, blogs and other independent Web sites. [[CriticReview]]s are typically more in-depth and professionally written. For simpler, casually written user/visitor/viewer/customer reviews, it is more appropriate to use the [[UserReview]] type. Review aggregator sites such as Metacritic already separate out the site\'s user reviews from selected critic reviews that originate from third-party sources.""",
    )

    RESERVOIR = Semantic(
        id="Reservoir",
        ref="schema:Reservoir",
        text="""A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir.""",
    )

    MEASUREMENT_TYPE_ENUMERATION = Semantic(
        id="MeasurementTypeEnumeration",
        ref="schema:MeasurementTypeEnumeration",
        text="""Enumeration of common measurement types (or dimensions), for example "chest" for a person, "inseam" for pants, "gauge" for screws, or "wheel" for bicycles.""",
    )

    RESERVATION_FOR = Semantic(
        id="reservationFor",
        ref="schema:reservationFor",
        text="""The thing -- flight, event, restaurant,etc. being reserved.""",
    )

    ACTIVITY_FREQUENCY = Semantic(
        id="activityFrequency",
        ref="schema:activityFrequency",
        text="""How often one should engage in the activity.""",
    )

    MEDICAL_IMAGING_TECHNIQUE = Semantic(
        id="MedicalImagingTechnique",
        ref="schema:MedicalImagingTechnique",
        text="""Any medical imaging modality typically used for diagnostic purposes. Enumerated type.""",
    )

    HEALTH_PLAN_FORMULARY = Semantic(
        id="HealthPlanFormulary",
        ref="schema:HealthPlanFormulary",
        text="""For a given health insurance plan, the specification for costs and coverage of prescription drugs. """,
    )

    FOLLOW_ACTION = Semantic(
        id="FollowAction",
        ref="schema:FollowAction",
        text="""The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates polled from.\\n\\nRelated actions:\\n\\n* [[BefriendAction]]: Unlike BefriendAction, FollowAction implies that the connection is *not* necessarily reciprocal.\\n* [[SubscribeAction]]: Unlike SubscribeAction, FollowAction implies that the follower acts as an active agent constantly/actively polling for updates.\\n* [[RegisterAction]]: Unlike RegisterAction, FollowAction implies that the agent is interested in continuing receiving updates from the object.\\n* [[JoinAction]]: Unlike JoinAction, FollowAction implies that the agent is interested in getting updates from the object.\\n* [[TrackAction]]: Unlike TrackAction, FollowAction refers to the polling of updates of all aspects of animate objects rather than the location of inanimate objects (e.g. you track a package, but you don\'t follow it).""",
    )

    TOURIST_TRIP = Semantic(
        id="TouristTrip",
        ref="schema:TouristTrip",
        text="""A tourist trip. A created itinerary of visits to one or more places of interest ([[TouristAttraction]]/[[TouristDestination]]) often linked by a similar theme, geographic area, or interest to a particular [[touristType]]. The [UNWTO](http://www2.unwto.org/) defines tourism trip as the Trip taken by visitors.
  (See examples below).""",
    )

    T_V_EPISODE = Semantic(
        id="TVEpisode",
        ref="schema:TVEpisode",
        text="""A TV episode which can be part of a series or season.""",
    )

    SOLD_OUT = Semantic(
        id="SoldOut",
        ref="schema:SoldOut",
        text="""Indicates that the item has sold out.""",
    )

    DEPENDENCIES = Semantic(
        id="dependencies",
        ref="schema:dependencies",
        text="""Prerequisites needed to fulfill steps in article.""",
    )

    INSERTION = Semantic(
        id="insertion",
        ref="schema:insertion",
        text="""The place of attachment of a muscle, or what the muscle moves.""",
    )

    EMPLOYMENT_TYPE = Semantic(
        id="employmentType",
        ref="schema:employmentType",
        text="""Type of employment (e.g. full-time, part-time, contract, temporary, seasonal, internship).""",
    )

    WATERFALL = Semantic(
        id="Waterfall", ref="schema:Waterfall", text="""A waterfall, like Niagara."""
    )

    PARENT_ITEM = Semantic(
        id="parentItem",
        ref="schema:parentItem",
        text="""The parent of a question, answer or item in general.""",
    )

    MOVING_COMPANY = Semantic(
        id="MovingCompany", ref="schema:MovingCompany", text="""A moving company."""
    )

    FREE = Semantic(
        id="free",
        ref="schema:free",
        text="""A flag to signal that the item, event, or place is accessible for free.""",
    )

    RESERVATION_PENDING = Semantic(
        id="ReservationPending",
        ref="schema:ReservationPending",
        text="""The status of a reservation when a request has been sent, but not confirmed.""",
    )

    APARTMENT_COMPLEX = Semantic(
        id="ApartmentComplex",
        ref="schema:ApartmentComplex",
        text="""Residence type: Apartment complex.""",
    )

    CUSTOMER_REMORSE_RETURN_LABEL_SOURCE = Semantic(
        id="customerRemorseReturnLabelSource",
        ref="schema:customerRemorseReturnLabelSource",
        text="""The method (from an enumeration) by which the customer obtains a return shipping label for a product returned due to customer remorse.""",
    )

    VALUE_REFERENCE = Semantic(
        id="valueReference",
        ref="schema:valueReference",
        text="""A secondary value that provides additional information on the original value, e.g. a reference temperature or a type of measurement.""",
    )

    ADDRESS_REGION = Semantic(
        id="addressRegion",
        ref="schema:addressRegion",
        text="""The region in which the locality is, and which is in the country. For example, California or another appropriate first-level [Administrative division](https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country) """,
    )

    SPORTS_TEAM = Semantic(
        id="sportsTeam",
        ref="schema:sportsTeam",
        text="""A sub property of participant. The sports team that participated on this action.""",
    )

    PUBLICATION_TYPE = Semantic(
        id="publicationType",
        ref="schema:publicationType",
        text="""The type of the medical article, taken from the US NLM MeSH publication type catalog. See also [MeSH documentation](http://www.nlm.nih.gov/mesh/pubtypes.html).""",
    )

    ADVANCE_BOOKING_REQUIREMENT = Semantic(
        id="advanceBookingRequirement",
        ref="schema:advanceBookingRequirement",
        text="""The amount of time that is required between accepting the offer and the actual usage of the resource or service.""",
    )

    PART_OF_SYSTEM = Semantic(
        id="partOfSystem",
        ref="schema:partOfSystem",
        text="""The anatomical or organ system that this structure is part of.""",
    )

    PRICE_SPECIFICATION = Semantic(
        id="priceSpecification",
        ref="schema:priceSpecification",
        text="""One or more detailed price specifications, indicating the unit price and delivery or payment charges.""",
    )

    SUSPENDED = Semantic(id="Suspended", ref="schema:Suspended", text="""Suspended.""")

    E_BOOK = Semantic(id="EBook", ref="schema:EBook", text="""Book format: Ebook.""")

    VESSEL = Semantic(
        id="Vessel",
        ref="schema:Vessel",
        text="""A component of the human body circulatory system comprised of an intricate network of hollow tubes that transport blood throughout the entire body.""",
    )

    ASSOCIATED_PATHOPHYSIOLOGY = Semantic(
        id="associatedPathophysiology",
        ref="schema:associatedPathophysiology",
        text="""If applicable, a description of the pathophysiology associated with the anatomical system, including potential abnormal changes in the mechanical, physical, and biochemical functions of the system.""",
    )

    FLORIST = Semantic(id="Florist", ref="schema:Florist", text="""A florist.""")

    PSYCHIATRIC = Semantic(
        id="Psychiatric",
        ref="schema:Psychiatric",
        text="""A specific branch of medical science that is concerned with the study, treatment, and prevention of mental illness, using both medical and psychological therapies.""",
    )

    PLAYER_TYPE = Semantic(
        id="playerType",
        ref="schema:playerType",
        text="""Player type required&#x2014;for example, Flash or Silverlight.""",
    )

    SUGAR_CONTENT = Semantic(
        id="sugarContent",
        ref="schema:sugarContent",
        text="""The number of grams of sugar.""",
    )

    MONOISOTOPIC_MOLECULAR_WEIGHT = Semantic(
        id="monoisotopicMolecularWeight",
        ref="schema:monoisotopicMolecularWeight",
        text="""The monoisotopic mass is the sum of the masses of the atoms in a molecule using the unbound, ground-state, rest mass of the principal (most abundant) isotope for each element instead of the isotopic average mass. Please include the units the form \'&lt;Number&gt; &lt;unit&gt;\', for example \'770.230488 g/mol\' or as \'&lt;QuantitativeValue&gt;.""",
    )

    IS_ENCODED_BY_BIO_CHEM_ENTITY = Semantic(
        id="isEncodedByBioChemEntity",
        ref="schema:isEncodedByBioChemEntity",
        text="""Another BioChemEntity encoding by this one.""",
    )

    MAXIMUM_DOSE_SCHEDULE = Semantic(
        id="MaximumDoseSchedule",
        ref="schema:MaximumDoseSchedule",
        text="""The maximum dosing schedule considered safe for a drug or supplement as recommended by an authority or by the drug/supplement\'s manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.""",
    )

    VIRUS = Semantic(
        id="Virus",
        ref="schema:Virus",
        text="""Pathogenic virus that causes viral infection.""",
    )

    INELIGIBLE_REGION = Semantic(
        id="ineligibleRegion",
        ref="schema:ineligibleRegion",
        text="""The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.\\n\\nSee also [[eligibleRegion]].
      """,
    )

    TOURIST_TYPE = Semantic(
        id="touristType",
        ref="schema:touristType",
        text="""Attraction suitable for type(s) of tourist. eg. Children, visitors from a particular country, etc. """,
    )

    EVENT_MOVED_ONLINE = Semantic(
        id="EventMovedOnline",
        ref="schema:EventMovedOnline",
        text="""Indicates that the event was changed to allow online participation. See [[eventAttendanceMode]] for specifics of whether it is now fully or partially online.""",
    )

    MOVIE_THEATER = Semantic(
        id="MovieTheater", ref="schema:MovieTheater", text="""A movie theater."""
    )

    PLACE_OF_WORSHIP = Semantic(
        id="PlaceOfWorship",
        ref="schema:PlaceOfWorship",
        text="""Place of worship, such as a church, synagogue, or mosque.""",
    )

    TELEVISION_CHANNEL = Semantic(
        id="TelevisionChannel",
        ref="schema:TelevisionChannel",
        text="""A unique instance of a television BroadcastService on a CableOrSatelliteService lineup.""",
    )

    TRANSCRIPT = Semantic(
        id="transcript",
        ref="schema:transcript",
        text="""If this MediaObject is an AudioObject or VideoObject, the transcript of that object.""",
    )

    ENTRY_POINT = Semantic(
        id="EntryPoint",
        ref="schema:EntryPoint",
        text="""An entry point, within some Web-based protocol.""",
    )

    PAPERBACK = Semantic(
        id="Paperback", ref="schema:Paperback", text="""Book format: Paperback."""
    )

    MEDIAN = Semantic(id="median", ref="schema:median", text="""The median value.""")

    ARCHIVED_AT = Semantic(
        id="archivedAt",
        ref="schema:archivedAt",
        text="""Indicates a page or other link involved in archival of a [[CreativeWork]]. In the case of [[MediaReview]], the items in a [[MediaReviewItem]] may often become inaccessible, but be archived by archival, journalistic, activist, or law enforcement organizations. In such cases, the referenced page may not directly publish the content.""",
    )

    COURSE_MODE = Semantic(
        id="courseMode",
        ref="schema:courseMode",
        text="""The medium or means of delivery of the course instance or the mode of study, either as a text label (e.g. "online", "onsite" or "blended"; "synchronous" or "asynchronous"; "full-time" or "part-time") or as a URL reference to a term from a controlled vocabulary (e.g. https://ceds.ed.gov/element/001311#Asynchronous ).""",
    )

    ELIGIBLE_QUANTITY = Semantic(
        id="eligibleQuantity",
        ref="schema:eligibleQuantity",
        text="""The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.""",
    )

    PREVENTION_INDICATION = Semantic(
        id="PreventionIndication",
        ref="schema:PreventionIndication",
        text="""An indication for preventing an underlying condition, symptom, etc.""",
    )

    BROKER = Semantic(
        id="broker",
        ref="schema:broker",
        text="""An entity that arranges for an exchange between a buyer and a seller.  In most cases a broker never acquires or releases ownership of a product or service involved in an exchange.  If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred.""",
    )

    IS_LOCATED_IN_SUBCELLULAR_LOCATION = Semantic(
        id="isLocatedInSubcellularLocation",
        ref="schema:isLocatedInSubcellularLocation",
        text="""Subcellular location where this BioChemEntity is located; please use PropertyValue if you want to include any evidence.""",
    )

    GOLF_COURSE = Semantic(
        id="GolfCourse", ref="schema:GolfCourse", text="""A golf course."""
    )

    BUSINESS_FUNCTION = Semantic(
        id="BusinessFunction",
        ref="schema:BusinessFunction",
        text="""The business function specifies the type of activity or access (i.e., the bundle of rights) offered by the organization or business person through the offer. Typical are sell, rental or lease, maintenance or repair, manufacture / produce, recycle / dispose, engineering / construction, or installation. Proprietary specifications of access rights are also instances of this class.\\n\\nCommonly used values:\\n\\n* http://purl.org/goodrelations/v1#ConstructionInstallation\\n* http://purl.org/goodrelations/v1#Dispose\\n* http://purl.org/goodrelations/v1#LeaseOut\\n* http://purl.org/goodrelations/v1#Maintain\\n* http://purl.org/goodrelations/v1#ProvideService\\n* http://purl.org/goodrelations/v1#Repair\\n* http://purl.org/goodrelations/v1#Sell\\n* http://purl.org/goodrelations/v1#Buy
        """,
    )

    IN_BROADCAST_LINEUP = Semantic(
        id="inBroadcastLineup",
        ref="schema:inBroadcastLineup",
        text="""The CableOrSatelliteService offering the channel.""",
    )

    ORDER_CANCELLED = Semantic(
        id="OrderCancelled",
        ref="schema:OrderCancelled",
        text="""OrderStatus representing cancellation of an order.""",
    )

    SCHEDULE = Semantic(
        id="Schedule",
        ref="schema:Schedule",
        text="""A schedule defines a repeating time period used to describe a regularly occurring [[Event]]. At a minimum a schedule will specify [[repeatFrequency]] which describes the interval between occurences of the event. Additional information can be provided to specify the schedule more precisely.
      This includes identifying the day(s) of the week or month when the recurring event will take place, in addition to its start and end time. Schedules may also
      have start and end dates to indicate when they are active, e.g. to define a limited calendar of events.""",
    )

    EAR = Semantic(
        id="Ear",
        ref="schema:Ear",
        text="""Ear function assessment with clinical examination.""",
    )

    ISSN = Semantic(
        id="issn",
        ref="schema:issn",
        text="""The International Standard Serial Number (ISSN) that identifies this serial publication. You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L) for, this serial publication.""",
    )

    CHARITABLE_INCORPORATED_ORGANIZATION = Semantic(
        id="CharitableIncorporatedOrganization",
        ref="schema:CharitableIncorporatedOrganization",
        text="""CharitableIncorporatedOrganization: Non-profit type referring to a Charitable Incorporated Organization (UK).""",
    )

    ISRC_CODE = Semantic(
        id="isrcCode",
        ref="schema:isrcCode",
        text="""The International Standard Recording Code for the recording.""",
    )

    WARRANTY_PROMISE = Semantic(
        id="warrantyPromise",
        ref="schema:warrantyPromise",
        text="""The warranty promise(s) included in the offer.""",
    )

    ITEM_REVIEWED = Semantic(
        id="itemReviewed",
        ref="schema:itemReviewed",
        text="""The item that is being reviewed/rated.""",
    )

    VOLCANO = Semantic(
        id="Volcano", ref="schema:Volcano", text="""A volcano, like Fuji san."""
    )

    ACHIEVE_ACTION = Semantic(
        id="AchieveAction",
        ref="schema:AchieveAction",
        text="""The act of accomplishing something via previous efforts. It is an instantaneous action rather than an ongoing process.""",
    )

    DELIVERY_EVENT = Semantic(
        id="DeliveryEvent",
        ref="schema:DeliveryEvent",
        text="""An event involving the delivery of an item.""",
    )

    ENCODING = Semantic(
        id="encoding",
        ref="schema:encoding",
        text="""A media object that encodes this CreativeWork. This property is a synonym for associatedMedia.""",
    )

    INTERACTIVITY_TYPE = Semantic(
        id="interactivityType",
        ref="schema:interactivityType",
        text="""The predominant mode of learning supported by the learning resource. Acceptable values are \'active\', \'expositive\', or \'mixed\'.""",
    )

    LEGAL_STATUS = Semantic(
        id="legalStatus",
        ref="schema:legalStatus",
        text="""The drug or supplement\'s legal status, including any controlled substance schedules that apply.""",
    )

    HOW_TO_STEP = Semantic(
        id="HowToStep",
        ref="schema:HowToStep",
        text="""A step in the instructions for how to achieve a result. It is an ordered list with HowToDirection and/or HowToTip items.""",
    )

    RIGHT_HAND_DRIVING = Semantic(
        id="RightHandDriving",
        ref="schema:RightHandDriving",
        text="""The steering position is on the right side of the vehicle (viewed from the main direction of driving).""",
    )

    HAS_COURSE = Semantic(
        id="hasCourse",
        ref="schema:hasCourse",
        text="""A course or class that is one of the learning opportunities that constitute an educational / occupational program. No information is implied about whether the course is mandatory or optional; no guarantee is implied about whether the course will be available to everyone on the program.""",
    )

    POSSIBLE_COMPLICATION = Semantic(
        id="possibleComplication",
        ref="schema:possibleComplication",
        text="""A possible unexpected and unfavorable evolution of a medical condition. Complications may include worsening of the signs or symptoms of the disease, extension of the condition to other organ systems, etc.""",
    )

    IS_PROPRIETARY = Semantic(
        id="isProprietary",
        ref="schema:isProprietary",
        text="""True if this item\'s name is a proprietary/brand name (vs. generic name).""",
    )

    CAPTION = Semantic(
        id="caption",
        ref="schema:caption",
        text="""The caption for this object. For downloadable machine formats (closed caption, subtitles etc.) use MediaObject and indicate the [[encodingFormat]].""",
    )

    SPATIAL = Semantic(
        id="spatial",
        ref="schema:spatial",
        text="""The "spatial" property can be used in cases when more specific properties
(e.g. [[locationCreated]], [[spatialCoverage]], [[contentLocation]]) are not known to be appropriate.""",
    )

    BODY_MEASUREMENT_UNDERBUST = Semantic(
        id="BodyMeasurementUnderbust",
        ref="schema:BodyMeasurementUnderbust",
        text="""Girth of body just below the bust. Used, for example, to fit women\'s swimwear.""",
    )

    USER_DOWNLOADS = Semantic(
        id="UserDownloads",
        ref="schema:UserDownloads",
        text="""UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].""",
    )

    BASIC_INCOME = Semantic(
        id="BasicIncome",
        ref="schema:BasicIncome",
        text="""BasicIncome: this is a benefit for basic income.""",
    )

    RSVP_ACTION = Semantic(
        id="RsvpAction",
        ref="schema:RsvpAction",
        text="""The act of notifying an event organizer as to whether you expect to attend the event.""",
    )

    ORDER_ITEM_STATUS = Semantic(
        id="orderItemStatus",
        ref="schema:orderItemStatus",
        text="""The current status of the order item.""",
    )

    POTENTIAL_USE = Semantic(
        id="potentialUse",
        ref="schema:potentialUse",
        text="""Intended use of the BioChemEntity by humans.""",
    )

    ALL_WHEEL_DRIVE_CONFIGURATION = Semantic(
        id="AllWheelDriveConfiguration",
        ref="schema:AllWheelDriveConfiguration",
        text="""All-wheel Drive is a transmission layout where the engine drives all four wheels.""",
    )

    POSTAL_CODE_BEGIN = Semantic(
        id="postalCodeBegin",
        ref="schema:postalCodeBegin",
        text="""First postal code in a range (included).""",
    )

    MONETARY_AMOUNT = Semantic(
        id="MonetaryAmount",
        ref="schema:MonetaryAmount",
        text="""A monetary value or range. This type can be used to describe an amount of money such as $50 USD, or a range as in describing a bank account being suitable for a balance between £1,000 and £1,000,000 GBP, or the value of a salary, etc. It is recommended to use [[PriceSpecification]] Types to describe the price of an Offer, Invoice, etc.""",
    )

    COUNTRY_OF_ASSEMBLY = Semantic(
        id="countryOfAssembly",
        ref="schema:countryOfAssembly",
        text="""The place where the product was assembled.""",
    )

    ARRIVAL_AIRPORT = Semantic(
        id="arrivalAirport",
        ref="schema:arrivalAirport",
        text="""The airport where the flight terminates.""",
    )

    EXPRESSED_IN = Semantic(
        id="expressedIn",
        ref="schema:expressedIn",
        text="""Tissue, organ, biological sample, etc in which activity of this gene has been observed experimentally. For example brain, digestive system.""",
    )

    REFURBISHED_CONDITION = Semantic(
        id="RefurbishedCondition",
        ref="schema:RefurbishedCondition",
        text="""Indicates that the item is refurbished.""",
    )

    NAIL_SALON = Semantic(
        id="NailSalon", ref="schema:NailSalon", text="""A nail salon."""
    )

    CHURCH = Semantic(id="Church", ref="schema:Church", text="""A church.""")

    LODGING_UNIT_TYPE = Semantic(
        id="lodgingUnitType",
        ref="schema:lodgingUnitType",
        text="""Textual description of the unit type (including suite vs. room, size of bed, etc.).""",
    )

    GENE = Semantic(
        id="Gene",
        ref="schema:Gene",
        text="""A discrete unit of inheritance which affects one or more biological traits (Source: [https://en.wikipedia.org/wiki/Gene](https://en.wikipedia.org/wiki/Gene)). Examples include FOXP2 (Forkhead box protein P2), SCARNA21 (small Cajal body-specific RNA 21), A- (agouti genotype).""",
    )

    PARCEL_DELIVERY = Semantic(
        id="ParcelDelivery",
        ref="schema:ParcelDelivery",
        text="""The delivery of a parcel either via the postal service or a commercial service.""",
    )

    RSVP_RESPONSE_MAYBE = Semantic(
        id="RsvpResponseMaybe",
        ref="schema:RsvpResponseMaybe",
        text="""The invitee may or may not attend.""",
    )

    IMAGE_OBJECT_SNAPSHOT = Semantic(
        id="ImageObjectSnapshot",
        ref="schema:ImageObjectSnapshot",
        text="""A specific and exact (byte-for-byte) version of an [[ImageObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata (e.g. XMP, EXIF) the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren\'t represented in their actual content, do not affect this notion of identity.""",
    )

    LIBRARY_SYSTEM = Semantic(
        id="LibrarySystem",
        ref="schema:LibrarySystem",
        text="""A [[LibrarySystem]] is a collaborative system amongst several libraries.""",
    )

    CONTENT_LOCATION = Semantic(
        id="contentLocation",
        ref="schema:contentLocation",
        text="""The location depicted or described in the content. For example, the location in a photograph or painting.""",
    )

    CODING_SYSTEM = Semantic(
        id="codingSystem",
        ref="schema:codingSystem",
        text="""The coding system, e.g. \'ICD-10\'.""",
    )

    PARENTS = Semantic(
        id="parents", ref="schema:parents", text="""A parents of the person."""
    )

    TRUE = Semantic(id="True", ref="schema:True", text="""The boolean value true.""")

    PAYMENT_CHARGE_SPECIFICATION = Semantic(
        id="PaymentChargeSpecification",
        ref="schema:PaymentChargeSpecification",
        text="""The costs of settling the payment using a particular payment method.""",
    )

    TOC_ENTRY = Semantic(
        id="tocEntry",
        ref="schema:tocEntry",
        text="""Indicates a [[HyperTocEntry]] in a [[HyperToc]].""",
    )

    SPORTS_EVENT = Semantic(
        id="SportsEvent", ref="schema:SportsEvent", text="""Event type: Sports event."""
    )

    HAS_VARIANT = Semantic(
        id="hasVariant",
        ref="schema:hasVariant",
        text="""Indicates a [[Product]] that is a member of this [[ProductGroup]] (or [[ProductModel]]).""",
    )

    DELIVERY_STATUS = Semantic(
        id="deliveryStatus",
        ref="schema:deliveryStatus",
        text="""New entry added as the package passes through each leg of its journey (from shipment to final delivery).""",
    )

    FOLLOWEE = Semantic(
        id="followee",
        ref="schema:followee",
        text="""A sub property of object. The person or organization being followed.""",
    )

    RESERVE_ACTION = Semantic(
        id="ReserveAction",
        ref="schema:ReserveAction",
        text="""Reserving a concrete object.\\n\\nRelated actions:\\n\\n* [[ScheduleAction]]: Unlike ScheduleAction, ReserveAction reserves concrete objects (e.g. a table, a hotel) towards a time slot / spatial allocation.""",
    )

    SUPERSEDED_BY = Semantic(
        id="supersededBy",
        ref="schema:supersededBy",
        text="""Relates a term (i.e. a property, class or enumeration) to one that supersedes it.""",
    )

    PLAYGROUND = Semantic(
        id="Playground", ref="schema:Playground", text="""A playground."""
    )

    COPYRIGHT_HOLDER = Semantic(
        id="copyrightHolder",
        ref="schema:copyrightHolder",
        text="""The party holding the legal copyright to the CreativeWork.""",
    )

    CASINO = Semantic(id="Casino", ref="schema:Casino", text="""A casino.""")

    CREDENTIAL_CATEGORY = Semantic(
        id="credentialCategory",
        ref="schema:credentialCategory",
        text="""The category or type of credential being described, for example "degree”, “certificate”, “badge”, or more specific term.""",
    )

    GAME_SERVER = Semantic(
        id="GameServer",
        ref="schema:GameServer",
        text="""Server that provides game interaction in a multiplayer game.""",
    )

    U_K_TRUST = Semantic(
        id="UKTrust",
        ref="schema:UKTrust",
        text="""UKTrust: Non-profit type referring to a UK trust.""",
    )

    OBSERVATIONAL = Semantic(
        id="Observational",
        ref="schema:Observational",
        text="""An observational study design.""",
    )

    GATED_RESIDENCE_COMMUNITY = Semantic(
        id="GatedResidenceCommunity",
        ref="schema:GatedResidenceCommunity",
        text="""Residence type: Gated community.""",
    )

    EDUCATION_REQUIREMENTS = Semantic(
        id="educationRequirements",
        ref="schema:educationRequirements",
        text="""Educational background needed for the position or Occupation.""",
    )

    CONTACT_OPTION = Semantic(
        id="contactOption",
        ref="schema:contactOption",
        text="""An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers).""",
    )

    PARKING_MAP = Semantic(
        id="ParkingMap", ref="schema:ParkingMap", text="""A parking map."""
    )

    SEAT = Semantic(
        id="Seat",
        ref="schema:Seat",
        text="""Used to describe a seat, such as a reserved seat in an event reservation.""",
    )

    IN_SUPPORT_OF = Semantic(
        id="inSupportOf",
        ref="schema:inSupportOf",
        text="""Qualification, candidature, degree, application that Thesis supports.""",
    )

    CREATIVE_WORK_SERIES = Semantic(
        id="CreativeWorkSeries",
        ref="schema:CreativeWorkSeries",
        text="""A CreativeWorkSeries in schema.org is a group of related items, typically but not necessarily of the same kind. CreativeWorkSeries are usually organized into some order, often chronological. Unlike [[ItemList]] which is a general purpose data structure for lists of things, the emphasis with CreativeWorkSeries is on published materials (written e.g. books and periodicals, or media such as tv, radio and games).\\n\\nSpecific subtypes are available for describing [[TVSeries]], [[RadioSeries]], [[MovieSeries]], [[BookSeries]], [[Periodical]] and [[VideoGameSeries]]. In each case, the [[hasPart]] / [[isPartOf]] properties can be used to relate the CreativeWorkSeries to its parts. The general CreativeWorkSeries type serves largely just to organize these more specific and practical subtypes.\\n\\nIt is common for properties applicable to an item from the series to be usefully applied to the containing group. Schema.org attempts to anticipate some of these cases, but publishers should be free to apply properties of the series parts to the series as a whole wherever they seem appropriate.
	  """,
    )

    CURRENCY = Semantic(
        id="currency",
        ref="schema:currency",
        text="""The currency in which the monetary amount is expressed.\\n\\nUse standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217) e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies e.g. "BTC"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types e.g. "Ithaca HOUR".""",
    )

    PAGINATION = Semantic(
        id="pagination",
        ref="schema:pagination",
        text="""Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49".""",
    )

    VEHICLE_MODEL_DATE = Semantic(
        id="vehicleModelDate",
        ref="schema:vehicleModelDate",
        text="""The release date of a vehicle model (often used to differentiate versions of the same make and model).""",
    )

    CONTRIBUTOR = Semantic(
        id="contributor",
        ref="schema:contributor",
        text="""A secondary contributor to the CreativeWork or Event.""",
    )

    THERAPEUTIC = Semantic(
        id="Therapeutic",
        ref="schema:Therapeutic",
        text="""A medical device used for therapeutic purposes.""",
    )

    BROADCAST_SUB_CHANNEL = Semantic(
        id="broadcastSubChannel",
        ref="schema:broadcastSubChannel",
        text="""The subchannel used for the broadcast.""",
    )

    CVD_NUM_BEDS_OCC = Semantic(
        id="cvdNumBedsOcc",
        ref="schema:cvdNumBedsOcc",
        text="""numbedsocc - HOSPITAL INPATIENT BED OCCUPANCY: Total number of staffed inpatient beds that are occupied.""",
    )

    CREATIVE_WORK_SEASON = Semantic(
        id="CreativeWorkSeason",
        ref="schema:CreativeWorkSeason",
        text="""A media season e.g. tv, radio, video game etc.""",
    )

    COMEDY_EVENT = Semantic(
        id="ComedyEvent", ref="schema:ComedyEvent", text="""Event type: Comedy event."""
    )

    NONPROFIT501C14 = Semantic(
        id="Nonprofit501c14",
        ref="schema:Nonprofit501c14",
        text="""Nonprofit501c14: Non-profit type referring to State-Chartered Credit Unions, Mutual Reserve Funds.""",
    )

    IS_ACCESSIBLE_FOR_FREE = Semantic(
        id="isAccessibleForFree",
        ref="schema:isAccessibleForFree",
        text="""A flag to signal that the item, event, or place is accessible for free.""",
    )

    REPLACEE = Semantic(
        id="replacee",
        ref="schema:replacee",
        text="""A sub property of object. The object that is being replaced.""",
    )

    E_U_ENERGY_EFFICIENCY_CATEGORY_A = Semantic(
        id="EUEnergyEfficiencyCategoryA",
        ref="schema:EUEnergyEfficiencyCategoryA",
        text="""Represents EU Energy Efficiency Class A as defined in EU energy labeling regulations.""",
    )

    TICKER_SYMBOL = Semantic(
        id="tickerSymbol",
        ref="schema:tickerSymbol",
        text="""The exchange traded instrument associated with a Corporation object. The tickerSymbol is expressed as an exchange and an instrument name separated by a space character. For the exchange component of the tickerSymbol attribute, we recommend using the controlled vocabulary of Market Identifier Codes (MIC) specified in ISO15022.""",
    )

    KNOWS_ABOUT = Semantic(
        id="knowsAbout",
        ref="schema:knowsAbout",
        text="""Of a [[Person]], and less typically of an [[Organization]], to indicate a topic that is known about - suggesting possible expertise but not implying it. We do not distinguish skill levels here, or relate this to educational content, events, objectives or [[JobPosting]] descriptions.""",
    )

    SPECIALTY = Semantic(
        id="specialty",
        ref="schema:specialty",
        text="""One of the domain specialities to which this web page\'s content applies.""",
    )

    EVENT = Semantic(
        id="event",
        ref="schema:event",
        text="""Upcoming or past event associated with this place, organization, or action.""",
    )

    MUSIC_BY = Semantic(
        id="musicBy", ref="schema:musicBy", text="""The composer of the soundtrack."""
    )

    SINGLE_BLINDED_TRIAL = Semantic(
        id="SingleBlindedTrial",
        ref="schema:SingleBlindedTrial",
        text="""A trial design in which the researcher knows which treatment the patient was randomly assigned to but the patient does not.""",
    )

    GUIDELINE_SUBJECT = Semantic(
        id="guidelineSubject",
        ref="schema:guidelineSubject",
        text="""The medical conditions, treatments, etc. that are the subject of the guideline.""",
    )

    LEGISLATION_DATE_VERSION = Semantic(
        id="legislationDateVersion",
        ref="schema:legislationDateVersion",
        text="""The point-in-time at which the provided description of the legislation is valid (e.g. : when looking at the law on the 2016-04-07 (= dateVersion), I get the consolidation of 2015-04-12 of the "National Insurance Contributions Act 2015")""",
    )

    EVENT_SCHEDULED = Semantic(
        id="EventScheduled",
        ref="schema:EventScheduled",
        text="""The event is taking place or has taken place on the startDate as scheduled. Use of this value is optional, as it is assumed by default.""",
    )

    GOVERNMENT_SERVICE = Semantic(
        id="GovernmentService",
        ref="schema:GovernmentService",
        text="""A service provided by a government organization, e.g. food stamps, veterans benefits, etc.""",
    )

    PROJECT = Semantic(
        id="Project",
        ref="schema:Project",
        text="""An enterprise (potentially individual but typically collaborative), planned to achieve a particular aim.
Use properties from [[Organization]], [[subOrganization]]/[[parentOrganization]] to indicate project sub-structures. 
   """,
    )

    BRIDGE = Semantic(id="Bridge", ref="schema:Bridge", text="""A bridge.""")

    LIST_ITEM = Semantic(
        id="ListItem",
        ref="schema:ListItem",
        text="""An list item, e.g. a step in a checklist or how-to description.""",
    )

    ENGINE_POWER = Semantic(
        id="enginePower",
        ref="schema:enginePower",
        text="""The power of the vehicle\'s engine.
    Typical unit code(s): KWT for kilowatt, BHP for brake horsepower, N12 for metric horsepower (PS, with 1 PS = 735,49875 W)\\n\\n* Note 1: There are many different ways of measuring an engine\'s power. For an overview, see  [http://en.wikipedia.org/wiki/Horsepower#Engine_power_test_codes](http://en.wikipedia.org/wiki/Horsepower#Engine_power_test_codes).\\n* Note 2: You can link to information about how the given value has been determined using the [[valueReference]] property.\\n* Note 3: You can use [[minValue]] and [[maxValue]] to indicate ranges.""",
    )

    PART_OF_ORDER = Semantic(
        id="partOfOrder",
        ref="schema:partOfOrder",
        text="""The overall order the items in this delivery were included in.""",
    )

    SHIPPING_DETAILS = Semantic(
        id="shippingDetails",
        ref="schema:shippingDetails",
        text="""Indicates information about the shipping policies and options associated with an [[Offer]].""",
    )

    COUNTRIES_SUPPORTED = Semantic(
        id="countriesSupported",
        ref="schema:countriesSupported",
        text="""Countries for which the application is supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.""",
    )

    LANDFORM = Semantic(
        id="Landform",
        ref="schema:Landform",
        text="""A landform or physical feature.  Landform elements include mountains, plains, lakes, rivers, seascape and oceanic waterbody interface features such as bays, peninsulas, seas and so forth, including sub-aqueous terrain features such as submersed mountain ranges, volcanoes, and the great ocean basins.""",
    )

    HAS_MAP = Semantic(
        id="hasMap", ref="schema:hasMap", text="""A URL to a map of the place."""
    )

    TEXT = Semantic(id="Text", ref="schema:Text", text="""Data type: Text.""")

    ACCESSIBILITY_CONTROL = Semantic(
        id="accessibilityControl",
        ref="schema:accessibilityControl",
        text="""Identifies input methods that are sufficient to fully control the described resource ([WebSchemas wiki lists possible values](http://www.w3.org/wiki/WebSchemas/Accessibility)).""",
    )

    PHYSICAL_ACTIVITY_CATEGORY = Semantic(
        id="PhysicalActivityCategory",
        ref="schema:PhysicalActivityCategory",
        text="""Categories of physical activity, organized by physiologic classification.""",
    )

    ASSOCIATED_ANATOMY = Semantic(
        id="associatedAnatomy",
        ref="schema:associatedAnatomy",
        text="""The anatomy of the underlying organ system or structures associated with this entity.""",
    )

    WINNER = Semantic(
        id="winner",
        ref="schema:winner",
        text="""A sub property of participant. The winner of the action.""",
    )

    ONCOLOGIC = Semantic(
        id="Oncologic",
        ref="schema:Oncologic",
        text="""A specific branch of medical science that deals with benign and malignant tumors, including the study of their development, diagnosis, treatment and prevention.""",
    )

    PAGE_END = Semantic(
        id="pageEnd",
        ref="schema:pageEnd",
        text="""The page on which the work ends; for example "138" or "xvi".""",
    )

    INFECTIOUS_AGENT_CLASS = Semantic(
        id="infectiousAgentClass",
        ref="schema:infectiousAgentClass",
        text="""The class of infectious agent (bacteria, prion, etc.) that causes the disease.""",
    )

    RESERVED_TICKET = Semantic(
        id="reservedTicket",
        ref="schema:reservedTicket",
        text="""A ticket associated with the reservation.""",
    )

    GEO_RADIUS = Semantic(
        id="geoRadius",
        ref="schema:geoRadius",
        text="""Indicates the approximate radius of a GeoCircle (metres unless indicated otherwise via Distance notation).""",
    )

    COMMENT_COUNT = Semantic(
        id="commentCount",
        ref="schema:commentCount",
        text="""The number of comments this CreativeWork (e.g. Article, Question or Answer) has received. This is most applicable to works published in Web sites with commenting system; additional comments may exist elsewhere.""",
    )

    DEFAULT_VALUE = Semantic(
        id="defaultValue",
        ref="schema:defaultValue",
        text="""The default value of the input.  For properties that expect a literal, the default is a literal value, for properties that expect an object, it\'s an ID reference to one of the current values.""",
    )

    FAX_NUMBER = Semantic(
        id="faxNumber", ref="schema:faxNumber", text="""The fax number."""
    )

    USER_COMMENTS = Semantic(
        id="UserComments",
        ref="schema:UserComments",
        text="""UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].""",
    )

    APPLICATION_CONTACT = Semantic(
        id="applicationContact",
        ref="schema:applicationContact",
        text="""Contact details for further information relevant to this job posting.""",
    )

    SIGN_OR_SYMPTOM = Semantic(
        id="signOrSymptom",
        ref="schema:signOrSymptom",
        text="""A sign or symptom of this condition. Signs are objective or physically observable manifestations of the medical condition while symptoms are the subjective experience of the medical condition.""",
    )

    WARNING = Semantic(
        id="warning",
        ref="schema:warning",
        text="""Any FDA or other warnings about the drug (text or URL).""",
    )

    PURCHASE_DATE = Semantic(
        id="purchaseDate",
        ref="schema:purchaseDate",
        text="""The date the item e.g. vehicle was purchased by the current owner.""",
    )

    SERVICE_AUDIENCE = Semantic(
        id="serviceAudience",
        ref="schema:serviceAudience",
        text="""The audience eligible for this service.""",
    )

    PHOTOGRAPH_ACTION = Semantic(
        id="PhotographAction",
        ref="schema:PhotographAction",
        text="""The act of capturing still images of objects using a camera.""",
    )

    MINIMUM_ADVERTISED_PRICE = Semantic(
        id="MinimumAdvertisedPrice",
        ref="schema:MinimumAdvertisedPrice",
        text="""Represents the minimum advertised price ("MAP") (as dictated by the manufacturer) of an offered product.""",
    )

    PRICE_COMPONENT_TYPE = Semantic(
        id="priceComponentType",
        ref="schema:priceComponentType",
        text="""Identifies a price component (for example, a line item on an invoice), part of the total price for an offer.""",
    )

    OFFICE_EQUIPMENT_STORE = Semantic(
        id="OfficeEquipmentStore",
        ref="schema:OfficeEquipmentStore",
        text="""An office equipment store.""",
    )

    PRODUCT_SUPPORTED = Semantic(
        id="productSupported",
        ref="schema:productSupported",
        text="""The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. "iPhone") or a general category of products or services (e.g. "smartphones").""",
    )

    BCC_RECIPIENT = Semantic(
        id="bccRecipient",
        ref="schema:bccRecipient",
        text="""A sub property of recipient. The recipient blind copied on a message.""",
    )

    PRODUCT_COLLECTION = Semantic(
        id="ProductCollection",
        ref="schema:ProductCollection",
        text="""A set of products (either [[ProductGroup]]s or specific variants) that are listed together e.g. in an [[Offer]].""",
    )

    ACTIVATE_ACTION = Semantic(
        id="ActivateAction",
        ref="schema:ActivateAction",
        text="""The act of starting or activating a device or application (e.g. starting a timer or turning on a flashlight).""",
    )

    EVIDENCE_LEVEL_A = Semantic(
        id="EvidenceLevelA",
        ref="schema:EvidenceLevelA",
        text="""Data derived from multiple randomized clinical trials or meta-analyses.""",
    )

    COMPOUND_PRICE_SPECIFICATION = Semantic(
        id="CompoundPriceSpecification",
        ref="schema:CompoundPriceSpecification",
        text="""A compound price specification is one that bundles multiple prices that all apply in combination for different dimensions of consumption. Use the name property of the attached unit price specification for indicating the dimension of a price component (e.g. "electricity" or "final cleaning").""",
    )

    OWNS = Semantic(
        id="owns",
        ref="schema:owns",
        text="""Products owned by the organization or person.""",
    )

    VARIABLE_MEASURED = Semantic(
        id="variableMeasured",
        ref="schema:variableMeasured",
        text="""The variableMeasured property can indicate (repeated as necessary) the  variables that are measured in some dataset, either described as text or as pairs of identifier and description using PropertyValue.""",
    )

    A_3_D_MODEL = Semantic(
        id="3DModel",
        ref="schema:3DModel",
        text="""A 3D model represents some kind of 3D content, which may have [[encoding]]s in one or more [[MediaObject]]s. Many 3D formats are available (e.g. see [Wikipedia](https://en.wikipedia.org/wiki/Category:3D_graphics_file_formats)); specific encoding formats can be represented using the [[encodingFormat]] property applied to the relevant [[MediaObject]]. For the
case of a single file published after Zip compression, the convention of appending \'+zip\' to the [[encodingFormat]] can be used. Geospatial, AR/VR, artistic/animation, gaming, engineering and scientific content can all be represented using [[3DModel]].""",
    )

    MEDICAL_TRIAL = Semantic(
        id="MedicalTrial",
        ref="schema:MedicalTrial",
        text="""A medical trial is a type of medical study that uses scientific process used to compare the safety and efficacy of medical therapies or medical procedures. In general, medical trials are controlled and subjects are allocated at random to the different treatment and/or control groups.""",
    )

    DATA_FEED = Semantic(
        id="DataFeed",
        ref="schema:DataFeed",
        text="""A single feed providing structured information about one or more entities or topics.""",
    )

    THROAT = Semantic(
        id="Throat",
        ref="schema:Throat",
        text="""Throat assessment with  clinical examination.""",
    )

    RELEVANT_OCCUPATION = Semantic(
        id="relevantOccupation",
        ref="schema:relevantOccupation",
        text="""The Occupation for the JobPosting.""",
    )

    ELIGIBILITY_TO_WORK_REQUIREMENT = Semantic(
        id="eligibilityToWorkRequirement",
        ref="schema:eligibilityToWorkRequirement",
        text="""The legal requirements such as citizenship, visa and other documentation required for an applicant to this job.""",
    )
